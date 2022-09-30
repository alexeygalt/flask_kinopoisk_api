from flask import request
from flask_restx import Namespace, Resource

from project.decorators import auth_required
from project.container import auth_service, user_service, favourite_service, movie_service
from project.dao.models import MovieSchema
from project.dao.models.favourites import FavouriteSchema

favourite_ns = Namespace('favorites')
favourite_schema = FavouriteSchema()
favourites_schema = FavouriteSchema(many=True)
movies_schema = MovieSchema(many=True)


@favourite_ns.route('/movies/')
class FavouritesViews(Resource):
    @auth_required
    @favourite_ns.doc(description='Get user favourites')
    def get(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        email = auth_service.get_email(token)
        user_id = user_service.get_by_email(email).id
        favourites = favourite_service.get_user_favourites(user_id)
        return movies_schema.dump(favourites), 200


@favourite_ns.route('/movies/<int:mid>/')
class FavouriteView(Resource):
    @auth_required
    @favourite_ns.doc(description='Add favourites')
    def post(self, mid):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        email = auth_service.get_email(token)
        user_id = user_service.get_by_email(email).id

        movie_service.get_one(mid)
        favourite_service.add_favourite(user_id, mid)
        return "", 201

    @auth_required
    @favourite_ns.doc(description='Delete favourites')
    def delete(self, mid):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        email = auth_service.get_email(token)
        user_id = user_service.get_by_email(email).id
        if movie_service.get_one(user_id):
            favourite_service.delete_favourite(user_id, mid)
        return "", 204




