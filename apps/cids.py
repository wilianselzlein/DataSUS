import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import DataFrameReader, SQLContext, SparkSession
import os
import config

if __name__ == "__main__":
    """
        Usage: table, cid
    """

    if len(sys.argv) != 2:
        print("Need arg table name and CID")
        exit(0)

    spark = SparkSession\
        .builder\
        .appName("CIDs")\
        .config("spark.jars", config.spark_jar) \
        .master(config.spark_url) \
        .getOrCreate()

    sc = spark.sparkContext
    sqlContext=SQLContext(sc)

    url = '{}://{}:{}/{}'.format(config.postgres_driver, config.postgres_host, config.postgres_port, config.postgres_db)
    dbConnectionUrl = "jdbc:" + url
    mode = "overwrite"
    properties = {'user': config.postgres_user, 'password': config.postgres_pass, 'driver': config.postgres_drive_full}
    
    df = DataFrameReader(sqlContext).jdbc(url='jdbc:%s' % url, table= sys.argv[1], properties=properties)
    # count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    cid = sys.argv[2].lower()
    print("CID %s" % cid)
    ins = df.where('lower(pa_cidpri) like "{}%"'.format(cid))
    table = "cid_{}".format(cid)
    ins.write.jdbc(url=dbConnectionUrl, table=table, mode=mode, properties=properties)

    del ins

    spark.stop()
