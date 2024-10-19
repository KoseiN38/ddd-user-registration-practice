from flask import Flask, jsonify, request

from src.core.error.request_error import RequestParameterNotFoundError
from src.core.error.user_exist_error import (
    UserAlreadyExistError,
    UserNameAlreadyExistError,
)
from src.core.logger.logger import logger
from src.custom.application.users.user_register_service import UserRegisterApplication
from src.custom.domein.services.user_service import UserService
from src.custom.infrastructure.repositories.user_repository import UserRepository

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def handle_create_user():
    """メイン関数"""
    try:
        data = request.json
        username = data.get("name")
        if username is None:
            raise RequestParameterNotFoundError(
                "リクエストパラメーター(username)に不備があります.",
            )

        user_repository = UserRepository()
        user_service = UserService(user_repository)
        program = UserRegisterApplication(user_service, user_repository)
        user = program.create_user(username)

        if user is None:
            raise UserNameAlreadyExistError(
                "ユーザー名がすでに存在します.",
            )

        return (
            jsonify(
                {
                    "id": user.user_id.value,
                    "name": user.user_name.value,
                    "message": "ユーザーが作成されました。",
                },
            ),
            200,
        )

    except UserAlreadyExistError as e:
        return (
            jsonify(
                {
                    "id": "",
                    "name": username,
                    "message": str(e),
                },
            ),
            400,
        )

    except RequestParameterNotFoundError as e:
        return (
            jsonify(
                {
                    "id": "",
                    "name": "",
                    "message": str(e),
                },
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "id": "",
                    "name": "",
                    "message": str(e),
                },
            ),
            500,
        )


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        logger.error(e)
