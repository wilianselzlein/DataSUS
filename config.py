import os
import logging

logger_name = "main"
ftp_datasus = "ftp.datasus.gov.br"
cwd_ftp = "dissemin/publicos/{}SUS/200801_/Dados/"

postgres_driver = "postgresql"
postgres_user = "postgres"
postgres_pass = "postgres"
postgres_host = os.environ.get("POSTGRES_URI", "localhost") #127.0.0.1
postgres_db = "datasus"
postgres_port = 5432
postgres_dsn = "{0}://{1}:{2}@{3}:{4}/{5}".format(postgres_driver, postgres_user, postgres_pass, postgres_host, postgres_port, postgres_db)

chunks = 500000

DEBUG_LEVEL = logging.DEBUG
