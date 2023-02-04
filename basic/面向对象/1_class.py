# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 创建一个对象
stu_1 = Student()

# 对象属性进行赋值
stu_1.name = '武媚娘'
stu_1.gender = '女'
stu_1.age = 10
stu_1.nationality = 'china'
stu_1.native_place = 'beijing'

# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.age)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.gender)
