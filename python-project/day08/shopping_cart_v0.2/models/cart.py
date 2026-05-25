class Cart_models:
    def __init__(self,user_id,product_id,product_name,price,quantity):
        self.user_id = user_id#| int | 用户 ID |
        self.product_id = product_id#| int | 商品 ID |
        self.product_name =product_name#| str | 商品名称 |
        self.price = price#| float | 商品价格 |
        self.quantity = quantity#| int | 购买数量 |
        
    def subtotal(self):
        sum = self.price*self.quantity#| float | 小计金额 (只读) |
        return sum

    def update(self,quantity):# | 更新数量 |
        if quantity >= 0:
            self.quantity = quantity
            return True
        return False

    def add_quantity(self,quantity):#| 增加数量 |
        if quantity > 0:
            self.quantity += quantity
            return True
        return False

    def update_quantity(self,price):#| 更新价格 |
        if price >= 0.01:
            self.price = price
            return True
        return False