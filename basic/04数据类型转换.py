"""
1 input
2 检测input数据类型str
3 int() 转换数据类型
4 检测是否成功
"""
num = input("请输入数字：")
print(num)

# <class 'str'>
print("检测num类型：%s" % type(num))

# <class 'int'>
print("转换后的num类型：%s" % type(int(num)))

# 1.float -- 将数据转换为浮点型
num1 = 1
str1 = "10"
# 1.0
print(float(num1))
print(float(str1))
# <class 'float'>
print(type(float(num1)))
print(type(float(str1)))
print("=======")

# str() -- 将数据转换为字符串类型
print(str(num1))
print(type(str(num1)))
print("=======")

# tuple() -- 将一个序列转换为元组
list1 = [10, 20, "朱元璋"]
print("list1转换前：", list1)
print("list1转换后：", tuple(list1))
print("list1转换检测类型：", type(tuple(list1)))
print("=======")

# list() -- 将一个序列转换为列表
list2 = (100, "朱标", 300.98)
print("list2转换前：", list2)
print("list2转换后：", list(list2))
print("list2转换检测类型：", type(list(list2)))

# eval() -- 计算在字符串中的有效py表达式，并返回一个对象
str2 = "1"
str3 = "1.1"
str4 = "(900,'朱元璋', 99.99)"
str5 = "[900,'朱元璋', 99.99]"
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
