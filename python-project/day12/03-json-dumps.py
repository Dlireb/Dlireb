import json

# data = {"姓名": "张三",
#     "年龄": 20,
#     "爱好": ["打球", "编程"],
#     (1,2):'D tuple'
#     }

# #python数据转换成json字符串
# str1 = json.dumps(data)
# print(str1)
# #运行结果：{"\u59d3\u540d": "\u5f20\u4e09", "\u5e74\u9f84": 20, "\u7231\u597d": ["\u6253\u7403", "\u7f16\u7a0b"]}
# #因为ensure_ascii默认使用ascii所以中文无法显示，指定为False，使用unicode编码可显示为中文


# str1 = json.dumps(data,ensure_ascii=False)
# print(str1)
# #运行结果：{"姓名": "张三", "年龄": 20, "爱好": ["打球", "编程"]}


# data=[{'a':'A','x':(2,4),'c':3.0}]
# print(json.dumps(data,sort_keys=True))
# #运行结果：[{"a": "A", "c": 3.0, "x": [2, 4]}]
# #sort_keys为True时把数据按照字典键值按升序输出。False为降序


# str1 = json.dumps(data,ensure_ascii=False,indent=4)
# print(str1)
# # 运行结果：
# # {
# #     "姓名": "张三",
# #     "年龄": 20,
# #     "爱好": [
# #         "打球",
# #         "编程"
# #     ]
# # }
# #indent指定缩进位数，格式化数据


# str1 = json.dumps(data,ensure_ascii=False,separators=(',',':'))
# print(str1)
# # 运行结果：{"姓名":"张三","年龄":20,"爱好":["打球","编程"]}
# # separators为python数据转json字符串压缩空间，去掉指定的符号。且只接受两个参数，（元素分割符，键值分隔符）


# str1 = json.dumps(data,ensure_ascii=False,skipkeys=True)
# print(str1)
# # 运行结果：{"姓名": "张三", "年龄": 20, "爱好": ["打球", "编程"]}
# # 在encoding编码过程中，处理的字典的键（key）值不是json规定的字符串类型就会报错
# # 如果是其他类型，就会抛出ValueError异常，设置了skipkeys就会跳过这些异常的key值
# # skipkeys默认值为False，设置True则跳过异常

# #方法1使用default
# #在类内部定义一个obj_json 方法将对象的属性转换成dict，然后再被序列化为json。
# class Employee(object):
#     def __init__(self, name, age, sex, tel):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.tel = tel

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     # 将序列化函数定义到类中
#     def obj_json(self, obj_instance): #obj_instance = emp
#         return {
#             'name': obj_instance.name,#相当于emp.name
#             'age': obj_instance.age,  #相当于emp.age
#             'sex': obj_instance.sex,  #相当于emp.sex
#             'tel': obj_instance.tel   #相当于emp.tel
#         }

# if __name__ == '__main__':
#     emp = Employee('kongsh', 28, 'female', 13123456789)
#     print(json.dumps(emp, default=emp.obj_json))#意思是把emp对象对应obj_json的形参

# #方法2
# #通过类的__dict__属性实现
# class Employee(object):
#     def __init__(self, name, age, sex, tel):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.tel = tel

# if __name__ == '__main__':
#     emp = Employee('kongsh', 18, 'female', 13123456789)
#     print(emp.__dict__,type(emp.__dict__))
#     print(json.dumps(emp, default=lambda Employee: Employee.__dict__))
#     print(json.dumps(emp, default=lambda emp: emp.__dict__))