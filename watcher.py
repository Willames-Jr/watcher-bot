from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from telegramloggin import TelegramLogging
from elonwatcher import ElonWatcher

class NewsWatcher():

    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        opt.headless = True
        self._actualNews = []
        self._driver = webdriver.Chrome("C:/Users/willa/browser_drivers/chromedriver", options =  opt)
        self._tBot = TelegramLogging("1812454812:AAEhhHgr2hmtZs8h8ZGCRaTOJQAP4Ez0LlY")
        self._tBot.start()
        elonWatcher = ElonWatcher(self._tBot)
        elonWatcher.start()

    def startWatching(self):

        while True:
            self._driver.get('https://www.binance.com/en/support/announcement')
            content = self._driver.page_source
            soup = BeautifulSoup(content, features="html.parser")
            news = soup.find_all('a', attrs = {'class':'css-qinc3w'})
            count = 0
            newNews = []
            for new in news:
                if(count == 5):
                    break
                newNews.append(new)
                count += 1
            if(newNews != self._actualNews and self._actualNews != []):
                print("Atualização ")
                message = 'Nova notícia\"'+newNews[0].text+'\", link '+'www.binance.com'+newNews[0]['href']
                self._tBot.sendMessage(message)
            self._tBot.sendMessage('eae, watcherBot aqui')
            self._actualNews = newNews
            sleep(120)