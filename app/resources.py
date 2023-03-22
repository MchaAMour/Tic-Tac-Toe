from flask_restful import Resource
from flask import request, g
from app.game_repo import create_player, GameRepo
from app.util import player_json, game_json


class Player(Resource):
    def post(self):
        sign = request.json.get('sign')
        print(sign)
        new_player = create_player(sign)
        return player_json(new_player)


class GameList(Resource):
    def get(self):
        games = GameRepo.get_all_games()
        if not games:
            return "NOTFOUND", 404
        return games

    def post(self):
        player_id = request.json.get('player_id')
        board = request.json.get('board')
        new_game = GameRepo.add_game(player_id, board)
        return game_json(new_game)


class Game(Resource):
    def get(self, game_id):
        game = GameRepo.get_game(game_id)
        return game_json(game)

    def put(self):
        gamed_id = request.json.get('game_id')
        board = request.json.get('board')
        GameRepo.play_game(gamed_id, board)
        return 'Game updated', 201

    def delete(self, game_id):
        GameRepo.delete_game(game_id)
        return 'Done', 201
