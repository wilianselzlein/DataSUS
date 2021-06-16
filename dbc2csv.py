import os
import sys

# print(sys.path)
# sys.path.append("/home/ivo/Dropbox/DataSUS/DataSUS/venv/")

import csv # https://docs.python.org/3/library/csv.html
import csv2df
# import dbf
# import PyTables
from tempfile import NamedTemporaryFile
# import geopandas as gpd
# from io import BytesIO
# from pysus.utilities.readdbc import read_dbc # not work
# from simpledbf import Dbf5
from dbfread import DBF #https://dbfread.readthedocs.io/en/latest/
from _readdbc import ffi, lib

# for file in os.listdir("data"):
#         if file.endswith(".dbf"):
#                 dbf = Dbf5("data/" + file, codec='utf-8')
#                 dbf.to_csv("data/csv/" + os.path.splitext(file)[0] + ".csv")

def dbc2dbf(infile, outfile):
    """
    Converts a DATASUS dbc file to a DBF database.
    :param infile: .dbc file name
    :param outfile: name of the .dbf file to be created.
    """
    if isinstance(infile, str):
        infile = infile.encode()
    if isinstance(outfile, str):
        outfile = outfile.encode()
    p = ffi.new('char[]', os.path.abspath(infile))
    q = ffi.new('char[]', os.path.abspath(outfile))

    lib.dbc2dbf([p], [q])

def read_dbc(file, encoding='utf-8', raw=False):
    """
    Opens a DATASUS .dbc file and return its contents as a pandas
    Dataframe.
    :param filename: .dbc filename
    :param encoding: encoding of the data
    :param raw: Skip type conversion. Set it to True to avoid type conversion errors
    :return: Pandas Dataframe.
    """
    if isinstance(file, str):
        filename = file.encode()

    tf = NamedTemporaryFile(delete=False)
    dbc2dbf(filename, tf.name.encode())

    try:
        db = DBF(tf.name, encoding=encoding, raw=raw)
    except:
        #db = dbf.Table(tf.name)
        try:
            db = DBF(tf.name, encoding='latin1', raw=raw)
        except: 
            print('erro')
            return

    # df = pd.DataFrame(iter(dbf))
    # dbf = Dbf5(tf.name, codec=encoding)
    # df =  dbf.to_dataframe() # gpd.GeoDataFrame(list(dbf))
    csvfile = open(file + '.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(db.field_names)
    for record in db:
        writer.writerow(list(record.values()))
    del db
    del writer

    csv2df.execute(file + '.csv')
    # os.system("zip " + file + ".zip " + file + ".csv > /dev/null")
    # os.system("rm " + file + ".csv")

    ##print('shape', df.shape)

    # compression_opts = dict(method='zip', archive_name=file+ '.csv')
    # df.to_csv(file + '.zip', sep='|', compression=compression_opts)

    ## del df

    # with NamedTemporaryFile(delete=False) as tf:
    #     dbc2dbf(filename, tf.name.encode())
    #     # print('read')
    #     dbf = DBF(tf.name, encoding=encoding, raw=raw)
    #     df = pd.DataFrame(iter(dbf))
    #     # dbf = Dbf5(tf.name, codec=encoding)
    #     # df =  dbf.to_dataframe() #  #gpd.GeoDataFrame(list(dbf))
    #     del dbf

    #     print('shape', df.shape)

    #     compression_opts = dict(method='zip', archive_name=file+ '.csv')
    #     df.to_csv(file + '.zip', sep='|', compression=compression_opts)

    #     del df
        
    os.unlink(tf.name)
    del tf
