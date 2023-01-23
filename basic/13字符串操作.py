"""
演示以数据容器的角色，学习字符串的相关操作
"""
my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是：{value}, 取下标为-16的元素，值是{value2}")

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标是：{value}")
# replace方法
new_my_str = my_str.replace("it", "程序")
print(f"将字符串：{my_str}，进行替换后得到：{new_my_str}")

# 字符串分割 split方法
# 语法：字符串.split(分隔符字符串)
# 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 注意：字符串本身不变，而是得到了一个列表对象
my_str = "itheima and itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}, 类型是：{type(my_str_list)}")

# 字符串的规整操作（去前后空格）
# 语法：字符串.strip()
my_str = "   itheima and itcast  "
print(f"字符串{my_str}被strip后得到：{my_str.strip()}")

# 字符串的规整操作（去前后指定的字符串）
# 语法：字符串.strip（字符串）
my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip('12')后得到：{new_my_str}")

# 统计字符串中某字符串的出现次数
count = new_my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{count}")

# 统计字符串的长度
length = len(new_my_str)
print(f"字符串{my_str}的长度是：{length}")
