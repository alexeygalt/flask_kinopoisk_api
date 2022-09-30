from project.setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
