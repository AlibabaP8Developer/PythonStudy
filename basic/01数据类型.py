"""
1 按经验将不同的变量存储不同的类型数据
2 验证数据到底是什么类型 -- 检测数据类型 -- type(待检测数据)
"""

num1 = 1
num2 = 1.1
num3 = True
num4 = "hello, github"
num5 = [10, 20, 30]
num6 = {10, 20, 30}
num7 = (10, 20, 30)
num8 = {"name": "大明太祖爷朱元璋", "address": "金陵应天府"}

# <class 'int'>
print(type(num1))

# <class 'float'>
print(type(num2))

# <class 'bool'>
print(type(num3))

# <class 'str'>
print(type(num4))

# <class 'list'> 列表
print(type(num5))

# <class 'set'>
print(type(num6))

# <class 'tuple'> 元组
print(type(num7))

# <class 'dict'> 字典 键值对，JSON格式，相当于Java中的Map
print(type(num8))
