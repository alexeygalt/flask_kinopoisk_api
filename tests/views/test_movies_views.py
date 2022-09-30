import pytest

from project.dao.models import Movie


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj = Movie(id=1, title='Самый', description='Лучший', trailer='Фильм', year=2005, rating=5.2,
                    genre_id=1,
                    director_id=1)
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre": movie.genre, "director": movie.director}]

    def test_director(self, client, movie):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre": movie.genre, "director": movie.director}

    def test_director_not_found(self, client, movie):
        with pytest.raises(Exception) as exc_info:
            response = client.get("/movies/2/")
            assert response == exc_info  ## ??
