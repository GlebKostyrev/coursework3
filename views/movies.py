from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movie_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movie_schema.dump(all_movies), 200

@movie_ns.route('/int:uid')
class MovieView(Resource):
    def get(self, uid: int):
        movie = movie_service.get_one(uid)
        return movie_schema.dump(movie), 200
