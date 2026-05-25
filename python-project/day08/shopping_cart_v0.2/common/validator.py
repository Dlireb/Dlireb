class Validator:
    @staticmethod
    def validate_username(name):# | 校验用户名 |
        if ' ' in name:
            return False,'用户名不能包含空格！！！'
        if not name:
            return False,'用户名不得为空！！！'
        if not name[0].isalpha():
            return False,'用户名开头必须为字母！！！'
        for item in name:
            if not (item.isalnum() or item == '_'):
                return False,'用户名只能包含字母，数字和下划线！！！'
        return True,'用户名合规'
    @staticmethod
    def validate_password (password ):# 校验密码 |
        if not password :
            return False,'密码不得为空！！！'
        if password.isspace():
            return False,'密码不能为全空格'
        if len(password) > 12 or len(password) < 6:
            return False,'密码不得少于6-12位'
        return True,'密码合规'
    @staticmethod
    def validate_phone ( phone ):# 校验手机号 |
        if not phone:
            return False,'手机号码不能为空'
        if not phone.startswith('1'):
            return False,'手机号码第一位要为1'
        if len(phone) != 11:
            return False,'手机号码必须为11位'
        if not phone.isdigit():
            return False,'手机号必须为全数字'
        return True,'手机号码合规'
    @staticmethod
    def validate_product_price(price):#校验商品价格 |
        if price >= 0.01 and price < 999999.99:
            return True,'商品金额合规'
        else:
            return False,'商品金额不合规'

    @staticmethod
    def validate_product_stock(stock):# | 校验商品库存 |
        if stock >= 0 and stock < 999999:
            return True,'商品数量合规'
        else:
            return False,'商品数量不合规'

    @staticmethod
    def validate_cart_quantity (quantity) :# 校验购物车数量 |
        if quantity >= 1 and quantity < 9999:
            return True,'数量合规'
        else:
            return False,'数量不合规'

    @staticmethod
    def validate_product_name (name):# | 校验商品名称 |
        if (name is not None) and not name.isspace():
            return True,'商品名称合规'
        else :
            return False,'商品名称不合规'

    @staticmethod
    def validate_amount(amount):#校验金额 |
        if amount <= 0:
            return False,'金额不合规'
        else:
            return True,'金额合规'
