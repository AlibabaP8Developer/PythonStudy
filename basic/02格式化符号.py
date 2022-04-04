"""
%s 字符串
%d 有符号的十进制整数
%f 浮点数
%c 字符
%u 无符号十进制整数
%o 八进制整数
%x 十六进制整数（小写ox）
%X 十六进制整数（大写OX）
%e 科学计数法（小写'e'）
%E 科学计数法（小写'E'）
%g %f和%e的简写
"""

age = 10
name = "朱元璋"
son = "朱标"
weight = 60
stuId = 111222333

# 今年朱元璋的年龄是10岁
print("今年%s的年龄是%d岁" % (name, age))

# 朱元璋的太子名字是朱标
print("朱元璋的太子名字是%s" % son)
print("%s的太子名字是%s" % (name, son))

# 朱元璋的体重是60kg
print("朱元璋的体重是%dkg" % weight)
print("明年朱元璋的体重是%dkg" % (weight + 10))

# 朱元璋的学号是111222333
print("朱元璋的学号是%d" % stuId)

print("%s的太子是%s，%s今年%d岁" % (name, son, son, age))

# f"{表达式}"
print("f{表达式}的方式 ==> " + f"{name}的太子是{son}，{son}今年{age}岁，明年{son}是{age+1}岁了")

