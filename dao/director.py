from dao.model.director import Director
# классы для работы с моделями CRUD
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Director).get(aid)

    def get_all(self):
        return self.session.query(Director).all()
