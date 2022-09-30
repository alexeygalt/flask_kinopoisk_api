import pytest

from project.dao import GenreDAO

from project.dao.models import Genre


class TestGenresDAO:

    @pytest.fixture
    def genres_dao(self, db):
        return GenreDAO(db.session, model=Genre)

    @pytest.fixture
    def genre_1(self, db):
        g = Genre(id=1, name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def genre_2(self, db):
        g = Genre(name="Комедия")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_one(self, genre_1, genres_dao):
        assert genres_dao.get_one(genre_1.id) == genre_1

    def test_get_all(self, genre_1, genre_2, genres_dao):
        assert genres_dao.get_all() == [genre_1, genre_2]

    def test_create(self, genres_dao, genre_2):
        data = {

            "name": "Test"
        }
        new_genre = genres_dao.create(data)
        assert new_genre.id is not None
        assert new_genre.name == "Test"

    # def test_delete(self, genres_dao, genre_1, pk=1):
    #     genres_dao.delete(pk)
    #     assert genre_1 is None
