"""
将RDD输出为Python对象
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备rdd
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7])

# collect算子，输出rdd为list对象
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子，对rdd进行两辆聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)  # 28

# take算子，取出rdd前n个元素，组成list返回
take_list = rdd.take(3)
print(take_list)  # [1, 2, 3]

# count，统计rdd内有多少条数据，返回值为数字
count_num = rdd.count()
print(f'rdd内有{count_num}个元素')

sc.stop()
