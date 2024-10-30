import sqlite3
from typing import Literal, Optional

from src.base.infrastructure.repositories.iuser_repository import \
    IUserRepositry
from src.custom.domein.entities.user import User
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class UserRepository(IUserRepositry):
    """sqlite3に接続してクエリを構築する永続に関わる処理を実装する."""

    def __init__(self):
        self.conn = sqlite3.connect("db/users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (id TEXT PRIMARY KEY, name TEXT UNIQUE)
        """
        )
        self.conn.commit()

    def get_users(self):
        self.cursor.execute("SELECT id, name FROM users")
        users = self.cursor.fetchall()
        return users

    def find_user_name(self, user_id: str) -> Optional[str]:
        self.cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def find(self, user_info: Literal[UserId, UserName]) -> bool:
        """入力されたユーザー名が存在しているか判定する."""
        if isinstance(user_info, UserId):
            self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_info.value,))
            return self.cursor.fetchone() is not None
        if isinstance(user_info, UserName):
            self.cursor.execute(
                "SELECT * FROM users WHERE name = ?", (user_info.value,)
            )
            return self.cursor.fetchone() is not None

    def save(self, user: User):
        """入力されたUserをデータベースに保存する."""
        self.cursor.execute(
            "INSERT INTO users (id, name) VALUES (?, ?)",
            (user.user_id.value, user.user_name.value),
        )

    def update(self, user: User):
        """入力されたUserに該当するユーザー名を変更する."""
        self.cursor.execute(
            "UPDATE users SET name = ? WHERE id = ?",
            (user.user_name.value, user.user_id.value),
        )

    def delete(self, user: User):
        """入力されたUserに該当するユーザーを削除する."""
        self.cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user.user_id.value,),
        )

    def commit(self):
        """トランザクションをコミットする."""
        self.conn.commit()

    def rollback(self):
        """トランザクションをロールバックする."""
        self.conn.rollback()
