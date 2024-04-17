from db import db
from marshmallow import Schema, fields

class Genre(db.Models):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
