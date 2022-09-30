from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api

from project.setup_db import db
from project.views import movie_ns, director_ns, genre_ns, auth_ns, user_ns, favourite_ns

api = Api(title="Flask Course Project 4", doc="/docs")

cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favourite_ns)

    return app
