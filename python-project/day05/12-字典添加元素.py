# 案例13: 现有dict2 = {"k1":"v11","a":"b"},通过一行操作使dict2 = {"k1":"v11","k2":"v2","k3":"v3","a":"b"}
dict2 = {"k1":"v11","a":"b"}
dict2.update({"k2":"v2","k3":"v3"})
print(dict2)
