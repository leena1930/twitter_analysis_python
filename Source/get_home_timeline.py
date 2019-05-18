import json
import tweepy 
from  Source.twitter_client import get_twitter_client
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import API



if __name__ == '__main__':
    # auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    # auth.set_access_token(config.access_token, config.access_secret)
    # client = API(auth) 
    client =get_twitter_client()
    with open('home_timeline.json','w')as f:
        for page in Cursor(client.home_timeline,count=200,include_rts=True).pages(4):
            for status in page:
                #process a single status
                f.write(json.dumps(status._json)+ '\n')




