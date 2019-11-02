from logging import getLogger, StreamHandler, DEBUG

def mylog(hoge):
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False
    logger.debug(hoge)
