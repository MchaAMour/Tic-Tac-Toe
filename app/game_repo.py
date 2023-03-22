from app.models import PlayerModel, GameModel, db, GStatus
import random

from dataclasses import dataclass

"""Tic-Tac-Toe
game steps
    - print the game board
    - take player input
    - check for win or tie
    - switch player
    - check for win or tie again
"""


def create_player(sign: str):
    new_player = PlayerModel(sign=sign.capitalize())
    db.session.add(new_player)
    db.session.commit()
    return new_player


@dataclass
class GameRepo:

    @classmethod
    def add_game(cls, player_id, board="X--------"):
        game = GameModel(status=GStatus.RUNNING,
                         board=board,
                         player_id=player_id)
        db.session.add(game)
        db.session.commit()
        return game

    @classmethod
    def play_game(cls, game_id, board):
        game = GameRepo.get_game(game_id)
        game.board = board
        db.session.add(game)
        db.session.commit()

    @staticmethod
    def get_game(game_id):
        game = GameModel.query.get(game_id)
        if not game:
            return None
        return game

    @staticmethod
    def delete_game(game_id):
        game = GameRepo.get_game(game_id)
        if not game:
            return None
        db.session.delete(game)
        db.session.commit()
        return "sucessfully deleted"

    @classmethod
    def get_all_games(cls):
        games = list(GameModel.query.all())
        return games


@dataclass
class TicTacToe:
    player_sign: str
    game_running: bool = False

    def __post_init__(self):
        self.player_sign = self.player_sign.capitalize()
        self.pc_sign = "O" if self.player_sign == "X" else "X"
        self.board = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-",
        ]

    def print_board(self):
        print("." + "-" * 11 + ".")
        print("| " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " | ")
        print("+" + "-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "+")
        print("| " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " | ")
        print("+" + "-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "+")
        print("| " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " | ")
        print("." + "-" * 11 + ".")

    def check_win(self, sign: str):
        if (self.board[0] == self.board[4] == self.board[8]) or (self.board[2] == self.board[4] == self.board[6]):
            if self.board[4] != "-":
                self.winner_package(sign)
        elif (self.board[1] == self.board[4] == self.board[7]) or (self.board[3] == self.board[4] == self.board[5]):
            if self.board[4] != "-":
                self.winner_package(sign)
        elif self.board[0] == self.board[1] == self.board[2]:
            if self.board[1] != "-":
                self.winner_package(sign)
        elif self.board[6] == self.board[7] == self.board[8]:
            if self.board[7] != "-":
                self.winner_package(sign)
        elif self.board[0] == self.board[3] == self.board[6]:
            if self.board[3] != "-":
                self.winner_package(sign)
        elif self.board[2] == self.board[5] == self.board[8]:
            if self.board[5] != "-":
                self.winner_package(sign)
        elif any(bloc == "-" for bloc in self.board):
            self.game_running = True
        else:
            print("This game ended in Draw")
            print("NO Winner")
            self.game_running = False

    def winner_package(self, sign: str) -> None:
        self.print_board()
        print(f"The winner is player {sign}")
        self.game_running = False

    def pc_move(self):
        while True:
            pc_move = random.randint(0, 8)
            if self.board[pc_move] == "-":
                self.board[pc_move] = self.pc_sign
                break

    def start_game(self):
        self.game_running = True
        print("Game has started")
        while self.game_running:
            self.print_board()
            player_move = int(input("choose the position where you want to play\n"))
            self.board[player_move] = self.player_sign
            self.check_win(sign=self.player_sign)
            if not self.game_running:
                break
            self.pc_move()
            self.check_win(sign=self.pc_sign)

        print("Game has Ended")
