import tweepy
from textblob import TextBlob 
#remember those import statements are case sensitive!!!


#twitter keys
consumer_key = 'ZpeVr5w08FBtsgifFR1B9h2AB'
consumer_secret = '0wcmUV3KEvsQnZTCkJvHwLBDX1lP7vZmGVIss09FNS2pUXm0hp'

accesstoken = '193624874-ZClEg4pw0ZPJpnzXoa0a2AmSeZNSKy57AFcctMAT'
acesstokensecret = 'etdVvwkaTyOTZWaR9qy0Fyk8wb1pFpPNVfJtP6sGo7cob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accesstoken, acesstokensecret)

api = tweepy.API(auth)

public_tweets = api.search('cats')
#this for loop goes through a list of tweets with similar sentiment
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)