import pytest

from project.dao.models import Genre


class TestGenresView:
    @pytest.fixture
    def genre(self, db):
        obj = Genre(name="genre")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, genre):
        response = client.get("/genres/")
        assert response.status_code == 200
        assert response.json == [{"id": genre.id, "name": genre.name}]

    def test_genre(self, client, genre):
        response = client.get("/genres/1/")
        assert response.status_code == 200
        assert response.json == {"id": genre.id, "name": genre.name}

    def test_genre_not_found(self, client, genre):
        with pytest.raises(Exception) as exc_info:
            response = client.get("/genres/2/")
            assert response == exc_info  ## ??
