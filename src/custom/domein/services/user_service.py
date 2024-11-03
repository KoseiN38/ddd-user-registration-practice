from typing import Literal

from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName
from src.custom.infrastructure.repositories.user_repository import UserRepository


class UserService:
    """Userに関わるドメインサービスを実装する"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def exist(self, user_info: Literal[UserId, UserName]) -> bool:
        """userRepositryを呼び出して入力されたUserの重複確認をする"""
        return self.user_repository.find(user_info)
