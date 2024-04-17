from flask import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
director_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return director_schema.dump(all_directors), 200

@director_ns.route('/int:uid')
class DirectorView(Resource):
    def get(self, uid: int):
        director = director_service.get_one(uid)
        return director_schema.dump(director), 200
