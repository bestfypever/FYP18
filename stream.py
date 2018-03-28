import tweepy
import time
from manager import Manager
consumer_key = 'v5WZMr6ZDC7t3n9Eq8FoYbOPW'
consumer_secret = '4OyjPO5BX7fGb8VnH292T7ILCgnYfaU1rMJa6VrkDa6Tq4bAwc'
access_token = '528267455-MNm6HmnzCmtLX8xBTkUNt0l8n7RwN82E6LkrV80r'
access_secret = 'GvY6pFR187sGUMzYnGLlZ4w3lgFiBFDkIOnX9f1t6bZjY'

__metaclass__ = type
class StreamManager():
    'manages StreamListener class'

    stream_instance = None
    languages = None

    class StreamListener(tweepy.StreamListener):
        'StreamListener class passed to tweepy.stream for callback functions'
        def __init__(self):
            tweepy.StreamListener.__init__(self)
            self.manager = Manager()
            
        def on_status(self, status):
            #print status.text.encode('utf8')
            self.manager.notify_observers(status)
            return True
    
        def on_error(self, code):
            print code
            return False

    def __init__(self, tracking_terms=None, languages=None):
        'authorize and initialize tweepy.Stream object'
        self.__start_stream(tracking_terms, languages)

    def __start_stream(self, tracking_terms, languages):
        'starts a singleton instance of StreamListener'
        if not self.stream_instance:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_secret)
            api = tweepy.API(auth)
            self.stream_instance = tweepy.Stream(auth=api.auth, listener=self.StreamListener())
            self.languages = languages
            if not languages:
                self.languages = ['en']
            if tracking_terms:
                self.stream_instance.filter(track=tracking_terms, languages=self.languages, async=True)
            else:
                self.stream_instance.sample(languages=self.languages, async=True)

    def stop_stream(self):
        if self.stream_instance:
            self.stream_instance.disconnect()
            del self.stream_instance

    def set_tracking_terms(self, terms):
        'restarts tweet stream with new filtering terms'
        self.stop_stream()
        self.__start_stream(terms, self.languages) 

if __name__=='__main__':
    stream_manager = StreamManager()
