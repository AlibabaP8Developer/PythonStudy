"""

"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 读取文件转换rdd
file_rdd = sc.textFile('/Users/lizhenghang/workspace/python/PythonStudy/pyspark/search_log.txt')

# TODO 需求1：热门搜索时间段Top3（小时精度）
# 1.1 取出全部的时间并转换为小时

# 1.2 转换为（小时，1）的二元元组

# 1.3 key分组聚合value

# 1.4 排序（降序）

# 1.5 取前3

# TODO 需求2：热门搜索词Top3
# 2.1 取出全部的搜索词

# 2.2 （词，1）二元元组

# 2.3 分组聚合

# 2.4 排序

# 2.5 Top3

# TODO 需求3：统计黑马程序员关键字在什么时段被搜索的最多
# 3.1 过滤内容，只保留黑马程序员关键词

# 3.2 转换为（小时，1）的二元元组

# 3.3 key分组聚合value

# 3.4 排序（降序）

# 3.5 取前1

# TODO 需求4：将数据转换为JSON格式，写出到文件中
# 4.1 转换为JSON格式的RDD


