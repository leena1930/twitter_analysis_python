import tweepy
from tweepy import OAuthHandler
import json

consumer_key ='iVVc1CyuW1HIPkU12qWV9tm7F'
consumer_secret='2OFEyGzqDYQHvv62izoQlxP23uoXqdJJHlpMJoXi716wObG1US'
access_token='206630724-mDavL7P5yDN5u8aqxEZoYavlvcds1jMzpsduhj77'
access_secret ='w2R2KXOhnnOdgZEVbWS51X1MkBmxMOKDGXSNu634jlb8L'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api =tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

#List of Tweets in text
for status in tweepy.Cursor(api.home_timeline).items(10):
    #process a single status
    print(status.text)

##List of Tweets in json
for status in tweepy.Cursor(api.home_timeline).items(10):
    #process a single status
    process_or_store(status._json)

#List of followers

for friend in tweepy.Cursor(api.friends).items(10):
    process_or_store(friend._json)

