from DAO.cart_dao import Cart_datas
from service.product_service import Product_service
from DAO.user_dao import User_datas
from common.validator import Validator
class Cart_service:
    def __init__(self):
        self.cart_datas = Cart_datas()
        self.product_service = Product_service()
        self.user_datas = User_datas()

    def view_cart(self,user_id):#| Tuple[bool, List[CartItem]] | 查看购物车 |
        user_cart = self.cart_datas.get_user_cart(user_id)
        if user_cart is None:
            return False,None
        return True,user_cart

    def add_to_cart(self,user_id,product_id,quantity):#| Tuple[bool, str] | 添加到购物车 |
        success,message = self.product_service.get_product_by_id(product_id)
        if not success:
            return False,'未找到商品'
        success,message = Validator.validate_cart_quantity(quantity)
        if success:
            if self.cart_datas.add_cart_item(user_id,product_id,quantity):
                return True,'添加成功'
            else:
                return False,'添加失败'
        else:
            return False,message
        
    def remove_from_cart_quantity(self,user_id,product_id):#| Tuple[bool, str] | 删除购物车项 |
        success = self.cart_datas.remove_cart_item(user_id,product_id)
        if success:
            return True,'删除成功'
        else:
            return False,'删除失败'

    def update_cart_item_quantity(self,user_id,product_id,quantity):#| Tuple[bool, str] | 更新数量 |
        success = self.cart_datas.update_cart_item_quantity(user_id,product_id,quantity)
        if success:
            return True,'更改成功'
        else:
            return False,'更改失败'

    def clear_cart(self,user_id):#| Tuple[bool, str] | 清空购物车 |
        success = self.cart_datas.clear_cart(user_id)
        if success:
            return True,'清空成功'
        else:
            return False,'清空失败'

    def get_cart_total(self,user_id):#| Tuple[float, int] | 获取总计 |
        total_price = self.cart_datas.get_cart_total_price(user_id)
        total_quantity =self.cart_datas.get_cart_total_quantity(user_id)
        return total_price, total_quantity

    def checkout(self,user_id,user_balance):#| Tuple[bool, str] | 结算购物车 |
        #检查余额 → 检查库存 → 扣减库存 → 扣减余额 → 清空购物车
        #检查余额
        user_cart = self.cart_datas.get_cart_items(user_id)#获取购物车
        user_cart_total = self.cart_datas.get_cart_total_price(user_id)#获取购物车的所有物品的总价
        if user_cart_total > user_balance:
            return False,'余额不足,请充值'
        #检查库存
        for item in user_cart:
            success,message = self.product_service.get_product_by_id(item.product_id)#获取商品信息
            if success:
                if message.stock < item.quantity:
                    return False,'库存不足，等待补货'
        #扣减库存
        for item in user_cart:
            success,message = self.product_service.get_product_by_id(item.product_id) #获取商品信息
            message.reduce_stock(item.quantity)#扣除库存
        #扣减余额
        user = self.user_datas.get_user_by_id(user_id)
        user.withdraw(user_cart_total)
        self.user_datas.update_user(user_id,balance = user.balance)
         #清空购物车
        success,message = self.clear_cart(user_id)
        if success:
            return True,message
        else:
            return False,message
        





