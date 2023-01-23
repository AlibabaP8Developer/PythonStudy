"""
查找某元素下标
功能：查找指定元素在列表的下标，如果找不到，报错valueError
语法：列表.index(元素)
index就是列表对象（变量）内置的方法（函数）
"""
#
my_list = ["朱元璋", "弘历", "朱五四", "itheima"]
# 查找某元素在列表内的下标索引
index = my_list.index("itheima")
print(f"itheima在列表中的下标索引值是：{index}")
# 如果被查找元素不存在，会报错，ValueError: 'itheima0' is not in list

# 修改特定下标索引值
# 语法：列表[下标]=值
my_list[0] = '朱允炆'
print(f"列表被修改元素值后，结果是: {my_list}")

# 在指定下标位置插入新元素
# 语法：列表.insert(下标，元素)，在指定的下标位置，插入指定的元素
my_list.insert(1, "完颜亮")
print(f"列表被修改元素值后，结果是: {my_list}")

# 在列表的尾部追加```单个```新元素
# 语法：列表.append(元素),将指定元素，追加到列表的尾部
my_list.append("完颜阿骨打")
print(f"列表在追加了元素后，结果是: {my_list}")

# 在列表的尾部追加```一批```新元素
# 语法：列表.extend(其它数据容器)，将其它数据容器的内容取出，依次追加到列表尾部
my_list2 = ["完颜宗弼", "完颜雍"]
my_list.extend(my_list2)
print(f"列表在追加了一个新的列表后，结果是: {my_list}")

# 删除指定下标索引的元素（2种方式）
# 方式1：del列表[下标]
del my_list[3]
print(f"列表删除元素后，结果是: {my_list}")
# 方式2：列表.pop(下标)
element = my_list.pop(3)
print(f"通过pop方法取出元素后列表内容是: {my_list}，取出的元素是：{element}")
# 删除某元素在列表中的第一个匹配项
# 语法：列表.remove(元素)
my_list.remove("朱允炆")
print(f"通过remove方法移除元素后，列表的结果是: {my_list}")

# 清空列表
# 列表.clear()
my_list.clear()
print(f"列表被清空了，结果是: {my_list}")

# 统计列表内某元素的数量
# 语法：列表.count(元素)
my_list = ['弘历', '弘历', '完颜宗弼', '完颜宗弼', '完颜雍']
print(f"列表中弘历的数量是: {my_list.count('弘历')}个")

# 统计列表中全部的元素数量
# 语法：len(列表)
count = len(my_list)
print(f"列表中的元素数量是: {count}个")
