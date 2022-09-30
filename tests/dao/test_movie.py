import pytest

from project.dao import MovieDAO
from project.dao.models import Movie


class TestMoviesDAO:

    @pytest.fixture
    def movies_dao(self, db):
        return MovieDAO(db.session, model=Movie)

    @pytest.fixture
    def movie_1(self, db):
        m = Movie(id=1, title="One", description="", trailer="", year=2005, rating=7.6, genre_id=1, director_id=1)
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def movie_2(self, db):
        m = Movie(id=2, title="Two", description="", trailer="", year=2005, rating=7.6, genre_id=1, director_id=1)
        db.session.add(m)
        db.session.commit()
        return m

    def test_get_one(self, movie_1, movies_dao):
        assert movies_dao.get_one(movie_1.id) == movie_1

    def test_get_all(self, movie_1, movie_2, movies_dao):
        assert movies_dao.get_all() == [movie_1, movie_2]

    def test_create(self, movies_dao, movie_2):
        data = {

            "title": "Three",
            "description": "",
            "trailer": "",
            "year": 2005, "rating": 7.6, "genre_id": 1, "director_id": 1
        }
        new_movie = movies_dao.create(data)
        assert new_movie.id is not None
        assert new_movie.title == "Three"

    # def test_delete(self, genres_dao, genre_1, pk=1): HOW TO CREATE THIS TEST?
    #     genres_dao.delete(pk)
    #     assert genre_1 is None
