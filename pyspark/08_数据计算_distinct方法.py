"""
rdd的distinct成员方法的使用
"""
# 构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备rdd
rdd = sc.parallelize([1, 3, 2, 2, 4, 5, 7, 6, 3, 8, 1, 9, 1, 4, 5, 8, 9, 5, 6, 8, 7])
# 对rdd的数据进行去重
rdd2 = rdd.distinct()
print(rdd2.collect())
