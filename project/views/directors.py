from flask import request
from flask_restx import Namespace, Resource

from project.container import director_service
from project.dao.models import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsViews(Resource):
    @director_ns.doc(description='Get all directors', params={'page': 'Page number'})
    def get(self):
        page = request.args.get('page', type=int)
        directors = director_service.get_all(page)
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    @director_ns.doc(description='Get director by id')
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

