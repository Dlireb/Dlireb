from models.cart import Cart_models
from DAO.product_dao import Product_datas
from DAO.user_dao import User_datas

class Cart_datas:
    def __init__(self):
        self.user_datas = User_datas()
        self.product_datas = Product_datas()

    def get_user_cart(self,user_id):#| user_id | Optional[dict] | 获取用户购物车 |
        user = self.user_datas.get_user_by_id(user_id)
        if user:
            return user.cart
        return None

    def get_cart_items(self,user_id):#| user_id | List[CartItem] | 获取购物车项列表 |
        user_item = self.get_user_cart(user_id)
        if user_item:
            return user_item
        return []

    def add_cart_item(self,user_id,product_id,quantity):#| user_id, product_id, ... | bool | 添加购物车项 |
        product = self.product_datas.get_products_by_id(product_id)#获取商品
        if not product:
            return False
        user_cart = self.get_cart_items(user_id)
        for item in user_cart:
            if item.product_id == product_id:
                item.add_quantity(quantity)
                return True
        cart = Cart_models(user_id=user_id,product_id=product_id,product_name=product.name,price=product.price,quantity=quantity)#创建购物车列表
        user = self.user_datas.get_user_by_id(user_id)
        if user:
            user.cart.append(cart)
            return True
        else:
            return False

    def remove_cart_item(self,user_id,product_id):#| user_id, product_id | bool | 删除购物车项 |
        user_cart = self.get_cart_items(user_id)#返回的是列表
        for item in user_cart:
            if item.product_id == product_id:
                user_cart.remove(item)
                return True
        return False
                
    def update_cart_item_quantity(self,user_id,product_id,quantity):#| user_id, product_id, quantity | bool | 更新数量 |
        user_cart = self.get_cart_items(user_id)#返回的是列表
        for item in user_cart:
            if item.product_id == product_id:
                return item.update(quantity)

    def clear_cart(self,user_id):#| user_id | bool | 清空购物车 |
        user_cart = self.get_cart_items(user_id)#返回的是列表
        user_cart.clear()
        return True

    def get_cart_total_price(self,user_id):#| user_id | float | 获取总金额 |
        user_cart = self.get_cart_items(user_id)
        total_price = 0.0
        for item in user_cart:
            total_price += item.subtotal()
        return total_price

    def get_cart_total_quantity(self,user_id):#| user_id | int | 获取总数量 |
        user_cart = self.get_cart_items(user_id)
        total_quantity = 0.0
        for item in user_cart:
            total_quantity += item.quantity
        return total_quantity
    