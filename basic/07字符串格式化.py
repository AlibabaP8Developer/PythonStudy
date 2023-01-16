name = "黑马"
address = "北平城黑马大学"
print(name + "在" + address)
tel = 18888888888
cource = "Python"

# 多个变量占位，变量要用括号括起来，并按占位顺序填入
# %s：将内容转换成字符串，放入占位位置
# %d：将内容转换成整数，放入占位位置
# %f：将内容转换成浮点数，放入占位位置
print(name + "在" + address + "学习%s课程，telephone is %s：" % (cource, tel))

name = "Google"
year = 1998
price = 10000.99
print("%s于%s成立，price is %s万万亿美金" % (name, year, price))

num1 = 11
num2 = 11.692
print('结果是：%5d' % num1)
print('结果是：%1d' % num1)
print('数字11.392 宽度限制7，小数精度2，结果是：%7.2f' % num2)
print('数字11.392 小数精度2，结果是：%.2f' % num2)

