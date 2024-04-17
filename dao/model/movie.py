from db import db
from marshmallow import Schema, fields

class Movie(db.Models):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(400))# описание
    trailer = db.Column(db.String(200))# ссылка на трейлер
    year = db.Column(db.Integer)# год выпуска
    rating = db.Column(db.Integer)# рейтинг
    genre_id = db.Column(db.Integer)# id жанра???????????????????
    director_id = db.Column(db.Integer)# id режиссера????????????????????????

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()
