# encongind='utf-8'
from ftplib import FTP
import config
import log
import os
import dbc2csv

log = log.get_logger(config.logger_name)

def execute(origin, type_sys, state, year, month, encoding="iso-8859-1"):

    ftp = FTP(config.ftp_datasus)
    ftp.login()
    # ftp.cwd("dissemin/publicos/SIHSUS/200801_/Dados/") #ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/
    # ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/
    ftp.cwd(config.cwd_ftp.format(origin))
    all_files = ftp.nlst(".")
    state_prefix = type_sys + state  # "SPSP18" "ERSP" "RJSP" "RDSP"

    files = sorted([file for file in all_files if state_prefix in file])

    for file in files:
        if year != "" and not state_prefix + year in file:
            continue
        if month != "" and not file.split(".")[0].endswith(month):
            continue

        if not os.path.isfile(file):
            log.info("Downloading {}...".format(file))
            fp = open(file, "wb")
            ftp.retrbinary("RETR {}".format(file), fp.write)
            fp.close()
            del fp

        dbc2csv.read_dbc(file, encoding=encoding)
        
        os.remove(file)
