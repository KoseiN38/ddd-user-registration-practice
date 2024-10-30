from typing import Optional

from src.base.domein.entities.base_iuser_factory import IUserFactory
from src.custom.domein.entities.user import User
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class UserFactory(IUserFactory):
    def create(self, username: UserName, userid: Optional[UserId] = None) -> User:
        if userid:
            return User(
                user_id=userid,
                user_name=username,
            )
        return User(
            user_id=UserId(),
            user_name=username,
        )
