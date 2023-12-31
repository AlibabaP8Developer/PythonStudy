"""
演示RDD的map成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备rdd
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 通过map方法将全部数据都乘以10
# ()->U     (T)->T  (T)->U

# def func(data):
#     return data * 10

# rdd2 = rdd.map(func)
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())
