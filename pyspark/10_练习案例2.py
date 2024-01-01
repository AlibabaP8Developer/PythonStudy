"""
JSON商品统计
需求：
1 各个城市销售额排名，从大到小
2 全部城市，有哪些商品类别在售卖
3 北京有哪些商品类别在售卖
"""
import json

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# TODO 需求1：城市销售额排名
# 1.1 读取文件得到rdd
file_rdd = sc.textFile('/Users/lizhenghang/workspace/python/PythonStudy/pyspark/orders.txt')

# 1.2 取出一个个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split('|'))
print(json_str_rdd.collect())
# 1.3 将一个个JSON字符串转换为字典 {'a':'v', 'b':'v'}
dict_add = json_str_rdd.map(lambda x: json.loads(x))
print(dict_add.collect())
# 1.4 取出城市和销售额数据
# (城市， 销售额) 计数
city_with_money_rdd = dict_add.map(lambda x: (x['areaName'], int(x['money'])))
print('取出城市和销售额数据：', city_with_money_rdd.collect())
# 1.5 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda x, y: x + y)
print('按城市分组按销售额聚合：', city_result_rdd.collect())
# 1.6 按销售额聚合结果进行排序
result_add = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print('按销售额聚合结果进行排序：', result_add.collect())
print('=======')
# TODO 需求2：全部城市有哪些商品类别在售卖
# 2.1 取出全部商品类别
category_rdd = dict_add.map(lambda x: x['category']).distinct()
# 2.2 对全部商品类别进行去重
print('对全部商品类别进行去重：', category_rdd.collect())
print('=======')
# TODO 需求3：北京有哪些商品类别在售卖
# 3.1 过滤北京的数据
beijing_data_rdd = dict_add.filter(lambda x: x['areaName'] == '北京')
print('北京：过滤北京的数据：', beijing_data_rdd.collect())
# 3.2 取出全部商品类别
result3_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()
print('北京：取出全部商品类别：', result3_rdd.collect())
# 3.3 进行商品类别去重

