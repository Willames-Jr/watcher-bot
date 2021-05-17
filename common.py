from elonwatcher import ElonWatcher


class SharedInfo:
    __actualElonTweets = []
    __actualBinanceNews = []

    @property
    def actualElonTweets(self):
        return self.__actualElonTweets
    
    @actualElonTweets.setter
    def actualElonTweets(self, value):
        self.__actualElonTweets = value

    @property
    def actualBinanceNews(self):
        return self.__actualBinanceNews
    
    @actualElonTweets.setter
    def actualBinanceNews(self, value):
        self.__actualBinanceNews = value

    @staticmethod
    def instance():
        if not SharedInfo.__instance:
            SharedInfo.__instance = SharedInfo()
        return SharedInfo.__instance