"""
将RDD输出到文件中
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备rdd
rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6, 7])

rdd2 = sc.parallelize([('hello', 3), ('spark', 4), ('hadoop', 6)])

rdd3 = sc.parallelize([[11, 22, 33], [333, 666, 888], [2, 3, 4]])

# 输出到文件中
rdd1.saveAsTextFile('/Users/lizhenghang/workspace/python/PythonStudy/output1')
rdd2.saveAsTextFile('/Users/lizhenghang/workspace/python/PythonStudy/output2')
rdd3.saveAsTextFile('/Users/lizhenghang/workspace/python/PythonStudy/output3')
