import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    """
        Usage: cids [CID or nothing]
    """
    spark = SparkSession\
        .builder\
        .appName("CIDs")\
        .getOrCreate()

    if len(sys.argv) > 1:
        cids = [sys.argv[1]]
    else:
        cids = ['A000', 'B000'] 

    # count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    for cid in cids: #TODO scale
        print("CID %s" % cid)

    spark.stop()
