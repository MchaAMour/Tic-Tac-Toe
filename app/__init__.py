from flask import Flask
from config import Config
from app.models import db
from flask_restful import Api
from app.resources import GameList, Game, Player


def create_app(config_class=Config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_class)
    api.add_resource(GameList, '/api/v1/games')
    api.add_resource(Player, '/api/v1/player')
    api.add_resource(Game, '/api/v1/games/<game_id>')
    db.app = app
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

