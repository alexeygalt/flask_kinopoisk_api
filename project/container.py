from project.dao import GenreDAO, MovieDAO, DirectorDAO, UserDAO, FavouriteDAO
from project.dao.models import Genre, Movie, Director, User
from project.dao.models.favourites import Favourite
from project.services import GenreService, MovieService, DirectorService, UserService, AuthService, FavouriteService
from project.setup_db import db

# GENRE
genre_dao = GenreDAO(session=db.session, model=Genre)
genre_service = GenreService(dao=genre_dao)

# MOVIE
movie_dao = MovieDAO(session=db.session, model=Movie)
movie_service = MovieService(dao=movie_dao)

# DIRECTOR
director_dao = DirectorDAO(session=db.session, model=Director)
director_service = DirectorService(dao=director_dao)

# USER
user_dao = UserDAO(session=db.session, model=User)
user_service = UserService(dao=user_dao)

# AUTH
auth_service = AuthService(user_service=user_service)

# FAVOURITE
favourite_dao = FavouriteDAO(session=db.session, model=Favourite)
favourite_service = FavouriteService(dao=favourite_dao)
