from flask import request
from flask_restx import Namespace, Resource

from project.decorators import auth_required
from project.container import auth_service, user_service
from project.dao.models import UserSchema

user_ns = Namespace('user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersViews(Resource):
    @auth_required
    @user_ns.doc(description='Get user by token')
    def get(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        email = auth_service.get_email(token)
        user = user_service.get_by_email(email)
        return user_schema.dump(user), 200

    @auth_required
    @user_ns.doc(description='Update user info(name, surname, fav genre)')
    def patch(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        email = auth_service.get_email(token)

        upload_data = user_schema.dump(request.get_json())
        print(upload_data)
        user_service.update_info(upload_data, email)
        return "", 201


@user_ns.route("/password/")
class PasswordView(Resource):
    @auth_required
    @user_ns.doc(description='Update user password')
    def put(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        email = auth_service.get_email(token)
        passwords = request.get_json()
        user_service.update_password(passwords, email)
        return "", 200



