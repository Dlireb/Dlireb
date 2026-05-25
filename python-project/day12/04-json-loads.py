import json
# JSON格式字符串

# #object_hock
# class student:
#     def __init__(self,name,age,ider):
#         self.name = name
#         self.age = age
#         self.ider = ider

# def dict_to_student(dict_data):
#     return student(dict_data['姓名'],dict_data['年龄'],dict_data['爱好'])  #return返回什么类型就是什么类型

# json_text = '{"姓名":"李四","年龄":22,"爱好":["听歌","跑步"]}'

# student_obj = json.loads(json_text,object_hook=dict_to_student)
# print(student_obj)     # <__main__.student object at 0x7f4c8e25be20>

# print(student_obj.name)#李四

# print(student_obj.age)#22

# print(student_obj.ider)#['听歌', '跑步']


#object_pairs_hock

json_str = '{"name":"小红","age":18,"sex":"女"}'

# 钩子函数：接收有序键值对列表
def handle_pairs(pairs_data):
    print("收到有序数据：", pairs_data)
    # 你可以返回任何类型
    return tuple(pairs_data)
    
    #return返回什么类型就是什么累心
    # 不做修改默认放回列表
    # 强转为dict，返回的就是字典类型

# 使用 object_pairs_hook
result = json.loads(json_str, object_pairs_hook=handle_pairs)

print(result)
print(type(result))