# 案例6：综合案例：
#     设计一个程序，帮助小学生练习10以内的加法
#     详情:
#     ● 随机生成加法题目;
#     ● 学生查看题目并输入答案;
#     ● 判别学生答题是否正确?
#     ● 退出时, 统计学生答题总数,正确数量及正确率(保留两位小数点)
import random
count = 0
accuracy = 0
num = 1
print("如退出请输入'q'")
while True:
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = input(f"题目{num}:{a}+{b}=")
    if c == 'q' :
        break 
    elif int(c) == a+b:
        count += 1
    accuracy = count / num
    num+=1      
print(f"共{num-1}题，答对{count}题,正确率：{accuracy:.2%}")