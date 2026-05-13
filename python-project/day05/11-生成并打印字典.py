# 案例12: 编写一个Python脚本来生成并打印一个字典，字典的形式为(x, x*x)，其中包含一个数字(1到n之间)。
num = int(input())
text_dict = { x : x**2 for x in  range(1,num+1)}
print(text_dict)
