"""
演示RDD的map成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备rdd
rdd = sc.parallelize([('男', 1), ('男', 2), ('女', 3), ('女', 4)])
# 求男女两个组数字之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b).collect()

print(rdd2)
