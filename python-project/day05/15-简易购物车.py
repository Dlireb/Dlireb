# 案例16:综合案例:
#     ● 要求用户输入总资产，例如：2000
#     ● 显示商品列表，让用户根据序号选择商品，加入购物车
#     ● 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
#     ● 附加：可充值、某商品移除购物车
goods = [{'id':1,'name':'电饭锅','price':199},
        {'id':2,'name':'洗碗机','price':399},
        {'id':3,'name':'洗衣机','price':499},
        {'id':4,'name':'冰箱','price':1699},
        {'id':5,'name':'电磁炉','price':159}
        ]
cart = []
num = 0
title = ''
amount = int(input("请输入总资产(只允许输入数字):"))
while True:
    #展示商品信息
    print('------商品信息------')
    for item in goods:
        print(f"{item['id']}\t{item['name']}\t{item['price']}")
    chooice = input('请输入购买物品的序号：')
    chooice_num = int(input('请输入购买物品的数量：'))
    target = {
        'name': '',
        'price': 0,
    }
    #查找商品
    for item in goods:
        if item['id'] == chooice:
            target.update({'name':item['name'],'price':item['price']})
            break
    #添加购物车    
    cart.append({
        'name': target['name'],
        'price': target['price'],
        'num': chooice_num,
        'amount': target['price'] * chooice_num,
    })

for x in range(0,len(cart)):
    num += cart[x][amount]
if num < amount:
    print('------商品信息------')
    for item in cart:
        print(f"{item['name']}\t{item['num']}\t{item['amount']}")
    print(f"共计{num}元,余额为{amount}")