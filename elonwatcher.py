import tweepy
import threading
from time import sleep

class ElonWatcher(threading.Thread):

    def __init__(self, telegramBot):
        threading.Thread.__init__(self)
        auth = tweepy.AppAuthHandler('f0mctwBL4MKh33IPK236rLfoF', '6hYynD9Ze1pwYKBWhtIlMbke0v96XZRW2Wgq6MdF7W6sJAzdEf')
        self._api = tweepy.API(auth)
        self._actualTweets = []
        self._tBot = telegramBot
    
    def run(self):
        while True:
            elon = self._api.get_user(screen_name='elonmusk')
            timeline = self._api.user_timeline(user_id = elon.id)
            newTweets = []
            for tweet in timeline:
                newTweets.append(tweet.text)    
            if(newTweets != self._actualTweets and self._actualTweets != []):
                self._tBot.sendMessage('Opa, tweet novo do Elon musk: '+ newTweets[0])
            self._actualTweets = newTweets
            sleep(30)
            
