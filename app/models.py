from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from app.util import generate_uuid




db = SQLAlchemy()


class GStatus(Enum):
    """
        Enum hold all game status codes
    """
    RUNNING = "game_running"
    X_WON = "player_x_won"
    Y_YON = "player_y_won"
    DRAW = "draw"
    INACTIVE = "inactive"


class GameModel(db.Model):
    """
        Model represents game
    """

    __tablename__ = "games"

    id = db.Column(db.VARCHAR(255), primary_key=True)
    status = db.Column(db.Enum(GStatus), default=GStatus.INACTIVE)
    board = db.Column(db.String(120))
    player_id = db.Column(db.VARCHAR(255), db.ForeignKey("players.id"))

    def __init__(self, **kwargs):
        self.id = generate_uuid()
        super(GameModel, self).__init__(**kwargs)

    def __repr__(self):
        return f"Game = {self.id}, status = {self.status}"


class PlayerModel(db.Model):
    """
     Model represents game player
    """
    __tablename__ = 'players'

    # id = db.Column(db.VARCHAR(255), primary_key=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sign = db.Column(db.String(10))
    games = db.relationship('GameModel', backref='player', lazy='dynamic')

    def __repr__(self):
        return f"player {self.sign} with id <{self.id}>"
