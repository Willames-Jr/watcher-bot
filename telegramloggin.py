import telebot
import threading

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

    def sendMessage(self, msg):
        if ( self._ids != [] ):
            for id in self._ids: 
                self._bot.send_message(id, msg)

    def run(self):
        self._bot.polling()