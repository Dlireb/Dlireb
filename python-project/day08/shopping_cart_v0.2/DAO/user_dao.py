from data.data import test_user_name
from data import data
class User_datas:
    def get_all_users(self):#| List[dict] | 获取所有用户 |
        return test_user_name.copy()

    def get_user_by_id(self,user_id):#| user_id | Optional[User] | 根据 ID 获取用户 |
        for item in test_user_name:#list
            if item.user_id == user_id:
                return item
        return None

    def get_user_by_name(self,name):#| name | Optional[User] | 根据名称获取用户 |
        for user in test_user_name:
           if user.name == name:
            return user
        return None

    def get_user_by_name_or_phone(self,name,phone):#| name, phone | tuple | 检查用户是否存在 |
        for user in test_user_name:
            if user.name == name:
                return False,'用户名已存在'
            if user.phone == phone:
                return False,'手机号码已注册'
        return True,'用户名和手机号合法'

    def add_user(self,user):#| user | bool | 添加用户 |
        user.user_id = data.new_user_id
        test_user_name.append(user)
        data.new_user_id += 1
        return True

    def update_user(self,user_id,**kwargs):#| user_id, **kwargs | bool | 更新用户信息 |
        text_user = self.get_user_by_id(user_id)
        # 支持更新的字段：balance
        if "balance" in kwargs:
            text_user.balance = kwargs["balance"]
        return True

    def delete_user(self,user_id):#| user_id | bool | 删除用户 |
        user = self.get_user_by_id(user_id)
        if user:
            test_user_name.remove(user)
            return True
        return False