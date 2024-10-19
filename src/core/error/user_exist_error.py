class UserAlreadyExistError(Exception):
    """ユーザー情報が重複しているエラー.

    Args:
        Exception (_type_): _description_
    """


class UserNameAlreadyExistError(UserAlreadyExistError):
    """ユーザー名が重複しているエラー.

    Args:
        UserAlreadyExistError (_type_): _description_
    """


class NotFoundUserError(Exception):
    """対象のユーザーが見つからなかった.

    Args:
        Exception (_type_): _description_
    """


class NotFoundUserIdError(NotFoundUserError):
    """対象のユーザーIDが見つからなかった.

    Args:
        NotFoundUserError (_type_): _description_
    """
