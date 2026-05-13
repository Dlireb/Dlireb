# 案例4：将str所指字符串的正序和反序进行连接
str_1 = "hello cxy-family"
new_str = reversed(str_1)
str_2 = ""
for item in new_str:
    str_2+=item
print(str_1+str_2)