from dao.model.movie import Movie
# классы для работы с моделями CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Movie).get(aid)

    def get_all(self):
        return self.session.query(Movie).all()
