from marshmallow import Schema, fields

from project.dao.models.movie import MovieSchema
from project.setup_db import db


class Favourite(db.Model):
    __tablename__ = 'favourite'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    user = db.relationship('User')
    movie = db.relationship('Movie')


class FavouriteSchema(Schema):
    user_id = fields.Int()
    movie = fields.Nested(MovieSchema)
