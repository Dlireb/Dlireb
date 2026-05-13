# 案例3：给一个字符串，统计其中的数字、字母和其他类型字符的个数；
txt = input("输入一个包含数字、字母和其他字符的字符串：")
txt_digit = 0
txt_letter = 0
txt_other = 0
for item in txt:
    if item.isdigit():
        txt_digit+=1
    elif item.isalpha():
        txt_letter+=1
    else:
        txt_other+=1
print(f"字符串中包含数字：{txt_digit},字母{txt_letter},其他字符:{txt_other}")