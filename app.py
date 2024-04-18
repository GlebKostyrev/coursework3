from flask import Flask
from flask_restx import Api
import json
from typing import Any, Dict, List, Type
from config import Config
from db import db
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)

def load_data(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))
def load_data():
    with open("fixtures.json") as f:
        return json.loads(f)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
