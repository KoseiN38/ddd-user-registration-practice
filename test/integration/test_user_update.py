import pytest

from src.custom.application.users import UserRegisterApplication, UserUpdateApplication
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName
from src.custom.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)


@pytest.fixture
def repository():
    return InMemoryUserRepository()


@pytest.fixture
def service(repository):
    return UserService(repository)


@pytest.fixture
def user_register_application(service, repository):
    return UserRegisterApplication(service, repository)


@pytest.fixture
def user_update_application(service, repository):
    return UserUpdateApplication(service, repository)


def test_update_user_name(
    user_register_application, user_update_application, repository
):
    """正常系: 指定したユーザーに対してユーザー名が更新できることを確認.

    Args:
        user_register_application (_type_): _description_
        user_update_application (_type_): _description_
        repository (_type_): _description_
    """
    user = user_register_application.execute("testuser1")
    user, status_code = user_update_application.execute(user.user_id.value, "testuser2")
    assert user is not None
    assert user.user_name.value == "testuser2"
    assert repository.find(UserName("testuser2"))
    assert status_code == 200


def test_update_userid_not_found(user_register_application, user_update_application):
    """異常系: 指定したユーザーに対して存在しないIDを指定したときの確認.

    Args:
        user_register_application (_type_): _description_
        user_update_application (_type_): _description_
    """
    user = user_register_application.execute("testuser1")
    user, status_code = user_update_application.execute(UserId(), "testuser2")
    assert user is None
    assert status_code == 404


def test_update_user_duplicate(user_register_application, user_update_application):
    """異常系: 指定したユーザーに対して他ユーザーで重複したユーザー名を指定した時の確認.

    Args:
        user_register_application (_type_): _description_
        user_update_application (_type_): _description_
    """
    user1 = user_register_application.execute("testuser1")
    _ = user_register_application.execute("testuser2")
    user1, status_code = user_update_application.execute(
        user1.user_id.value, "testuser2"
    )
    assert user1 is None
    assert status_code == 400
