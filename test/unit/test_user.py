import pytest

from src.custom.domein.entities.user_factory import UserFactory
from src.custom.domein.value_objects.user_id import UserId
from src.custom.domein.value_objects.user_name import UserName


@pytest.fixture
def user_factory():
    return UserFactory()


@pytest.mark.parametrize(
    ("user_id", "user_name"),
    [
        ("001", "testuser1"),
        ("002", "testuser2"),
    ],
)
def test_create_user(user_factory, user_id, user_name):
    user = user_factory.create(
        userid=UserId(user_id),
        username=UserName(user_name),
    )
    assert user.user_id.value == user_id
    assert user.user_name.value == user_name


@pytest.mark.parametrize(
    ("user_id", "changed_user_id", "user_name"),
    [
        ("001", "0011", "testuser1"),
        ("002", "0022", "testuser2"),
    ],
)
def test_change_id(user_factory, user_id, changed_user_id, user_name):
    user = user_factory.create(
        userid=UserId(user_id),
        username=UserName(user_name),
    )
    user.change_id(UserId(changed_user_id))
    assert user.user_id.value == changed_user_id
    assert user.user_name.value == user_name


@pytest.mark.parametrize(
    ("user_id", "user_name", "changed_user_name"),
    [
        ("001", "testuser1", "testuser11"),
        ("002", "testuser2", "testuser22"),
    ],
)
def test_change_username(user_factory, user_id, user_name, changed_user_name):
    user = user_factory.create(
        userid=UserId(user_id),
        username=UserName(user_name),
    )
    user.change_name(UserName(changed_user_name))
    assert user.user_id.value == user_id
    assert user.user_name.value == changed_user_name
