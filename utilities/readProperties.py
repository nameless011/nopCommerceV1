import configparser
import os

config = configparser.RawConfigParser()
path = ".\\Configurations\\config.ini"

config.read(path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo','baseurl')
        return url

    @staticmethod
    def getuseremail():
        useremail = config.get('commonInfo','username')
        return useremail

    @staticmethod
    def getpassword():
        password = config.get('commonInfo','password')
        return password


# print(ReadConfig.getApplicationURL())
# print(ReadConfig.getuseremail())
# print(ReadConfig.getpassword())