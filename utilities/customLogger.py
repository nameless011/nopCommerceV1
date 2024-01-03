import os
import logging

console = logging.StreamHandler()
file = logging.FileHandler(os.path.abspath(os.curdir) + ".\\logs\\basic.log")


class LogGEN():
    @staticmethod
    def loggen():
        logging.basicConfig(
            # filename="basic.log",
            # encoding='utf-8',
            # level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            handlers=[file,console],
            # filemode='w'
        )
        #logging.root.setLevel(logging.NOTSET)
        logger = logging.getLogger('test_login4')
        logger.setLevel(logging.DEBUG)
        return logger
