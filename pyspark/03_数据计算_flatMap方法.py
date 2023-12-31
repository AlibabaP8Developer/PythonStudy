"""
演示RDD的flatMap成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备rdd
rdd = sc.parallelize(['itheima alibaba', 'xiaomi alibaba', 'xiaomi itheima huawei mate60pro'])

# 需求：将RDD数据里面的一个个单词提取出来
rddMap = rdd.map(lambda x: x.split(' '))
# [['itheima', 'alibaba'], ['xiaomi', 'alibaba'], ['xiaomi', 'itheima', 'huawei', 'mate60pro']]
print(rddMap.collect())

rddMap = rdd.flatMap(lambda line: line.split(' '))
# ['itheima', 'alibaba', 'xiaomi', 'alibaba', 'xiaomi', 'itheima', 'huawei', 'mate60pro']
print(rddMap.collect())

