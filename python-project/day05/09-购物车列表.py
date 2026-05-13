# 案例10: products =   [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]，需打印出以下格式：
# 	------  商品列表 ------
# 	0  iphone    6888
# 	1  MacPro    14800
# 	2  小米6     2499
# 	3  Coffee    31
# 	4  Book      60
# 	5  Nike      699
#     根据products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，
#     最终用户输入q退出时，打印购买的商品列表。
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
cart = []
while True:
    goods_id = 0
    print("------  商品列表 ------")
    for x in products:
        print(f"{goods_id}\t{x[0]}\t{x[1]}")
        goods_id += 1
    chooice = input("请输入需要购买物品的编号(按'q'退出):")
    if chooice == 'q':
        print("------  购物车列表 ------")
        for x in cart:
            print(f"{x[0]}\t{x[1]}")
        break
    else:
        cart.append(products[int(chooice)])
        