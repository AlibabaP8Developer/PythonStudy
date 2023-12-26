"""
演示pyspark的执行环境入库对象：spackContext
并通过sparkContext对象获取当前pyspark的版本
"""

# 导包
from pyspark import SparkContext, SparkConf

# 创建spackConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("text_spark_app")
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印pyspark的运行版本
print(sc.version)

# 停止sparkcontext对象的运行
sc.stop()
