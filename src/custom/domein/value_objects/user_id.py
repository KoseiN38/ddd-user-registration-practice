import uuid
from typing import Optional


class UserId:
    """ユーザーIDをuuidで発行して管理する"""

    def __init__(self, user_id: Optional[str] = None):
        if user_id:
            self.value = str(user_id)
        else:
            self.value = str(uuid.uuid4())
