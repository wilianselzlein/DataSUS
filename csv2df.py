import pandas as pd
import os
# import zipfile
import warnings
import log

# DIR = '/home/ivo/Downloads/DataSUS/SP/SIH/SP/'
# DIR = '/home/ivo/Downloads/DataSUS/SP/SIA/PA/'

warnings.filterwarnings('ignore')

log = log.get_logger("main")

def execute(filename):
    # for file in sorted(os.listdir(DIR), reverse=True):
        # if file.endswith(".zip"):
            # filename = os.path.join(DIR, file)
            # print(filename)
    log.info(filename)

    # zipper = zipfile.ZipFile(filename)
    # filename = filename.split('zip')[0] + 'csv'
    # print(filename)
    # fp = zipper.open(filename)
    # if '|' in str(fp.read()[:50]):
    df = pd.read_csv(filename, sep='|', index_col=0, low_memory=False)
    # if df.shape[1] == 35:
    #     fp = zipper.open(filename)
    #     df = pd.read_csv(fp, sep='|', index_col=False, low_memory=False)
    # if df.shape[1] == 0:
    #     fp = zipper.open(filename)
    #     df = pd.read_csv(fp, sep=',', index_col=False, low_memory=False)
    print(df.shape)
    # print(df.columns)
    print(df.head(1))
    # fp.close()
    # zipper.close()
    del df, 
    # del fp, zipper
    #break

