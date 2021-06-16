import pandas as pd
import os
# import zipfile
import warnings
import log
import config 
from sqlalchemy import create_engine
import argparser
import re

# DIR = '/home/ivo/Downloads/DataSUS/SP/SIH/SP/'
# DIR = '/home/ivo/Downloads/DataSUS/SP/SIA/PA/'

# warnings.filterwarnings('ignore')
log = log.get_logger("main")
args_ = argparser.parser.parse_args()
TABLE = "{}_{}_{}".format(args_.origin, args_.type, args_.state).lower()
target_type = str

def execute(filename):
    # for file in sorted(os.listdir(DIR), reverse=True):
        # if file.endswith(".zip"):
            # filename = os.path.join(DIR, file)
            # print(filename)

    # zipper = zipfile.ZipFile(filename)
    # filename = filename.split('zip')[0] + 'csv'
    # print(filename)
    # fp = zipper.open(filename)
    # if '|' in str(fp.read()[:50]):
    
    with warnings.catch_warnings(record=True) as ws:
        warnings.simplefilter("always")

        df = pd.read_csv(filename, sep='|', index_col=0, nrows=1)
        columns = df.columns.str.lower()
        df = pd.read_csv(filename, sep='|', index_col=0, skiprows=1, chunksize=config.chunks, names=columns) #, low_memory=False

        # log.fatal("Warnings raised: " + ws)
        for w in ws:
            s = str(w.message)
            log.fatal("Warning message: " + s)
            match = re.search(r"Columns \(([0-9,]+)\) have mixed types\.", s)
            if match:
                columns = match.group(1).split(',') # Get columns as a list
                columns = [int(c) for c in columns]
                log.critical("Applying %s dtype to columns:" % target_type, columns)
                df.iloc[:,columns] = df.iloc[:,columns].astype(target_type)

        # if df.shape[1] == 35:
        #     fp = zipper.open(filename)
        #     df = pd.read_csv(fp, sep='|', index_col=False, low_memory=False)
        # if df.shape[1] == 0:
        #     fp = zipper.open(filename)
        #     df = pd.read_csv(fp, sep=',', index_col=False, low_memory=False)
        # log.info("DF readed {} shape ".format(df.shape))
        
        # print(df.columns)
        # print(df.head(1))
        # print(df.info())
        # print(df.dtypes)

        engine = create_engine(config.postgres_dsn)

        for chunk in df:
            chunk.to_sql(TABLE, engine, chunksize=config.chunks, if_exists='append') # method=callable	
            log.info("Chunk {} records ".format(chunk.shape))	
            del chunk

        del engine
        # fp.close()
        # zipper.close()
        del df
        # del fp, zipper
        #break
