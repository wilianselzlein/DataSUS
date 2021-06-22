import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import DataFrameReader, SQLContext, SparkSession
import os

if __name__ == "__main__":
    """
        Usage: cids [CID,  or nothing]
    """
    spark = SparkSession\
        .builder\
        .appName("CIDs")\
        .config("spark.jars", "/opt/spark/jars/postgresql-42.2.22.jar") \
        .master('spark://wilian-ubuntu:7077') \
        .getOrCreate()

    sc = spark.sparkContext
    sqlContext=SQLContext(sc)

    url = 'postgresql://127.0.0.1:5432/datasus'
    properties = {'user':'postgres', 'password':'postgres', 'driver':'org.postgresql.Driver'}
    df = DataFrameReader(sqlContext).jdbc(url='jdbc:%s' % url, table='sia_pa_rs', properties=properties)

    if len(sys.argv) > 1:
        cids = [sys.argv[1]]
    else:
        cids = ['B342', 'B972', 'U049', 'U071']

# COVID
# B342 - Infecção por coronavírus de localização não especificada
# B972 - Coronavírus, como causa de doenças classificadas em outros capítulos
# U049 - Síndrome Respiratória Aguda Grave – SARS
# U071 - diagnóstico da Doença respiratória aguda devido ao COVID-19

    # count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    for cid in cids: #TODO scale
        print("CID %s" % cid)
        ins = df.where('PA_CIDPRI like "{}%"'.format(cid)) #.show()

        # Properties to connect to the database,
        # the JDBC driver is part of our build.sbt
        dbConnectionUrl = "jdbc:postgresql://localhost:5432/datasus"
        mode = "overwrite"
        table = "cid_{}".format(cid)
        # Write in a table called ch02
        ins.write.jdbc(url=dbConnectionUrl, table=table, mode=mode, properties=properties)

        del ins

    spark.stop()
