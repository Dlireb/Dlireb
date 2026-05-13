# 案例14: 编写一个Python脚本合并两个Python字典
#     编写一个Python脚本来打印一个字典，其中键是1到15之间的数字(都包括在内)，值是键的平方。
initil_dict = {x :x**2 for x in range(1,16)}
for x in range(1,16):
    print(f"{x}:{initil_dict[x]}")