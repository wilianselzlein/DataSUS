#!/usr/bin/env bash

$SPARK_HOME/bin/spark-submit \
 --master spark://wilian-ubuntu:7077 \
 --py-files cids.py \
 cids.py

