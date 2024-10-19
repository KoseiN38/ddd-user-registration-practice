from typing import Dict, Literal

from src.custom.domein.entities.user import User
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class InMemoryUserRepository:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def find(self, user_info: Literal[UserId, UserName]) -> bool:
        print("情報", user_info.value)
        if isinstance(user_info, UserId):
            return any(user_info.value == user_id for user_id in self.users.keys())
        if isinstance(user_info, UserName):
            return any(
                user_info.value == user.user_name.value for user in self.users.values()
            )

    def save(self, user: User):
        self.users[user.user_id.value] = user

    def commit(self):
        pass  # インメモリ実装のため、実際のコミットは必要ありません

    def rollback(self):
        pass  # インメモリ実装のため、実際のロールバックは必要ありません
