import facebook
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams

stop_words = stopwords.words('english')
api_key = {
			'api_key': # Replace with your api key,
			'api_secret': # Replace with your api secret, 
			'access_token': # Replace with your access token,
		}
graph = facebook.GraphAPI(access_token= api_key['access_token'])
post = graph.get_object('narendramodi/feed',fields='caption,description,from,message,created_time,full_picture,id,link,status_type,story,story_tags,type,updated_time,with_tags,is_popular,actions')
all_token = []
all_stem_token = []
for status in post['data']:
    if 'message' in status:
        all_token += word_tokenize(status['message'].lower())
frequencies = Counter(all_token)
stemmer = PorterStemmer()
for token in all_token:
    all_stem_token.append(stemmer.stem(token))
print all_stem_token
for token, count in frequencies.most_common(25):
    if token in stop_words or len(token) < 3:
        continue
    print token, count
