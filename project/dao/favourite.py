from project.dao.base import BaseDAO
from project.dao.models import Favourite, Movie


class FavouriteDAO(BaseDAO):
    def get_favourite(self, user_id, movie_id):
        """get favourite by user_id and movie_id"""
        return self.session.query(Favourite).filter(Favourite.user_id == user_id, Favourite.movie_id == movie_id).all()

    def get_user_favourites(self, user_id):
        """get favourites by user id"""
        return self.session.query(Movie).join(Favourite).filter(Favourite.user_id == user_id,
                                                               Movie.id == Favourite.movie_id).all()
