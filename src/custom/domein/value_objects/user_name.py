class UserName:
    """入力されたユーザー名が３文字以上であるか判定し管理する"""

    def __init__(self, value: str):
        if len(value) < 3:
            raise ValueError("ユーザー名は3文字以上である必要があります。")
        self.value = value
