from src.base.application.users.base_service_execute import BaseUserApplication
from src.base.domein.entities.base_iuser_factory import IUserFactory
from src.base.infrastructure.repositories.iuser_repository import \
    IUserRepositry
from src.core.logger.logger import logger
from src.core.trunsaction.trunsaction import transactional
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


class UserDeleteApplication(BaseUserApplication):
    def __init__(self, user_service: UserService, user_repository: IUserRepositry, user_factory: IUserFactory):
        self.user_service = user_service
        self.user_repository = user_repository
        self.user_factory = user_factory

    @transactional
    def execute(self, user_id: str) -> bool:
        userid = UserId()
        userid.value = user_id
        user = self.user_factory.create(
            userid=userid,
            username=UserName("dummy"),
        )
        if self.user_service.exist(user.user_id) is False:
            logger.error("指定されたユーザーが見つかりません。")
            return None

        user_name = self.user_repository.find_user_name(user_id)
        user.change_name(UserName(user_name))
        self.user_repository.delete(user)
        logger.info("ユーザーが正常に削除されました。")
        return user
