"""
演示类的构造方法
"""

# 构造方法的名称：__init__

class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"student类创建了一个类对象{name}, {age}，{tel}")

stu = Student("朱重八", 11, 18888888888)
print(stu.name)
