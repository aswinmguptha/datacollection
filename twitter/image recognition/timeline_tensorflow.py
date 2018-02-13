import os
import json
from twython import Twython
from collections import Counter
from nltk import word_tokenize
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

stopwords_english = stopwords.words('english')
api_key = {
	'api_key': 'gRdl3mzjeeJpEsScpJfHAYy5g',
	'api_secret': 'Zvkh8twsEmlSbeXDySWFQzfNlW6HwURbZnWgiqWVApIDGZiIDt',
	'access_token': '476540708-NaWoCEMRYB0WVI3Knv5y1nwf4LVPCuk3xHMw8ucN',
	'access_token_secret': '169ZM65KBEKy7gqRdagID6WygLmx2lboUQLYn7uotFhKx'
}

twitter = Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)

def search_tweets(userid, MaxTweet):
	timeline = []
	tweets = []
	unigrams = []
	all_unigrams = []
	stemmed_unigrams = []
	all_stemmed_unigrams = []
	list_of_tweets = []
	all_unigrams_without_noise = []
	all_bigrams = []
	id_of_earliest_tweet = None
	tweet_count = 0
	check = 0
	
	print "Fetching tweets..."
	while tweet_count < MaxTweet:
		if id_of_earliest_tweet <= 0:
			timeline += twitter.get_user_timeline(screen_name=userid, count="100", tweet_mode='extended', exclude_replies='true')
		else:
			timeline += twitter.get_user_timeline(screen_name=userid, count="100", tweet_mode='extended', max_id=id_of_earliest_tweet - 1, exclude_replies='true')		
		
		for tweet in timeline:
			tweets.append(tweet['full_text'])
			list_of_tweets.append(tweet['id'])
			tweet_count = len(tweets)
			if check < 50:
				try:
					extended_entities = tweet['extended_entities']
					media = extended_entities['media']
					if media[0]['type'] == 'photo':
						url = media[0]['media_url']
						name = url.split('/')
						os.system('wget ' + url)
						out = os.popen('python /home/guptha/Privacy/models/tutorials/image/imagenet/classify_image.py --image_file /home/guptha/Privacy/' + name[len(name) - 1]).read()
						out = out.split(' (')[0].split()
						for each in out:
							unigrams.append(each.strip(','))
						check += 1
				except KeyError as e:
					continue
		
		id_of_earliest_tweet = sorted(list_of_tweets)[0]

	for each in unigrams:
		unigram = word_tokenize(each.lower())
		all_unigrams += unigram

	stemmer = PorterStemmer()
	for word in all_unigrams:
		stemmed_unigram = stemmer.stem(word)
		all_stemmed_unigrams.append(stemmed_unigram)

	for word in all_stemmed_unigrams:
		if word in stopwords_english or len(word) < 3 or 'http' in word:
			continue
		else:
			all_unigrams_without_noise.append(word)

	all_bigrams = list(ngrams(all_unigrams_without_noise,2))
	frequencies = Counter(all_bigrams)

	for token,count in frequencies.most_common(20):
		print token,count

search_tweets('ponguru', 2096)