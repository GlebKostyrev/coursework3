from db import db
from marshmallow import Schema, fields

class User(db.Models):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    favorite_genre = db.Column(db.String(20))

class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
