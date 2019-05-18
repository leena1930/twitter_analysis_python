from tweepy import Stream
from tweepy.streaming import StreamListener
from Source.twitter_client import get_twitter_client

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            with open('python.json', 'a')as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data:  {}".format(str(e)))
            return True

    def on_error(self,status):
        print(status)
        return True

client = get_twitter_client()
twitter_stream = Stream(client.auth, MyListener())
twitter_stream.filter(track=['#python'])


