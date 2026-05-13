# 案例17: 用户兴趣标签分析（集合 + 字典）
# # 用户兴趣标签数据（字典的键为用户名，值为兴趣集合）
# user_interests = {
#     "Alice": {"电影", "音乐", "旅行"},
#     "Bob": {"体育", "游戏", "音乐"},
#     "Charlie": {"电影", "摄影", "旅行"},
#     "David": {"游戏", "科技", "体育"}
# }
# # 1. 统计所有兴趣标签的出现次数
# # 2. 找到最热门的兴趣
# # 3. 找到兴趣最相似的两个用户（交集最大）
import copy
user_interests = {
    "Alice": {"电影", "音乐", "旅行"},
    "Bob": {"体育", "游戏", "音乐"},
    "Charlie": {"电影", "摄影", "旅行"},
    "David": {"游戏", "科技", "体育"}
}
# 1. 统计所有兴趣标签的出现次数
new_value = list(user_interests.values())#筛选出每个用户的兴趣集合
new_list = []
new_tuple = set()
for item in new_value:
    new_list.append(list(item))
    new_tuple.update(item)
new_dict = {x:0 for x in new_tuple}
for x in new_list:
    for y in x:
        new_dict[y] += 1
print(new_dict)
# 2. 找到最热门的兴趣
hot_interests = []
hot_value = list(new_dict.values())
hot_keys = list(new_dict.keys())
hot_num = 0
for item in hot_value:
    if item > hot_num:
        hot_num = item
for item in hot_keys:
    if new_dict[item] == hot_num:
        hot_interests.append(item)
print(f'最热门的兴趣：{hot_interests}')
# 3. 找到兴趣最相似的两个用户（交集最大）
max_user_intersts = {}
new_key = list(user_interests.keys())
for x in range(0,len(user_interests)):
    for y in range(x+1,len(user_interests)):
        max_user_intersts.update({new_key[x]+'和'+new_key[y]:user_interests[new_key[x]].intersection(user_interests[new_key[y]])})
copy_max_user_intersts = copy.deepcopy(max_user_intersts)
max_user_key = list(max_user_intersts.keys())
for item in range(0,len(max_user_intersts)):
    if len(copy_max_user_intersts[max_user_key[item]]) != hot_num:
        del copy_max_user_intersts[max_user_key[item]]
user_key = list(copy_max_user_intersts.keys())
user_value = list(copy_max_user_intersts.values())
for x in range(len(copy_max_user_intersts)):
    print(f'{user_key[x]}兴趣最相似，他们都喜欢{user_value[x]}')