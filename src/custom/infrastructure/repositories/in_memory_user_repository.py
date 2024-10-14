from typing import Dict

from src.custom.domein.entities.user import User


class InMemoryUserRepository:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def find(self, username: str) -> bool:
        return any(user.user_name.value == username for user in self.users.values())

    def save(self, user: User):
        self.users[user.user_id.value] = user

    def commit(self):
        pass  # インメモリ実装のため、実際のコミットは必要ありません

    def rollback(self):
        pass  # インメモリ実装のため、実際のロールバックは必要ありません
