# class Persend:
#     name = 'zhangshang'
#     age = 18
#     gender = '男'
#     def eat():
#         print('我会吃饭')
#     def drink(self):
#         print('我会喝水')


# persend = Persend()
# print(persend.name)
# print(persend.age)
# print(persend.gender)
# persend.drink()#通过对象调用对象方法
# # persend.eat()
# Persend.eat()#通过类直接调用类方法

#对实例化对象后属性的修改、增加和删除
# Persend.name = 'lisi' #修改
# Persend.hight = 180   #增加
# del Persend.gender    #删除

#对实例化对象后方法（函数）的添加和修改
# def drink(self):
#     print("我要喝饮料")

# #需要导入库来将新定义的方法和对象绑定起来
# from types import MethodType
# persend.drink = MethodType(drink,persend)#修改
# persend.drink()
# persend1 = Persend()
# persend1.drink()

# def say(self):
#     print('我会说话')
# persend.say = MethodType(say,persend)#增加
# persend.say()

# del persend.say#删除
# persend.say()

#构造函数
# class Person:
#     def __init__(self,name='yiyi',age=0):
#         self.name = name
#         self.age = age
#         print('我被调用了')
#     def say(self):
#         print(f"我是{self.name},今年{self.age}岁")
#         pass

# person = Person('zhansan',18)
# person1 = Person('lisi',20)
# person2 = Person()
# print(person.name,person.age)
# print(person1.name,person1.age)
# print(person2.name,person2.age)
# person.say()
# person1.say()
# person2.say()

# #析构函数
# class Person:
#     def __init__(self,name='yiyi',age=0):
#         self.name = name
#         self.age = age
#         print('我是构造函数！')
#     def __del__(self):
#         print('我是析构函数！')
# Person = Person('x',0)

#类属性
class Circle:
    pi = 3.1415926
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"圆的面积是{Circle.pi*self.radius*self.radius}")
    
cir1 = Circle(1)
cir2 = Circle(2)
cir1.area()
cir2.area()

#实例属性：属于对象的属性，和self参数绑定，且多在构造函数中定义
#__dict__：查看对象的属性，但只能能查看和self绑定的属性，返回值为字典类型。用法 对象名/类名.__dict__

#实例方法

#静态方法：通过@staremethod定义

#类方法：通过@classmethod定义，用来访问和修改类属性，无法访问实例属性



