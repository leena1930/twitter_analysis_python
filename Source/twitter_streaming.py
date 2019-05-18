# To run this code, first edit config.py with your configuration, then:
#
# mkdir data
# python twitter_stream_download.py -q apple -d data
# 
# It will produce the list of tweets for the query "apple" 
# in the file data/stream_apple.json
import tweepy
from tweepy import OAuthHandler
from  tweepy import Stream
from tweepy.streaming import StreamListener
import time
import string
import argparse
import json
import config

# def get_parser():
#     """Get parser for command line arguments."""
#     parser = argparse.ArgumentParser(description="Twitter Downloader")
#     parser.add_argument("-q",
#                         "--query",
#                         dest="query",
#                         help="Query/Filter",
#                         default='-')
#     parser.add_argument("-d",
#                         "--data-dir",
#                         dest="data_dir",
#                         help="Output/Data Directory")
#     return parser

class CustomListener(StreamListener):
    '''custom streamlistener for streaming data'''
    def __init__(self,data_dir,query):
        query_fname = format_filename(query)
        self.outfile ="%s/stream_%s.json" % (data_dir,query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile,'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on data: {}\n".format(e))
            time.sleep(5)
            return True

    def on_error(self,status):
        if status == 420:
            print("Rate limit exceeded\n".format(status))
            return False
        else:
            print("Error {} \n".format(status))
            return True
   
def format_filename(fname):
        """Convert fname into a safe string for a file name.
                Return: string
                """
        return ''.join(convert_valid(one_char) for one_char in fname)
def convert_valid(one_char):
        """Convert a character into '_' if "invalid".
            Return: string
        """
        valid_chars = "-_.%s%s" % (string.ascii_letters,string.digits)
        if one_char in valid_chars:
            return one_char
        else:
            return '_'

def main():
    #parser =get_parser()
    #args =parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)
    twitter_stream =Stream(auth, CustomListener('data','GOT'))
    twitter_stream.filter(track=['GOT'],async=True)

if __name__ == '__main__': main()



   


        