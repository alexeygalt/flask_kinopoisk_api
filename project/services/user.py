import base64
import hashlib
import hmac

from flask import current_app
from flask_restx import abort

from project.services.base import BaseService


class UserService(BaseService):
    def get_by_email(self, email):
        user = self.dao.get_by_email(email)
        if not user:
            abort(404)
        return user

    def create(self, data):
        user = self.dao.get_by_email(data.get('email'))
        if user:
            abort(400)
        data['password'] = self.create_hash(data.get('password'))
        return self.dao.create(data)

    def update_info(self, data, email):
        """update user info (name, surname, favourite genre)"""
        self.get_by_email(email)

        if 'password' not in data.keys() and 'email' not in data.keys():
            self.dao.update_by_email(data, email)

        else:
            abort(405)

    def update_password(self, data, email):
        user = self.get_by_email(email)
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        if None in [old_password, new_password] or not self.compare_passwords(user.password, old_password):
            abort(404)

        self.dao.update_by_email(
            {'password': self.create_hash(new_password)},
            email
        )

    def create_hash(self, password):
        """create password hash"""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            current_app.config.get('PWD_HASH_SALT'),
            current_app.config.get('PWD_HASH_ITERATIONS')))

    def compare_passwords(self, password_hash, other_password):
        """compare passwords"""
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), current_app.config.get('PWD_HASH_SALT'),
                                current_app.config.get('PWD_HASH_ITERATIONS')))
