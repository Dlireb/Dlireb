class Product_models:
    def __init__(self,name,price,stock,product_id=None):
        self.product_id = product_id#| 商品 ID |
        self.name = name#| 商品名称 |
        self.price = price#| 商品价格 |
        self.stock = stock#| 商品库存 |

    def is_in_stock(self,quantity):#| 检查库存是否充足 |
        if self.stock < quantity:
            return False
        else:
            self.stock -= quantity
            return True

    def add_stock(self,quantity):#| 增加库存 |
        if quantity > 0:
            self.stock += quantity
            return True
        else :
            return False

    def reduce_stock(self,quantity):#| 减少库存 |
        if quantity > 0:
            self.stock -= quantity
            return True
        else :
            return False

    def update(self,name,price,stock):#| 更新商品信息 |
        if not name:
            return False
        elif price < 0.01:
            return False
        elif stock < 0:
            return False
        else:
            self.name = name
            self.price = price
            self.stock = stock
            return True