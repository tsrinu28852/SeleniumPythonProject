import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getInvalidUser():
        invalidUser = config.get('common info', 'invalid_username')
        return invalidUser

    @staticmethod
    def getInvalidUserPasswd():
        invalidUserPwd = config.get('common info', 'password_invalid_username')
        return invalidUserPwd