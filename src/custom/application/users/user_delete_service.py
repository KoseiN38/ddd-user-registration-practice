from src.base.application.users.base_service_execute import BaseUserApplication
from src.core.logger.logger import logger
from src.core.trunsaction.trunsaction import transactional
from src.custom.domein.entities.user import User
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName
from src.custom.infrastructure.repositories.user_repository import UserRepository


class UserDeleteApplication(BaseUserApplication):
    def __init__(self, user_service: UserService, user_repository: UserRepository):
        self.user_service = user_service
        self.user_repository = user_repository

    @transactional
    def execute(self, user_id: str) -> bool:
        userid = UserId()
        userid.value = user_id
        user = User(userid, UserName("dummy"))
        if self.user_service.exist(user.user_id) is False:
            logger.error("指定されたユーザーが見つかりません。")
            return None

        user_name = self.user_repository.find_user_name(user_id)
        user.change_name(UserName(user_name))
        self.user_repository.delete(user)
        logger.info("ユーザーが正常に削除されました。")
        return user
