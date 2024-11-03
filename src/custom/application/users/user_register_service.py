from src.base.application.users.base_service_execute import BaseUserApplication
from src.base.domein.entities.base_iuser_factory import IUserFactory
from src.base.infrastructure.repositories.iuser_repository import IUserRepositry
from src.core.logger.logger import logger
from src.core.trunsaction.trunsaction import transactional
from src.custom.domein.entities.user import User
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_name import UserName


class UserRegisterApplication(BaseUserApplication):
    """ユーザーに関わる処理を実装する"""

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
    def execute(self, username: str) -> User:
        """
        Userインスタンスを作成し、UserServiceを呼び出して重複チェックをする。
        重複がなかった場合、userRepositoryを呼び出してデータベースに保存する
        """
        user = self.user_factory.create(UserName(username))
        if self.user_service.exist(user.user_name):
            return None
        self.user_repository.save(user)
        logger.info("ユーザーが正常に作成されました。")
        return user
