from typing import Optional
from models.user import User_models
from common.validator import Validator
from DAO.user_dao import User_datas
class User_service:

    def __init__(self):
        self.user_dao = User_datas()
        self.validator = Validator()
        self.current_user: Optional[User_models] = None  # 当前登录用户
        self.current_user_id: Optional[int] = None  # 当前登录用户ID

    def register(self,name,password,phone):#| Tuple[bool, str] | 注册用户 |
        success_name,name_str =self.validator.validate_username(name)
        if not success_name:
            return False,name_str
        success_password,password_str = self.validator.validate_password(password)
        if not success_password:
            return False,password_str
        success_phone,phone_str = self.validator.validate_phone(phone)
        if not success_phone:
            return False,phone_str
        exists,exists_str = self.user_dao.get_user_by_name_or_phone(name,phone)#用户是否存在
        if not exists:
            return False,exists_str
        new_user = User_models(name,password,phone)
        success = self.user_dao.add_user(new_user)
        if success:
            return True,f"用户{name}注册成功,初始余额1000元"
        return False,"注册失败，请重试"
        
    def login(self,name,password):#| Tuple[bool, str] | 登录用户 |
        success_name , success_name_str = Validator.validate_username(name)
        if not success_name :
            return False,success_name_str
        success_paw,success_paw_str = Validator.validate_password(password)
        if not success_paw:
            return False, success_paw_str
        user_name = self.user_dao.get_user_by_name(name)
        if not user_name:
            return False, "用户不存在"
        if user_name.password != password:
            return False,'密码错误'
        user_name.login()
        self.current_user = user_name
        self.current_user_id = user_name.user_id
        return True, f"欢迎{name}登录！"

    def logout(self):#| Tuple[bool, str] | 注销/退出 |
        if not self.current_user:
            return False, "未登录，无需注销"
        self.current_user.logout() #修改登录状态
        self.current_user = None
        self.current_user_id = None
        return True,'注销成功'
        
    def query_balance(self):#| Tuple[bool, str] | 查询余额 |
        if not self.current_user:
            return False, "未登录，无法查询"
        return True,f'余额为：{self.current_user.balance}'

    def recharge(self,amount):#| Tuple[bool, str] | 充值 |
        if not self.current_user:
            return False,'请先登录'
        valid, msg = self.validator.validate_amount(amount)
        if not valid:
            return False, msg
        self.current_user.deposit(amount)
        return True,f'{amount}充值成功!'

    def get_user_info(self):#| Tuple[bool, str] | 获取用户信息 |
        if not self.current_user:
            return False,'请先登录'
        info =(
            f"用户ID：{self.current_user.user_id}\n"
            f"用户名：{self.current_user.name}\n"
            f"手机号：{self.current_user.phone}\n"
            f"余额：{self.current_user.balance:.2f}元\n"
            f"购物车：{self.current_user.cart}\n"
            f"状态：{self.current_user.status}"
        )
        return True,info