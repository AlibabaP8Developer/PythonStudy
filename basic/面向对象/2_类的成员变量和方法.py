"""
类中成员方法
def 方法名(self, 形参1, ..., 形参n):
     方法体
"""
class Student:
    name = None
    def say_hi(self):
        print(f"hello, 我是{self.name}")
    def say_hi2(self, msg):
        print(f'大家好，我是{self.name}, {msg}')

stu_1 = Student()
stu_1.name = '太祖爷朱重八'
stu_1.say_hi()

stu_2 = Student()
name = stu_2.name = '成祖爷燕王'
stu_2.say_hi()
