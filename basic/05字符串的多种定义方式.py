"""
演示字符串的三种定义方式
单引号定义法
双引号
三引号
"""
name = '单引号'
print(type(name))
name = "黑马"
print(type(name))
name = """
        黑马大学
       """
print(type(name))

# 使用转义字符 \ 解除引号
name = '传智播客\"黑马\"'
print(name)
name = '传智播客"黑马"'
print(name)
