"""
演示通过pyspark代码加载数据，即数据输入
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')

sc = SparkContext()

# 通过parallelize方法将Python对象加载到spark内，成为rdd对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("甲乙丙丁戊己庚辛壬癸")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})

# 如果要查看rdd里面有什么内容，需要用collect()方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())  # ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
print(rdd4.collect())
print(rdd5.collect())  # ['key1', 'key2', 'key3']

sc.stop()

# 用过textFile方法，读取文件数据加载到spark内，成为rdd对象

