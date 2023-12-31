"""
rdd的filter成员方法的使用
"""
# 构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 读取数据文件
rdd = sc.textFile('/Users/lizhenghang/workspace/python/PythonStudy/pyspark/text_file.txt')

# 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(' '))
print(word_rdd.collect())

# 对rdd数据进行过滤
word_rdd = word_rdd.filter(lambda x: x == 'itheima')
print(word_rdd.collect())

rdd2 = sc.parallelize([1,2,3,4,5,6])
rdd3 = rdd2.filter(lambda num: num % 2 == 0)
print(rdd3.collect())
