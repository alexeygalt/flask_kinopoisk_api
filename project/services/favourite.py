from flask_restx import abort

from project.services.base import BaseService


class FavouriteService(BaseService):
    def  add_favourite(self, user_id, movie_id):
        """add movie to favourite"""
        if self.dao.get_favourite(user_id, movie_id):
            abort(400)

        data = {
            'user_id': user_id,
            'movie_id': movie_id
        }
        self.dao.create(data)

    def delete_favourite(self, user_id, movie_id):
        """delete movie from favourite"""
        favourite = self.dao.get_favourite(user_id, movie_id)

        if not favourite:
            abort(404)

        self.dao.delete(favourite[0].id)

    def get_user_favourites(self, user_id):
        """get all user favourite movies"""
        favourites = self.dao.get_user_favourites(user_id)

        if not favourites:
            abort(404)

        return favourites

