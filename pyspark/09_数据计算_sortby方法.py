"""
rdd的distinct成员方法的使用
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
print('取出全部单词：', word_rdd.collect())
# 将所有单词都转换成二元元组，单词为key、value设置为1
# (hello, 1) (spark, 1)
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
print('将所有单词都转换成二元元组，单词为key、value设置为1：', word_with_one_rdd.collect())
# 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda x, y: x + y)
# 打印输出结果
print('分组并求和：', result_rdd.collect())

# 对rdd的数据进行排序
"""
rdd.sortBy(func, ascending=False, numPartitions=1)
func:(T)->U:告知按照rdd中的哪个数据进行排序，比如lambda x：x[1] 表示按照rdd中的第二列元素进行排序
ascending： true升序，false降序
numPartitions：用多少分区排序
"""
rdd2 = result_rdd.sortBy(lambda x: x[1], ascending=True, numPartitions=1)
print(rdd2.collect())
