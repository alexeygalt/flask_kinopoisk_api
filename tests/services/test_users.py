from unittest.mock import MagicMock
import pytest
from werkzeug import exceptions

from project.dao import UserDAO
from project.dao.models import User
from project.services import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None, model=User)
    user_one = User(id=1, email="test", password="test", name="test_one")
    user_two = User(id=2, email="test_two", password="test_two")
    user_three = User(id=3, email="test_three", password="test_three")
    user_dao.get_by_email = MagicMock(return_value=user_one)
    user_dao.create = MagicMock()

    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_by_email(self):
        user = self.user_service.get_by_email(email="test")
        assert user is not None
        assert user.id is not None

    def test_create(self):
        with pytest.raises(exceptions.BadRequest):
            user_data = {
                "email": "test_two",
                "password": "test_two"
            }
            user = self.user_service.create(user_data)  ### ?




