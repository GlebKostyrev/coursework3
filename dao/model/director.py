from db import db
from marshmallow import Schema, fields

class Director(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
