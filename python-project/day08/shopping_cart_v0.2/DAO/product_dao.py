from data.data import test_product
from data import data
from models.product import Product_models

class Product_datas:

    def get_all_product(self):#| - | List[Product] | 获取所有商品 |
        return test_product.copy()

    def get_products_by_id(self,product_id):#| product_id | Optional[Product] | 根据 ID 获取商品 |
        for item in self.get_all_product():
            if item.product_id == product_id:
                return item

    def get_product_by_name(self,name):#| name | Optional[Product] | 根据名称获取商品 |
        for item in self.get_all_product():
            if item.name == name:
                return item

    def add_product(self,product):#| product | bool | 添加商品 |
        product.product_id = data.new_product_id
        test_product.append(product)
        data.new_product_id += 1
        return True

    def update_product(self,product_id,**kwargs):#| product_id, **kwargs | bool | 更新商品信息 |
        product_up = self.get_products_by_id(product_id)
        if product_up:
            product_up.update(**kwargs)
            return True
        return False


    def delete_product(self,product_id):#| product_id | bool | 删除商品 |
        product_del = self.get_products_by_id(product_id)
        if product_del:
            test_product.remove(product_del)
            return True
        else :
            return False

    def search_products(self,keyword):#| keyword | List[Product] | 搜索商品 |
        product_list = []
        for item in self.get_all_product():
            if keyword.lower() in item.name.lower():
                product_list.append(item)
        return product_list
