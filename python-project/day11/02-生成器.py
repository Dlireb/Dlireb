def Yield_item(end):
    count =  1
    while count <= end:
        yield count
        count += 1

res = Yield_item(5)
for item in res:
    print(item)