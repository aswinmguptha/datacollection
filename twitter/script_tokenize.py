import json
# import sys
import time
# import os
from pymongo import MongoClient
from twython import Twython

api_key = {
	'api_key': # Replace with api key,
	'api_secret': # Replace with api secret,
	'access_token': # Replace with access token,
	'access_token_secret': # Replace with access token secret
}

twitter= Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)

def search_tweets(search_phrase):


	count = 0
	tweetCount = 0
	list_of_tweets = []
        
	new_statuses = twitter.search(q=search_phrase, count="100", include_entities= True)
	tweetCount += len(new_statuses['statuses'])

	print tweetCount

	for tweet in new_statuses['statuses']:
		count += 1
		print json.dumps(tweet, indent=4)
		list_of_tweets.append(tweet['id'])
        tmp = sorted(list_of_tweets)[0]

        new_statuses = twitter.search(q=search_phrase, count="100", include_entities= True, max_id=tmp)
	tweetCount += len(new_statuses['statuses'])

	print tweetCount

	for tweet in new_statuses['statuses']:
		count += 1
		print json.dumps(tweet, indent=4)
		list_of_tweets.append(tweet['id'])
		
                # Saving data in files

		with open('~/Privacy/smog/tweet'+str(count)+'.json', 'w') as outfile:
				json.dump(tweet,outfile)

	print "Total tweets: ", tweetCount

# First parameter: The keyword we wish to search for
search_tweets('#smog')
