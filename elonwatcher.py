import tweepy
import threading
from time import sleep
import common

class ElonWatcher(threading.Thread):

    def __init__(self, telegramBot):
        threading.Thread.__init__(self)
        auth = tweepy.AppAuthHandler('f0mctwBL4MKh33IPK236rLfoF', '6hYynD9Ze1pwYKBWhtIlMbke0v96XZRW2Wgq6MdF7W6sJAzdEf')
        self._api = tweepy.API(auth)
        self._actualTweets = []
        self._tBot = telegramBot
    
    def run(self):
        while True:
            try:
                elon = self._api.get_user(screen_name='elonmusk')
                timeline = self._api.user_timeline(user_id = elon.id, count = 5)
                newTweets = []
                for tweet in timeline:
                    newTweets.append(tweet)   
                print('////'*10) 
                print('Novos tweets: ', newTweets)
                print('Tweets atuais:', self._actualTweets)
                print('////'*10)
                if(newTweets[0] != self._actualTweets[0]):
                    self._tBot.sendMessage('Opa, tweet novo do Elon musk: '+ newTweets[0].text +'\nLink: https://twitter.com/elonmusk/status/'+tweet.id)
                self._actualTweets = newTweets
                
                common.SharedInfo.instance().actualElonTweets = self._actualTweets
                sleep(120)
            except IndexError:
                print("Erro de index no tweepy")
                self._actualTweets = newTweets
                
                common.SharedInfo.instance().actualElonTweets = self._actualTweets
                sleep(120)
            except Exception as err:
                print('Ocorreu um erro no tweepy: ', err)
                self._actualTweets = newTweets
                
                common.SharedInfo.instance().actualElonTweets = self._actualTweets
                sleep(120)
