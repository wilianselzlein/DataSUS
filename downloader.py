from ftplib import FTP
import config
import log
import os
import dbc2csv

log = log.get_logger("main")

# encongind='utf-8'
def execute(type, state, year, month, encoding="iso-8859-1"): #, raw=False

    ftp = FTP(config.ftp_datasus)
    ftp.login()
    # ftp.cwd("dissemin/publicos/SIHSUS/200801_/Dados/") #ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/
    # ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/
    ftp.cwd("dissemin/publicos/" + type + "SUS/200801_/Dados/")
    all_files = ftp.nlst(".")
    state_prefix = "PA" + state  # "SPSP18" # "ERSP" "RJSP" "RDSP"

    files = sorted([file for file in all_files if state_prefix in file])

    for file in files:
  
        log.info("Downloading {}...".format(file))
        # if file not exists
        fp = open(file, "wb")
        ftp.retrbinary("RETR {}".format(file), fp.write)

        dbc2csv.read_dbc(file, encoding=encoding)

        fp.close()
        del fp

        os.remove(file)
