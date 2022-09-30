from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_restx import Api

from project.exceptions import BaseServiceError

from project.setup_db import db
from project.views import auth_ns, genre_ns, user_ns, director_ns, favourite_ns, movie_ns

api = Api(title="Flask Course Project 4", doc="/docs")

cors = CORS()


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')
    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favourite_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
