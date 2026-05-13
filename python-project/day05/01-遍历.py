# 案例1: 遍历打印成 ['h','e','l','l','o','c','x','y','-','f','a','m','i','l','y']
item = "hello cxy-family"
new_item = []
for x in item:
    if not x.isspace():
        new_item.append(x)
print(new_item)