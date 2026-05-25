#私有属性的设置，在属性和方法名前添加双下划线前缀
#私有属性只能在定义类时访问和修改

class Person:
    def __init__(self,name='lisi',paw=123456):
        self.name = name
        self.__paw = paw
    def __sayy(self):
        print(f"password:{self.__paw}")
person = Person()
print(person.__dict__)

