import traceback
import functools
import logging
from colorlog import ColoredFormatter
import config
import coloredlogs

def get_logger(name):
    # logger.debug("this is a debugging message")
    # logger.info("this is an informational message")
    # logger.warning("this is a warning message")
    # logger.error("this is an error message")
    # logger.critical("this is a critical message")

    # LOGFORMAT = '%(log_color)s%(asctime)s - %(levelname)-8s[%(name)-25s | '\
    #             '%(process)-6d]%(reset)s | %(log_color)s%(message)s%(reset)s'

    logging.root.setLevel(config.DEBUG_LEVEL)

    # formatter = ColoredFormatter(LOGFORMAT)
    # stream = logging.StreamHandler()
    # stream.setLevel(logging.INFO)
    # stream.setFormatter(formatter)

    logger = logging.getLogger("{:15s}".format(name))
    coloredlogs.install(level="DEBUG", logger=logger)
    # logger.addHandler(stream)
    logger.propagate = False

    return logger