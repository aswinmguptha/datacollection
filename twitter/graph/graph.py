from twython import Twython
import datetime
from highcharts import Highchart

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
chart = Highchart()
options = {
        'chart': {'type': 'line'},
        'title': {'text': 'Account Activity'},
        'legend': {'enabled':True},
        'xAxis': {
                'title' : {'text' : 'Time'},
                'categories' : ['Jan-Jun 2009', 'Jul-Dec 2009',  'Jan-Jun 2010', 'Jul-Dec 2010',  'Jan-Jun 2011', 'Jul-Dec 2011',  'Jan-Jun 2012', 'Jul-Dec 2012',  'Jan-Jun 2013', 'Jul-Dec 2013',  'Jan-Jun 2014', 'Jul-Dec 2014',  'Jan-Jun 2015', 'Jul-Dec 2015',  'Jan-Jun 2016', 'Jul-Dec 2016',  'Jan-Jun 2017', 'Jul-Dec 2017']
        },
        'yAxis':{
                        'title': {'text': 'Number of tweets'}
        },
}

def search_tweets(userid, MaxTweet):
	id_of_earliest_tweet = None
	count = 0
	list_of_tweets = []
	timeline = []
	tweets = []
	print "Fetching tweets..."
	while count < MaxTweet:
		if id_of_earliest_tweet <= 0:
			t = twitter.get_user_timeline(screen_name=userid, count="100", exclude_replies='true')
                        timeline += t
		else:
			t = twitter.get_user_timeline(screen_name=userid, count="100", max_id=id_of_earliest_tweet - 1, exclude_replies='true')
                        timeline += t
		for tweet in t:
			list_of_tweets.append(tweet['id'])
                        print tweet['id']
                        count += 1
		
		tweet_count = len(t)
		if tweet_count:
			id_of_earliest_tweet = sorted(list_of_tweets)[0]
		else:
			break
	t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18 = [0 for i in range(0, 18)]
	for tweet in timeline:
		d = tweet['created_at'].split()
		date = datetime.datetime.strptime(d[1] + " " + d[2] + " " + d[5], '%b %d %Y')
                print date
		if (datetime.datetime(2009, 1, 1) <= date <= datetime.datetime(2009, 6, 30)):
		    t1 += 1
		elif (datetime.datetime(2009, 7, 1) <= date <= datetime.datetime(2009, 12, 31)):
		    t2 += 1
		elif (datetime.datetime(2010, 1, 1) <= date <= datetime.datetime(2010, 6, 30)):
		    t3 += 1
		elif (datetime.datetime(2010, 7, 1) <= date <= datetime.datetime(2010, 12, 31)):
		    t4 += 1
		elif (datetime.datetime(2011, 1, 1) <= date <= datetime.datetime(2011, 6, 30)):
		    t5 += 1
		elif (datetime.datetime(2011, 7, 1) <= date <= datetime.datetime(2011, 12, 31)):
		    t6 += 1
		elif (datetime.datetime(2012, 1, 1) <= date <= datetime.datetime(2012, 6, 30)):
		    t7 += 1
		elif (datetime.datetime(2012, 7, 1) <= date <= datetime.datetime(2012, 12, 31)):
		    t8 += 1
		elif (datetime.datetime(2013, 1, 1) <= date <= datetime.datetime(2013, 6, 30)):
		    t9 += 1
		elif (datetime.datetime(2013, 7, 1) <= date <= datetime.datetime(2013, 12, 31)):
		    t10 += 1
		elif (datetime.datetime(2014, 1, 1) <= date <= datetime.datetime(2014, 6, 30)):
		    t11 += 1
		elif (datetime.datetime(2014, 7, 1) <= date <= datetime.datetime(2014, 12, 31)):
		    t12 += 1
		elif (datetime.datetime(2015, 1, 1) <= date <= datetime.datetime(2015, 6, 30)):
		    t13 += 1
		elif (datetime.datetime(2015, 7, 1) <= date <= datetime.datetime(2015, 12, 31)):
		    t14 += 1
		elif (datetime.datetime(2016, 1, 1) <= date <= datetime.datetime(2016, 6, 30)):
		    t15 += 1
		elif (datetime.datetime(2016, 7, 1) <= date <= datetime.datetime(2016, 12, 31)):
		    t16 += 1
		elif (datetime.datetime(2017, 1, 1) <= date <= datetime.datetime(2017, 6, 30)):
		    t17 += 1
		elif (datetime.datetime(2017, 7, 1) <= date <= datetime.datetime(2017, 12, 31)):
			t18 += 1
	print t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18
	data1 = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18]
        chart.set_dict_options(options)
        chart.add_data_set(data1,'line', "ponguru's tweets")
        chart.save_file('./charts')

search_tweets('ponguru', 1939)
