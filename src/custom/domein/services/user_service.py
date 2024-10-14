from src.custom.domein.entities.user import User
from src.custom.infrastructure.repositories.user_repository import UserRepository


class UserService:
    """Userに関わるドメインサービスを実装する"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def exist(self, user: User) -> bool:
        """userRepositryを呼び出して入力されたUserの重複確認をする"""
        return self.user_repository.find(user.user_name.value)
