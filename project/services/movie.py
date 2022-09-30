from project.services.base import BaseService
from flask import abort


class MovieService(BaseService):
    def get_all(self, page=None, status=None):
        """get all movies"""
        movies = self.dao.get_all(page, do_sort=status == 'new')
        if not movies:
            abort(404)

        return movies
