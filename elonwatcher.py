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
            try:
                print('###'*10)
                elon = self._api.get_user(screen_name='elonmusk')
                print('Elon: ',elon)
                timeline = self._api.user_timeline(user_id = elon.id)
                print('Timeline: ', timeline)
                print('####'*10)
                newTweets = []
                for tweet in timeline:
                    newTweets.append(tweet.text)   
                    print(tweet.text)
                print('////'*10) 
                print('Novos tweets: ', newTweets)
                print('Tweets atuais:', self._actualTweets)
                print('////'*10)
                if(newTweets != self._actualTweets and self._actualTweets != []):
                    self._tBot.sendMessage('Opa, tweet novo do Elon musk: '+ newTweets[0])
                self._actualTweets = newTweets
                sleep(60)
            except IndexError:
                print("Erro de index")
            except Exception as err:
                print('Ocorreu um erro: ', err)
                
