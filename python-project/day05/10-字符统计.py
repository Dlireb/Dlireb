# 案例11: 重复的单词: 此处认为单词之间以空格为分隔符， 并且不包含，和.>；
#     ● 1. 用户输入一句英文句子；
#     ● 2. 打印出每个字母及其重复的次数;“hellojavahellopython”
#         h:3
#         e:2
#         l:4
#         ...
text_str = input('请输入一串英文句子：')
text_set = { x for x in text_str}
text_list = [x for x in text_str]
text_list.sort()
text_dict = {x:0 for x in text_set}
text_set = list(text_set)
text_set.sort()
for x in text_list:
    text_dict[x]+=1
for x in range(len(text_dict)):
    print(f'{text_set[x]}:{text_dict[text_set[x]]}')

