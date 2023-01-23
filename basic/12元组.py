"""
元组定义：使用小括号，数据可以是不同的数据类型
"""

# 定义元组 tuple
t1 = ("朱元璋", 1, True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}, 内容：{t1}")
# 定义单个元素的元素
t1 = ("朱元璋",)
print(f"t1的类型是：{type(t1)}, 内容：{t1}")

# 元组的嵌套
t1 = ((1, 2, 3), (4, 5, 6))
print(f"t1的类型是：{type(t1)}, 内容：{t1}")

# 下标索引取出内容
num = t1[1][1]
print(f"num的类型是：{type(num)}, 从嵌套元组中取出的数据是：{num}")

# 元组的操作：index查找方法
t1 = (100, "朱元璋", "朱高炽")
index = t1.index("朱元璋")
print(f"在元组t1中查找朱高炽的下标是：{index}")

# 元组的操作：count统计方法
t1 = ("朱元璋", "朱元璋", "朱高炽")
num = t1.count("朱元璋")
print(f"在元组t1中统计朱元璋的数量是：{num}")

# 元组的操作：len函数统计元素数量
count = len(t1)
print(f"t1元组中的元素数量是: {count}个")

print("============")
# 元组的操作：while
t1 = ("朱元璋", "朱允炆", "朱詹基", "朱高炽")
index = 0
while index < len(t1):
    print(f"for 元组的元素有：{t1[index]}")
    index += 1

print("============")
# 元组的操作：for
for element in t1:
    print(f"for 元组的元素有：{element}")