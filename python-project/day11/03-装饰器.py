# def func1(func):
#     def func2():
#         print('c')
#         func()
#     print('b')
#     return func2

# @func1
# def func():
#     print('a')

# func()

#装饰只带一个参数的函数
# def func1(func):
#     def func2(x):
#         print(x+1)
#         func(x)
#         print(x+2)
#     return func2

# @func1
# def func(x):
#     print(x)

# func(1)

# #装饰未知数量参数的函数
# def fun1(func):
#     def fun2(*args,**kwargs):
#         return func(*args,**kwargs)
#     return fun2

# @fun1
# def func(x,y):
#     print(x+y)

# func(1,2)

# #带参数的装饰器
# def func1(func_iter_item):   #func_iter_item = How are you?
#     def func2(func_name):    #func_name = func
#         def func3(*args,**kwargs):  #args = apple
#             res = func_name(*args,**kwargs)   #等同于   res = func('apple')
#             print(f'{res}{func_iter_item}')   #等同于  print（'Hello, apple How are you?'）
#         return func3
#     return func2

# @func1('How are you?')
# def func(func_item):
#     return f"Hello, {func_item} "

# func('apple')

# #装饰器嵌套
# def func_one(func_one_str):                 #func保存被装饰函数的内存地址
#     def func_one_1(func):                
#         def func_one_2(*args,**kwargs):
#             print(func_one_str)
#             func(*args,**kwargs)        #进入func_two装饰器中并把apple一起传过去
#             print(func_one_str)
#         return func_one_2
#     return func_one_1

# def func_two(func_two_str):
#     def func_two_1(func):
#         def func_two_2(*args,**kwargs):
#             print(func_two_str)
#             func(*args,**kwargs)        #进入func装饰器中并把apple一起传过去
#             print(func_two_str)
#         return func_two_2
#     return func_two_1

# @func_one('Me is one')
# @func_two('Me is two')
# def func(name):
#     print(name)

# func('apple')

class ParamDecorator:
    # 第一层：接收装饰器参数
    def __init__(self, tip_msg):
        self.tip = tip_msg

    # 第二层：接收被装饰函数
    def __call__(self, func):
        def inner(*args, **kwargs):
            print(f"装饰器参数：{self.tip}")
            print("前置操作")
            res = func(*args, **kwargs)
            print("后置操作")
            return res
        return inner

# 传参使用
@ParamDecorator("我是类装饰器传入的参数")
def test_func(a, b):
    print(f"原函数运算：{a}+{b}")
    return a + b

print(test_func(10,20))
