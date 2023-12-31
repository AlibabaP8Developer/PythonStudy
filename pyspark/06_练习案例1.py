"""
练习案例：单词计数统计
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
# 将所有单词都转换成二元元组，单词为key、value设置为1
# (hello, 1) (spark, 1)
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
print(word_with_one_rdd.collect())
# 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda x, y: x + y)
# 打印输出结果
print(result_rdd.collect())
