import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
       url= config.get('common info','baseURL')
       return url

    @staticmethod
    def getUseremail():
       usermail= config.get('common info','userid')
       return usermail

    @staticmethod
    def getPassword():
       userPass= config.get('common info','userpass')
       return userPass
