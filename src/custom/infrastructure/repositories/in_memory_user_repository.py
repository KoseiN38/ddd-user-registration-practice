from typing import Dict, Literal, Optional

from src.base.infrastructure.repositories.iuser_repository import IUserRepositry
from src.custom.domein.entities.user import User
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class InMemoryUserRepository(IUserRepositry):
    def __init__(self):
        self.users: Dict[str, User] = {}

    def get_user(self):
        pass

    def find_user_name(self, user_id: str) -> Optional[str]:
        return self.users[user_id].user_name.value if self.users[user_id] else None

    def find(self, user_info: Literal[UserId, UserName]) -> bool:
        if isinstance(user_info, UserId):
            return any(user_info.value == user_id for user_id in self.users.keys())
        if isinstance(user_info, UserName):
            return any(
                user_info.value == user.user_name.value for user in self.users.values()
            )

    def update(self, user: User):
        if user.user_id.value in self.users.keys():
            self.users[user.user_id.value] = user

    def save(self, user: User):
        self.users[user.user_id.value] = user

    def delete(self, user: User):
        del self.users[user.user_id.value]

    def commit(self):
        pass  # インメモリ実装のため、実際のコミットは必要ありません

    def rollback(self):
        pass  # インメモリ実装のため、実際のロールバックは必要ありません
