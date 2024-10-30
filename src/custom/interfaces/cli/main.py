from flask import Flask, jsonify, request

from src.core.error.request_error import RequestParameterNotFoundError
from src.core.error.user_exist_error import (NotFoundUserError,
                                             NotFoundUserIdError,
                                             UserAlreadyExistError,
                                             UserNameAlreadyExistError)
from src.core.logger.logger import logger
from src.custom.application.users import (UserDeleteApplication,
                                          UserRegisterApplication,
                                          UserUpdateApplication)
from src.custom.domein.entities.user_factory import UserFactory
from src.custom.domein.services.user_service import UserService
from src.custom.infrastructure.repositories.user_repository import \
    UserRepository

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def handle_get_users():
    try:
        users = UserRepository().get_users()

        result = []
        for user in users:
            result.append(
                {
                    "id": user[0],
                    "name": user[1],
                },
            )
        return jsonify(result), 200
    except Exception as e:
        logger.error(e)
        return (
            jsonify(
                {
                    "message": str(e),
                },
            ),
            500,
        )


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
        user_factory = UserFactory()
        user_service = UserService(user_repository)
        program = UserRegisterApplication(user_service, user_repository, user_factory)
        user = program.execute(username)

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
        logger.error(e)
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


@app.route("/update", methods=["PUT"])
def handle_update_user_name():
    try:
        data = request.json
        userid = data.get("id")
        username = data.get("name")

        if (userid is None) or (username is None):
            raise RequestParameterNotFoundError(
                "リクエストパラメーターに不備があります.",
            )

        user_repository = UserRepository()
        user_service = UserService(user_repository)
        user_factory = UserFactory()
        program = UserUpdateApplication(user_service, user_repository, user_factory)
        user, status_code = program.execute(userid, username)

        if user is None:
            if status_code == 400:
                raise UserNameAlreadyExistError(
                    "新しいユーザー名がすでに存在します.",
                )
            elif status_code == 404:
                raise NotFoundUserIdError(
                    "指定されたユーザーが見つかりません.",
                )

        return (
            jsonify(
                {
                    "id": user.user_id.value,
                    "name": user.user_name.value,
                    "message": "ユーザー名が更新されました.",
                },
            ),
            200,
        )

    except RequestParameterNotFoundError as e:
        logger.error(e)
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

    except UserAlreadyExistError as e:
        logger.error(e)
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

    except NotFoundUserError as e:
        logger.error(e)
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
        logger.error(e)
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


@app.route("/delete", methods=["DELETE"])
def handle_delete_user():
    try:
        data = request.json
        userid = data.get("id")

        if userid is None:
            raise RequestParameterNotFoundError(
                "リクエストパラメーターに不備があります.",
            )

        user_repository = UserRepository()
        user_service = UserService(user_repository)
        user_factory = UserFactory()
        program = UserDeleteApplication(user_service, user_repository, user_factory)
        user = program.execute(userid)

        if user is None:
            raise NotFoundUserIdError(
                "指定されたユーザーが見つかりません.",
            )

        return (
            jsonify(
                {
                    "id": user.user_id.value,
                    "name": user.user_name.value,
                    "message": "ユーザーを削除しました",
                },
            ),
            200,
        )

    except RequestParameterNotFoundError as e:
        logger.error(e)
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

    except NotFoundUserError as e:
        logger.error(e)
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
        logger.error(e)
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
