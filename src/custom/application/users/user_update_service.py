from typing import Optional, Tuple

from src.base.application.users.base_service_execute import BaseUserApplication
from src.base.domein.entities.base_iuser_factory import IUserFactory
from src.base.infrastructure.repositories.iuser_repository import IUserRepositry
from src.core.logger.logger import logger
from src.core.trunsaction.trunsaction import transactional
from src.custom.domein.entities.user import User
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class UserUpdateApplication(BaseUserApplication):
    def __init__(
        self,
        user_service: UserService,
        user_repository: IUserRepositry,
        user_factory: IUserFactory,
    ):
        self.user_service = user_service
        self.user_repository = user_repository
        self.user_factory = user_factory

    @transactional
    def execute(self, user_id: str, new_username: str) -> Tuple[Optional[User], int]:
        user = self.user_factory.create(username=UserName(new_username))
        user.change_id(UserId(user_id))
        if self.user_service.exist(user.user_id) is False:
            logger.error("指定されたユーザーが見つかりません。")
            return None, 404

        if self.user_service.exist(user.user_name):
            logger.error("新しいユーザー名が既に存在します。")
            return None, 400

        user.change_name(UserName(new_username))
        self.user_repository.update(user)
        logger.info("ユーザー名が正常に更新されました。")
        return user, 200
