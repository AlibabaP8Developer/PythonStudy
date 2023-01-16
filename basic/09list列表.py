"""
演示数据容器 list列表
语法：[元素, ...]
"""
my_list = ["itheima", "python", 9, 10.0, True, ["atguigu", 10, False], [11, 12]]
print(my_list)
print(type(my_list))
print(my_list[0])

print('=====')

my_list = ["朱元璋", "弘历", "朱五四"]
# 列表[下标索引]，从前向后从0开始，每次加1；从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])

print('=====')

print(my_list[-1])
print(my_list[-2])

print('=====')

my_list = [["朱元璋", "弘历", "朱五四"], ["朱四九", "朱初一", "爱猷识理达腊"]]
print(my_list[1][2])

"""
查找某元素下标
功能：查找指定元素在列表的下标，如果找不到，报错valueError
语法：列表.index(元素)
index就是列表对象（变量）内置的方法（函数）
"""
