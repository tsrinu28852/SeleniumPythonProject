import logging
import inspect

class LogGen:
    @staticmethod
    def loggen(logLevel=logging.DEBUG):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # By default, log all messages
        logger.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler(".//Logs//automation.log", mode='a')
        fileHandler.setLevel(logLevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger

