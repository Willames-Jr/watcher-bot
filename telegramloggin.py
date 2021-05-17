import telebot
import threading
import common

class TelegramLogging(threading.Thread):
    def __init__(self, token):
        threading.Thread.__init__(self)
        self._bot = telebot.AsyncTeleBot(token)
        self._bot.set_update_listener(self.listener)
        self._ids = []

    def listener(self, messages):

        for m in messages:
            if m.content_type == 'text':
                if (m.text == '/start'):
                    if(m.chat.id not in self._ids):
                        self._ids.append(m.chat.id)
                    self.sendMessage("Olá, a partir de agora lhe manterei informado sobre notícias na binance e os tweets de Elon musk!")
                if(m.text == '/actualTweets'):
                    tweets = common.SharedInfo.instance().actualElonTweets

                    if(tweets == []):
                        self.sendMessage('Ops, ocorreu um erro ao pegar os tweets. Tente novamente mais tarde')
                    else:
                        message = "Aqui estão os Tweets: \n"
                        for tweet in tweets:
                            message += tweet + "\n"
                        self.sendMessage(message)
                if(m.text == '/actualNews'):
                    newNews = common.SharedInfo.instance().actualBinanceNews

                    if(newNews == []):
                        self.sendMessage('Ops, ocorreu um erro ao pegar as notícias. Tente novamente mais tarde')
                    else:
                        for news in newNews:
                            message = '\"'+news.text+'\", link '+'www.binance.com'+news['href']
                            self.sendMessage(message)
                if(m.text == '/help' or m.text == '/h'):
                    self.sendMessage("""
                        Olá Você pode usar a seguinte lista de comandos apra intergair comigo:\n
                            */actualNews - Retorna as ultimas notícias da Binance
                            */actualTweets - Retorna os últimos 5 tweets do Elon Musk 
                        Sempre que houver uma atualização lhe mandarei uma mensagem ;)
                    """)
                
    def sendMessage(self, msg):
        if ( self._ids != [] ):
            for id in self._ids: 
                self._bot.send_message(id, msg)

    def run(self):
        self._bot.polling()