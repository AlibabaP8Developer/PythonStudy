"""
对文件的读取
"""
f = open('/Users/lizhenghang/Desktop/hello.txt', 'r', encoding='UTF-8')
print(type(f))  # <class '_io.TextIOWrapper'>

# 读取文件 read()
# print(f'读取3个字节的结果：{f.read(3)}')  # hel
# print(f'read方法读取全部的结果是：{f.read()}')  # lo,拓跋思恭,朱重八

print('-------------')

# 读取文件 readLines()
# 读取文件的全部行，封装到列表中
lines = f.readlines()
print(f'lines对象的类型：{type(lines)}')
print(f'lines对象的类型：{lines}')

# 读取文件 readLine()
