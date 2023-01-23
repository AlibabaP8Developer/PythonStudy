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
