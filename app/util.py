import uuid

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List
from app.models import PlayerModel, GameModel
import uuid

def generate_uuid():
    return str(uuid.uuid4()).replace('-', '')

class HttpStatus(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500


def player_json(player: PlayerModel):
    """ Convert a Player Model to JSON """
    result = {
        "sign": player.sign,
        "id": player.id,

    }
    return result


def game_json(game: GameModel):
    """ Convert a Game Model to JSON """
    result = {

        "id": game.id,
        "status": game.status.value,
        "board": game.board

    }
    return result

