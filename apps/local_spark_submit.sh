#!/usr/bin/env bash

# COVID cids = ['B342', 'B972', 'U049', 'U071'] 

$SPARK_HOME/bin/spark-submit \
 --master spark://wilian-ubuntu:7077 \
 --py-files cids.py \
 cids.py sia_pa_rs B342

