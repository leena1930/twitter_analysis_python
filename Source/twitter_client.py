import tweepy
from tweepy import OAuthHandler
from tweepy import API
import config
import sys

def get_twitter_auth():

    consumer_key =config.consumer_key
    consumer_secret=config.consumer_secret
    access_token=config.access_token
    access_secret =config.access_secret
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth
    
def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client
    

def main():
    get_twitter_client()
    

if __name__ == '__main__':main()