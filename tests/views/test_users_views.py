import pytest

from project.dao.models import User


class TestUsersView:
    @pytest.fixture
    def user(self, db):
        obj = User(id=1, email="test", password="test", name="test_one")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, user):
        response = client.get("/user/")
        assert response.status_code == 401
        assert response.json == {'message': 'Authorization not found'}


