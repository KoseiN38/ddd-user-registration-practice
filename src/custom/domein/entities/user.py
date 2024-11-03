from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class User:
    """値オブジェクトとしてユーザーID,ユーザー名を管理する"""

    def __init__(self, user_id: UserId, user_name: UserName):
        self.user_id = user_id
        self.user_name = user_name

    def change_name(self, user_name: UserName):
        self.user_name = user_name

    def change_id(self, user_id: UserId):
        self.user_id = user_id
