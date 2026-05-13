#1、展示商品信息、包括品名、价格
goods = [
    {"id": 1, "name": "苹果", "price": 5},
    {"id": 2, "name": "香蕉", "price": 3},
    {"id": 3, "name": "橙子", "price": 4}
    ]
#2、购物车列表
cart = []
#3、顾客选着界面 1、查看商品，2、添加商品到购物车、3、查看购物车，4、结账、5、退出
while True:
    print("1、查看商品\n2、添加购物车\n3、查看购物车\n4、结账\n5、退出")
    choice=input("请输入选择：")
    match choice:
        case '1':
            for x in goods:
                print(f"品名：{x['name']}\t价格:{x['price']}\n")
        case '2':
            #存储顾客需要购买的物品及数量，并筛选掉非法输入
            while True:
                for x in goods:
                    print(f"编号:{x['id']}\t品名:{x['name']}\t价格:{x['price']}\n")
                #校验输入的编号合法性
                good_id = int(input("请输入商品id:"))
                if not good_id.is_integer():
                    print("非法输入！！，编号为数字请输入数字")
                    continue
                #把goods中的每条商品信息拿出的单独赋值给item，单个item的值为：{"id": 1, "name": "苹果", "price": 5}
                #再通过item["id"]提取出字典中的key为“id”的值
                item_id = [item["id"] for item in goods]
                if good_id not in item_id:
                    print("输入的编号不存在，请重新输入！！！")
                    continue
                #校验输入的数量合法性
                good_num = input("请输入商品数量:")
                print('\n')
                if not good_id.is_integer():
                    print("非法输入！！，编号为数字请输入数字")
                    continue
                good_num = int(good_num)
                if good_num < 0:
                    print("数量不得小于0!!!")
                    continue
                #将商品添加至购物车
                targe_goods = None
                for item in goods:
                    if item['id'] == good_id:
                        targe_goods = item
                cart.append(
                    {
                        'name':targe_goods['name'],
                        'price':targe_goods['price'],
                        'num':good_num,
                        'totel':targe_goods['price'] * good_num
                    }
                )
                #是否继续购物
                choose = input("是否继续购物(y/n):")
                if choose == 'n':
                    break

        case '3':
            if not cart:
                print("购物车空空如也！！！\n")
            else:
                for x in cart:
                    print(f"品名:{x['name']}\t数量:{x['num']}\t价格:{x['totel']}")
        case '4':
            print("你的购物车清单如下：\n")
            for x in cart:
                    print(f"品名:{x['name']}\t数量:{x['num']}\t价格:{x['totel']}")
            totel = 0
            for item in cart:
                totel = totel + item["totel"]
            print(f"你共计消费{totel}!!!")
            break
        case '5':
            break
        case _:
            print("无效输入！！！") 
            continue