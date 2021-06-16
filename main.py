import argparse
import config
import time
import log
import importer  

parser = argparse.ArgumentParser()

parser.add_argument(
    "--download", 
    help="Download FTP file and write in db", 
    action="store_true", 
    default=True
)

parser.add_argument(
    "--type",
    help="SIA or SIH",
    default="SIA",
    type=str
)

parser.add_argument(
    "--state",
    help="Example RS",
    default="RS",
    type=str
)

parser.add_argument(
    "--year",
    help="Example 2020",
    default="2021",
    type=str
)

parser.add_argument(
    "--month",
    help="Example 01",
    default="01",
    type=str
)

log = log.get_logger("main")

if __name__ == '__main__':

    args_ = parser.parse_args()
    log.warning("Starting ")

    if args_.download:
        log.warning("Download " + config.ftp_datasus)
        importer.execute(args_.type, args_.state, args_.year, args_.month)

    time.sleep(1)

    log.info("Finished")
