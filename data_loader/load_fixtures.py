import os, sys

path = os.path.abspath('')
sys.path.insert(1, path)

from sqlalchemy.exc import IntegrityError

from project.config import DevelopmentConfig
from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.server import create_app
from project.setup_db import db
from project.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("../data_loader/fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(**genre))

    for director in data["directors"]:
        db.session.add(Director(**director))

    for movie in data["movies"]:
        db.session.add(Movie(**movie))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
