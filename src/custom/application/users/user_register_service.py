from src.core.logger.logger import logger
from src.core.trunsaction.trunsaction import transactional
from src.custom.domein.entities.user import User
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName
from src.custom.infrastructure.repositories.user_repository import UserRepository


class UserRegisterApplication:
    """ユーザーに関わる処理を実装する"""

    def __init__(self, user_service: UserService, user_repository: UserRepository):
        self.user_service = user_service
        self.user_repository = user_repository

    @transactional
    def create_user(self, username: str) -> User:
        """
        Userインスタンスを作成し、UserServiceを呼び出して重複チェックをする。
        重複がなかった場合、userRepositoryを呼び出してデータベースに保存する
        """
        user = User(UserId(), UserName(username))
        if self.user_service.exist(user.user_name):
            return None
        self.user_repository.save(user)
        logger.info("ユーザーが正常に作成されました。")
        return user
