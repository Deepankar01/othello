"""Othello Game"""

from othello.board import Board, Disc
from othello.rules import RuleEngine


class Othello:
    """Othello game class
    """
    def __init__(self) -> None:
        self.board = Board()
        self.rule_engine = RuleEngine(self.board)
        self.white_score = 0
        self.black_score = 0
        self.current_chance:Disc = Disc.BLACK # the game always starts with Black disc
    def __switch_current_chance(self):
        """Switches the current chance"""
        match self.current_chance:
            case Disc.BLACK:
                self.current_chance = Disc.WHITE
            case Disc.WHITE:
                self.current_chance = Disc.BLACK
    def start_game(self):
        """Start Othello game"""
        self.move()
        print(self.board)
    def move(self):
        """Place a disc on the board and validate whether it's a valid move or not"""
        self.board.add_disc(0,0, self.current_chance)
        self.__switch_current_chance()
        