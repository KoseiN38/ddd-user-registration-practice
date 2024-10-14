import sqlite3

from src.custom.domein.entities.user import User


class UserRepository:
    """sqlite3に接続してクエリを構築する永続に関わる処理を実装する"""

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

    def find(self, username: str) -> bool:
        """入力されたユーザー名が存在しているか判定する"""
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
        return self.cursor.fetchone() is not None

    def save(self, user: User):
        """入力されたUserをデータベースに保存する"""
        self.cursor.execute(
            "INSERT INTO users (id, name) VALUES (?, ?)",
            (user.user_id.value, user.user_name.value),
        )

    def commit(self):
        """トランザクションをコミットする"""
        self.conn.commit()

    def rollback(self):
        """トランザクションをロールバックする"""
        self.conn.rollback()
