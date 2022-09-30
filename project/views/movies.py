from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.dao.models import MovieSchema
from project.exceptions import ItemNotFound

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
    @movie_ns.doc(description='Get all movies', params={
        'page': 'Page number',
        'status': 'if "new": sort by release year'
    })
    def get(self):
        try:
            page = request.args.get('page', type=int)
            status = request.args.get('status')
            movies = movie_service.get_all(page, status)
            return movies_schema.dump(movies), 200
        except ItemNotFound:
            abort(404)


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movie_ns.doc(description='Get movie by id')
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except ItemNotFound:
            abort(404)
