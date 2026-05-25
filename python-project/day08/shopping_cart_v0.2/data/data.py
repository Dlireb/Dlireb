from models.user import User_models
from models.product import Product_models

test_user_name = [] #存储用户列表 （用product_d，user映像）
test_product= []    #存储商品列表 （product_id，product映像）
new_user_id = 100000
new_product_id = 1

def Data():
    global new_user_id,new_product_id
    admin_user = User_models(user_id = new_user_id,name='admin',password = 'admin123',phone='13570070000')
    test_user_name.append(admin_user)
    new_user_id += 1
    test_products = [
        Product_models(name="华为Mate60", price=5999.99, stock=100, product_id=new_product_id),
        Product_models(name="iPhone15", price=6999.99, stock=80, product_id=new_product_id+1),
        Product_models(name="小米14", price=3999.99, stock=200, product_id=new_product_id+2)
    ]
    test_product.extend(test_products)
    new_product_id += 3


