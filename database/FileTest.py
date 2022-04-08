# 如果操作文件不存在会创建文件
file_txt = open("test.txt", "w")
name_txt = file_txt.name
print(name_txt)
file_txt.write("hello, py file!")
# 如果操作文件不存在，则会报错
file_txt = open("test.txt", "r")

file_txt.close()
