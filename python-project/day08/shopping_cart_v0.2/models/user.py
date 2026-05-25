from re import T


class User_models:
    
    def __init__(self,name,password,phone,user_id=None,balance=1000,status='inactive'):
        self.user_id = user_id#| 用户 ID |
        self.name = name#| 用户名称 |
        self.password = password#| 用户密码 |
        self.phone = phone#| 用户手机号 |
        self.balance = balance# 初始余额1000元，符合业务规则
        self.cart= []# 购物车，关联CartItem对象
        self.status = status #用户状态active/inactive

    def deposit(self,amount):#充值
        if amount > 0:
            self.balance += amount
            return  True
        else :
            return False

    def withdraw(self,amount):#扣款
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            return True
    def login(self):#登录
        self.status = 'active'
    def logout(self):#注销
        self.status = 'inactive'