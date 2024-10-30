from abc import ABC, abstractmethod
from typing import Literal

from src.custom.domein.entities.user import User
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class IUserRepositry(ABC):
    """レポジトリ処理を管理する抽象クラス.

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def find_user_name(self, user_id: str):
        pass

    @abstractmethod
    def find(self, user_info: Literal[UserId, UserName]):
        pass

    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def update(self, user: User):
        pass

    @abstractmethod
    def delete(self, user: User):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
