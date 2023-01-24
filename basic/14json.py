"""
json是一种轻量级的数据交互格式。可以按照json指定的格式去组织和封装数据

Python数据和JSON数据的相互转化
"""
# 导入JSON模块
import json

# 准备列表，列表内每一个元素都是字典，将其转化为json
data = [{"name": "朱元璋", "age": "11"}, {"name": "朱高炽", "age": "20"}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)
# 准备字典，字典转化为json
data = {"name": "朱元璋", "age": "11", "address": "应天府"}
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# json字符串转换为Python数据类型 [{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "朱元璋", "age": "11"}, {"name": "朱高炽", "age": "20"}]'
data = json.loads(s)
print(type(data))
print(data)

# json字符串转换为Python数据类型{k:v, k:v}
s = '{"name": "朱元璋", "age": "11", "address": "应天府"}'
data = json.dumps(data)
data = json.loads(s)
print(type(data))
print(data)
