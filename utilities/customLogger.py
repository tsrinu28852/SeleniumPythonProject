import logging

class LogGen:

    @staticmethod
    def loggen():
        #logging.basicConfig(filename='automation.log',
        logging.basicConfig(filename='.\\Logs\example.log', encoding='utf-8', level=logging.DEBUG)
                            #format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
