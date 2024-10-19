from src.core.logger.logger import logger
from src.core.trunsaction.trunsaction import transactional
from src.custom.domein.entities.user import User
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName
from src.custom.infrastructure.repositories.user_repository import UserRepository


class UserDeleteService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def delete_user(self, user_id: str) -> bool:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            print("指定されたユーザーが見つかりません。")
            return False

        self.user_repository.delete(user_id)
        self.user_repository.commit()
        print("ユーザーが正常に削除されました。")
        return True
