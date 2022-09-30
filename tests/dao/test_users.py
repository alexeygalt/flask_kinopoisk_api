import pytest

from project.dao import UserDAO

from project.dao.models import User


class TestUsersDAO:

    @pytest.fixture
    def users_dao(self, db):
        return UserDAO(db.session, model=User)

    @pytest.fixture
    def user_1(self, db):
        u = User(id=1, email="test", password="test", name="alex")
        db.session.add(u)
        db.session.commit()
        return u

    @pytest.fixture
    def user_2(self, db):
        u = User(id=2, email="test_two", password="test_two")
        db.session.add(u)
        db.session.commit()
        return u

    def test_get_by_email(self, users_dao, user_1, email="test"):
        assert users_dao.get_by_email(email) == user_1

    def test_update_by_email(self, users_dao, user_1, email="test"):
        data = {"name": "update"}
        users_dao.update_by_email(data, email)
        assert user_1.name == "update"

    def test_create(self, users_dao):
        data = {
            "id": 3,
            "email": "update",
            "password": "update",
            "name": "update"
        }
        new_user = users_dao.create(data)
        assert new_user is not None
        assert new_user.name == "update"
