from abc import ABC, abstractmethod

from src.custom.domein.entities.user import User
from src.custom.domein.value_objects.user_name import UserName


class IUserFactory(ABC):
    """ファクトリとしてUserオブジェクトを生成する.

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def create(self, username: UserName) -> User:
        pass
