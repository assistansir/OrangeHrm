import configparser

config = configparser.RawConfigParser()
filepath = "D:\\OrangeHrm\\Configuration\\config.ini"
config.read(filepath)


class Readconfig:

    @staticmethod
    def GetUserName():
        username = config.get('common data', 'Username')
        return username


    @staticmethod
    def GetPassword():
        password = config.get('common data', 'Password')
        return password
