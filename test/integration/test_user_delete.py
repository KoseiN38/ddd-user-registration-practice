import pytest

from src.custom.application.users import UserDeleteApplication, UserRegisterApplication
from src.custom.domein.services.user_service import UserService
from src.custom.domein.value_objects.user_id import UserId
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
def user_delete_application(service, repository):
    return UserDeleteApplication(service, repository)


def test_delete_user(user_register_application, user_delete_application, repository):
    user = user_register_application.execute("testuser")
    user = user_delete_application.execute(user.user_id.value)
    assert user.user_name.value == "testuser"
    assert repository.find(user.user_id) is False
    assert repository.find(user.user_name) is False


def test_delete_userid_not_found(user_register_application, user_delete_application):
    user = user_register_application.execute("testuser1")
    user = user_delete_application.execute(UserId().value)
    assert user is None
