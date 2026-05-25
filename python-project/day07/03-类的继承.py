#方法
class Father:
    def play(self):
        print("爸爸在玩手机")

class Son(Father):
    def play(self):
        # 先调用父类的 play
        super().play()
        print("儿子也跟着玩")

s = Son()
s.play()

#属性
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        # 调用父类构造
        super().__init__(name)
        self.age = age

stu = Student("小明", 18)
print(stu.name, stu.age)