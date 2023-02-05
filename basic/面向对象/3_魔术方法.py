"""
演示类的魔术方法
"""


# 构造方法的名称：__str__

class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 魔术方法
    def __str__(self):
        return f'student类对象，name：{self.name}, age: {self.age}'

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("朱重八", 11)
stu2 = Student("朱高炽", 11)
print(stu1 == stu2)
print(stu1 < stu2)
