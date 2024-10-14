from src.custom.application.users.user_register_service import UserRegisterApplication
from src.custom.domein.services.user_service import UserService
from src.custom.infrastructure.repositories.user_repository import UserRepository


def main():
    """メイン関数"""
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    program = UserRegisterApplication(user_service, user_repository)

    while True:
        username = input("ユーザー名を入力してください（終了するには 'q' を入力）: ")
        if username.lower() == "q":
            break
        try:
            program.create_user(username)
        except ValueError as e:
            print(f"エラー: {str(e)}")


if __name__ == "__main__":
    main()
