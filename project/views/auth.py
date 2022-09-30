from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegView(Resource):
    @auth_ns.doc(description='User registration')
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        if None in [email, password]:
            abort(400)

        data = {
            'email': email,
            'password': password
        }
        user = user_service.create(data)
        return "", 201, {"location": f"/user/{user.id}"}


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    @auth_ns.doc(description='Get tokens')
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        if None in [email, password]:
            abort(403)

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    @auth_ns.doc(description="Get new tokens")
    def put(self):
        refresh_token = request.json.get('refresh_token')
        if not refresh_token:
            abort(403)
        return auth_service.approve_token(refresh_token), 201