from dao.director import DirectorDAO
from dao.movie import MovieDAO
from dao.genre import GenreDAO
from dao.user import UserDAO
from db import db
from services.director import DirectorService
from services.movie import MovieService
from services.user import UserService
from services.genre import GenreService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)