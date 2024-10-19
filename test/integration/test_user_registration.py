import pytest

from src.custom.application.users.user_register_service import UserRegisterApplication
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_name import UserName
from src.custom.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)


@pytest.fixture
def UserApplication():
    repository = InMemoryUserRepository()
    service = UserService(repository)
    return UserRegisterApplication(service, repository)


# テスト関数
def test_create_user_success(UserApplication):
    user = UserApplication.execute("testuser")
    assert user is not None
    assert user.user_name.value == "testuser"
    assert UserApplication.user_repository.find(UserName("testuser"))


def test_create_user_duplicate(UserApplication):
    UserApplication.execute("testuser")
    duplicate_user = UserApplication.execute("testuser")
    assert duplicate_user is None


def test_create_user_invalid_name(UserApplication):
    user = UserApplication.execute("ab")
    assert user is None


def test_create_multiple_users(UserApplication):
    user1 = UserApplication.execute("user1")
    user2 = UserApplication.execute("user2")
    assert user1 is not None
    assert user2 is not None
    assert UserApplication.user_repository.find(UserName("user1"))
    assert UserApplication.user_repository.find(UserName("user2"))
