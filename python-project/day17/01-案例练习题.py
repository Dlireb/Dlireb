# 题目 1
# 输入一段英文句子，将句子里所有逗号全部替换为句号，输出处理后的完整内容。
english = input('请输入英文句子')
new_english = ''
for item in english:#非函数实现办法
    if item == ',':
        new_english += '.'
    else:
        new_english += item
print(new_english)
print(english.replace(',','.'))#函数实现
# 题目 2
# 输入一个百分制分数，根据分数划分等级并输出：60 分以下为不及格，60~79 分为及格，80~89 分为良好，90 分及以上为优秀。
try:
    score = int(input('请输入一个分数（百分制）：'))
    if score >= 90 and score <= 100:
        print('优秀')
    elif score >= 80 and score <= 89:
        print('良好')
    elif score >= 60 and score <= 79:
        print('及格') 
    elif score < 60 and score >= 0:
        print('不及格')
    else:
        print("输入错误！")
except ValueError:
    print('请输入数字')
# 题目 3
# 依次输入三个英文单词，将这三个单词用短横线-连接成一整段内容，最后输出拼接后的结果。
new_list_str = []
new_str = ''
for num in range(0,3):
    new_list_str.append(input(f'请输入第{num}单词：'))
new_str = '-'.join(new_list_str)
print(new_str)