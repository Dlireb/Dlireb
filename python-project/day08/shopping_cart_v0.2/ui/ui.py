import getpass
from service.cart_service import Cart_service
from service.product_service import Product_service
from service.user_service import User_service
from common.validator import Validator
from data import data

class UserInterface:
    def __init__(self):
        self.cart_service = Cart_service()
        self.product_service = Product_service()
        self.user_service = User_service()
        self.validator = Validator()

    def print_menu(self):#打印功能菜单即进入对应功能
            print("-----------功能菜单-----------")
            if not self.user_service.current_user:
                print(f'当前用户: {None}\tID:{None}')
            else:
                print(f'当前用户: {self.user_service.current_user.name}\tID:{self.user_service.current_user_id}')
            print("[1]\t\t登录")
            print("[2]\t\t注册")
            print("[3]\t\t注销")
            print("[4]\t\t查询余额")
            print("[5]\t\t充值")
            print("[6]\t\t查看商品列表")
            print("[7]\t\t添加商品")
            print("[8]\t\t删除商品")
            print("[9]\t\t更新商品信息")
            print("[10]\t\t添加到购物车")
            print("[11]\t\t删除购物车")
            print("[12]\t\t更新购物车数量")
            print("[13]\t\t查看购物车")
            print("[14]\t\t结算购物车")
            print("[15]\t\t清空购物车")
            print("[0]\t\t退出")

    def _do_login(self): #| 登录功能 |
        print('\n-----用户登录-----')
        user_name = input("请输入用户名：")
        password = getpass.getpass("请输入密码：")
        success, message = self.user_service.login(user_name,password)
        if success:
            print(message)
        else :
            print(message)
                
    def _do_register(self): #| 注册功能 |
        while True:
            print('\n-----用户注册-----')
            user_name = input("请输入用户名：")
            password = input("请输入密码(6-1):")
            phone = input('请输入手机号：')
            success, message = self.user_service.register(user_name,password,phone)
            if success:
                print(message)
                break
            else:
                print(message)
                continue

    def _do_logout(self): #| 注销功能 |
        success ,message =  self.user_service.logout()
        if success:
            print(message)
        else:
            print(message)

    def _do_query_balance(self):#| 查询余额 |
        success , message = self.user_service.query_balance()
        if success:
            print(f'当前用户  {self.user_service.current_user.name}\t{message}\t')
        else:
            print(message)

    def _do_recharge(self): #| 充值 |
        while True:
            try:
                recharge = int(input("请输入充值金额："))
            except ValueError:
                print('输入的金额不为数字')
                continue
            success,message = self.user_service.recharge(recharge)
            if success:
                print(message)
                break

    def _do_view_products(self): #| 查看商品列表 |
        all_product = self.product_service.get_product_list()
        print('-------------------商品信息-----------------')
        for item in all_product:
            print(f'{item.product_id:<4d}{item.name:<20s}{item.price:<12.2f}{item.stock:<10d}')
        print('\n')

    def _do_add_product(self): #| 添加商品 |
        while True:
            product_name = input('请输入商品名称:')
            try:
                product_price = float(input('请输入商品价格：'))
                product_stock = int(input('请输入商品数量：'))
            except ValueError:
                print('输入的价格和数量不为数字')
                continue
            success,message = self.product_service.add_product(product_name,product_price,product_stock)
            if success:
                print(message)
                break
            else:
                print(message)
                continue

    def _do_delete_product(self): #| 删除商品 |
        print("\n----- 删除商品 -----")
        try:
            product_id = int(input('请输入商品ID:'))
        except ValueError:
            print('输入错误，请输入数字')
        success ,message =self.product_service.delete_product(product_id)
        if success:
            print(message)
        else:
            print(message)

    def _do_update_product(self): #| 更新商品信息 |
        while True:
            print("\n----- 更新商品 -----")      
            try:
                product_id = int(input('商品ID:'))
                product_name = input('请输入商品名称:')
                product_price = float(input('请输入商品价格：'))
                product_stock = int(input('请输入商品数量：'))
            except ValueError:
                print('输入的ID、价格和数量不为数字')
                continue
            success, message = self.product_service.update_product(product_id,product_name,product_price,product_stock)
            if success:
                print(message)
                break
            else:
                print(message)
                continue

    def _do_add_to_cart(self):#| 添加到购物车 |
        while True:
            if not self.user_service.current_user:
                print('未登录，无法添加')
                break
            print('-----------添加购物车-------------')
            self._do_view_products()
            try:
                cart_product_id = int(input('请输入商品ID:'))
                cart_product_quantity = int(input('请输入商品数量:'))
            except ValueError:
                print('输入的商品ID及数量要为数字')
                continue
            success ,message = self.cart_service.add_to_cart(self.user_service.current_user_id,cart_product_id,cart_product_quantity)
            if success:
                print(message)
                break
            else:
                print(message)
                continue

    def _do_remove_from_cart(self): #| 删除购物车项 |
        if not self.user_service.current_user:
            return None
        print('-----------删除购物车商品-------------')
        self._do_view_cart()
        print('\n')
        try:
            product_id = int(input('请输入商品ID:'))
        except ValueError:
            print('输入的商品ID要为数字')
        success, message = self.cart_service.remove_from_cart_quantity(self.user_service.current_user_id,product_id)
        if success:
            print(message)
        else :
            print(message)  

    def _do_update_cart_quantity(self): #| 更新购物车数量 |
        while True:
            if not self.user_service.current_user:
                print('未登录，无法更改')
                break
            print('-----------更改购物车商品数量-------------')
            try:
                product_id = int(input('请输入商品ID:'))
                product_quantity = int(input('请输入商品数量:'))
            except ValueError:
                print('输入的商品ID及数量要为数字')
                continue
            success,message = self.cart_service.update_cart_item_quantity(self.user_service.current_user_id,product_id,product_quantity)
            if success:
                print(message)
                break
            else :
                print(message)   
                continue   

    def _do_view_cart(self): #| 查看购物车 |
        if not self.user_service.current_user:
            print('未登录，无法查看')
        success, items = self.cart_service.view_cart(self.user_service.current_user_id)
        if success:
            if len(items) == 0:
                print('购物车为空')
            else:
                print('-----------用户购物车列表-------------')
                for item in items:
                    print(f'{item.user_id:<10d}{item.product_id:<20d}{item.product_name:20s}{item.price:<12.2f}{item.quantity:<10d}')
        else:
            print('错误:用户不存在')

    def _do_checkout(self): #| 结算 |
        if not self.user_service.current_user:
            print('未登录，无法结算')
        success,message = self.cart_service.checkout(self.user_service.current_user_id, self.user_service.current_user.balance)
        if success:
            print(message)
        else:
            print(message)

    def _do_clear_cart(self): #| 清空购物车 |
        if not self.user_service.current_user:
            print('未登录，无法清空')
        success,message = self.cart_service.clear_cart(self.user_service.current_user_id)
        if success:
            print(message)
        else :
            print(message)   
    
    def main_program(self):#主程序循环
        data.Data()#初始化管理员数据
        while True:
            self.print_menu()
            choice = input('请输入编号:')
            match choice:
                case '1':
                    self._do_login()
                case '2':
                    self._do_register()
                case '3':
                    self._do_logout()
                case '4':
                    self._do_query_balance()
                case '5':
                    self._do_recharge()
                case '6':
                    self._do_view_products()
                case '7':
                    self._do_add_product()
                case '8':
                    self._do_delete_product()
                case '9':
                    self._do_update_product()
                case '10':
                    self._do_add_to_cart()
                case '11':
                    self._do_remove_from_cart()
                case '12':
                    self._do_update_cart_quantity()
                case '13':
                    self._do_view_cart()
                case '14':
                    self._do_checkout()
                case '15':
                    self._do_clear_cart()
                case '0':
                    break
                case _:
                    print('输入的编号有误请重新输入：')
                    continue