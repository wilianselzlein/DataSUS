#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Ivo'
__email__ = 'wilianselzlein@gmail.com'
__title__ = 'DataSUS'
__license__ = 'MIT'

import config
import time
import log
import importer 
import argparser

log = log.get_logger(config.logger_name)

if __name__ == '__main__':

    args_ = argparser.parser.parse_args()
    log.warning("Starting ")

    if args_.download:
        log.warning("Download {}".format(config.ftp_datasus))
        importer.execute(args_.origin, args_.type, args_.state, args_.year, args_.month)

    time.sleep(1)

    log.info("Finished")
