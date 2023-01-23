"""
演示对list列表的循环，使用while和for循环2种方式
"""

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ['朱初一', '朱重八', '完颜宗弼', '完颜亮', '完颜雍']
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量<列表的元素数量

    # 定义一个变量用来标记列表的下标
    index = 0  # 初始值0
    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"while 列表的元素：{element}")
        index += 1

    print("===========")

    for element in my_list:
        print(f"for 列表的元素：{element}")

list_while_func()
