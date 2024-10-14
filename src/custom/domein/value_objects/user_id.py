import uuid


class UserId:
    """ユーザーIDをuuidで発行して管理する"""

    def __init__(self):
        self.value = str(uuid.uuid4())
