# date = [1,2,3,4,5,6,7,8,9]
# new_date = []
# group_size = 3
# for a in range(0,len(date),group_size):
#     a = date[a:a+group_size]
#     new_date.append(tuple(a))
# print(new_date)


# items = [('apple',2.5),('banana',1.8),('orange',3.0),('grape',2.8)]
# for i in range(len(items)):
#     for j in range(len(items)-i-1):
#         if items[j][1] > items[j+1][1] :
#             items[j] , items[j+1] = items[j+1],items[j]
# print(items)


# list1 = [1,2,3,4,5,5]
# list2 = [4,5,6,7,8,5]
# print(set(list1).intersection(set(list2)))


# group_a = ['apple','banana','orange','grape']
# group_b = ['banana','grape','watermelon']
# group_c = ['orange','peach']
# #1、找出只在group_a中出现的水果
# set_a = set(group_a)
# set_b = set(group_b)
# set_c = set(group_c)
# #b和a的交集
# new_set_b_C = set_b.intersection(set_c)
# #b和a的交集
# new_set_b_a = set_b.intersection(set_a)
# #c和a的交集
# new_set_c_a = set_c.intersection(set_a)
# for x in new_set_b_a:
#     set_a.discard(x)
# for x in new_set_c_a:
#     set_a.discard(x)
# print(f"只在group_a中出现的水果:{set_a}")
# #2、找出同时在group_a和group_b中出现，但不在group_c中出现的水果
# tilte2 = {x for x in new_set_b_a  for y in set_c if x != y }
# print(f"同时在group_a和group_b中出现,但不在group_c中出现的水果:{tilte2}")
# #3、找出所有只在一个组中出现的水果（A独有或B独有或C独有）
# set_a = set(group_a)
# tilte3 = new_set_c_a.union(new_set_b_a.union(new_set_b_C))

# print(f"a中只有:{set_a.difference(tilte3)}\nb中只有:{set_b.difference(tilte3)}\nc中只有:{set_c.difference(tilte3)}")

# str_1 = input("请输入一段英文文本：")
# str_1 = str_1.lower()
# str2 = ""
# str3 = []
# dict_1 = {}
# for x in str_1:
#     if x>='a' and x <= 'z':
#         str2+=x
#     else:
#         str3.append(str2)
#         dict_1[str2] = 0
#         str2 = ''
# for x in str3:
#     dict_1[x] = str3.count(x)
# print(dict_1)

original_dict = {'a':1,'b':2,'c':1,'d':3,'e':2}
new_dict = {}
values_new = original_dict.values()
Keys_new = list(original_dict.keys())
a = 0
for x in values_new:
    if x in new_dict:
        new_dict[x]+=Keys_new[a]
    else:
        new_dict.setdefault(x,Keys_new[a])
    a+=1
print(new_dict)
