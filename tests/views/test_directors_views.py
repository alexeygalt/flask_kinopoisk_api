import pytest

from project.dao.models import Director


class TestDirectorsView:
    @pytest.fixture
    def director(self, db):
        obj = Director(name="director")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, director):
        response = client.get("/directors/")
        assert response.status_code == 200
        assert response.json == [{"id": director.id, "name": director.name}]

    def test_director(self, client, director):
        response = client.get("/directors/1/")
        assert response.status_code == 200
        assert response.json == {"id": director.id, "name": director.name}

    def test_director_not_found(self, client, director):
        with pytest.raises(Exception) as exc_info:
            response = client.get("/directors/2/")
            assert response == exc_info  ## ??
