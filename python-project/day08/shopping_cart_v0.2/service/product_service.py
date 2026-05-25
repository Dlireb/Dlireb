from DAO.product_dao import Product_datas
from models.product import Product_models
from common.validator import Validator
class Product_service:
    def __init__(self):
        self.product_datas = Product_datas()
        self.validator = Validator()

    def get_product_list(self):#| List[Product] | 获取商品列表 |
        return self.product_datas.get_all_product()
        

    def get_product_by_id(self,product_id):#| Tuple[bool, Product] | 根据 ID 获取商品 |
        item = self.product_datas.get_products_by_id(product_id)
        if item:
            return True, item
        return False, None

    def add_product(self,name,price,stock):#| Tuple[bool, str] | 添加商品 |
        if not Validator.validate_product_name(name):
            return False,'商品名不合规'
        if not Validator.validate_product_price(price):
            return False,'商品价格不合规'
        if not Validator.validate_product_stock(stock):
            return False,'商品数量不合规'
        new_product = Product_models(name,price,stock)
        if self.product_datas.add_product(new_product):
            return True,'添加成功'

    def delete_product(self,product_id):#| Tuple[bool, str] | 删除商品 |
        if self.product_datas.delete_product(product_id):
            return True,'删除成功'
        else:
            return False,'删除失败'

    def update_product(self,product_id,name,price,stock):#| Tuple[bool, str] | 更新商品信息 |
        
        if name:
            success,message = Validator.validate_product_name(name)
            if not success:
                return False,message

        if price is not None:
            success,message = Validator.validate_product_price(price)
            if not success:
                return False,message

        if stock is not None:
            success,message = Validator.validate_product_stock(stock)
            if not success:
                return False,message
        update_product_dict = {}
        update_product_dict['name'] = name
        update_product_dict['price'] = price
        update_product_dict['stock'] = stock
        success_product= self.product_datas.update_product(product_id,**update_product_dict)
        if success_product:
            return True,'更新成功'
        else:
            return False,'无此商品'

    def search_products(self,keyword):#| List[Product] | 搜索商品 |
        return self.product_datas.search_products(keyword)
    