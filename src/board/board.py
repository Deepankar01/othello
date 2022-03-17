"""Creates an Othello Board"""
import enum
import numpy as np


class Disc(enum.Enum):
    """Disc types"""
    BLACK = '0'
    WHITE = 'X'


class Board:
    """Board class"""
    def __init__(self) -> None:
        self.board = np.arange(64).reshape(8, 8)
        self.white_discs:int = 32
        self.black_discs:int = 32

    def add_disc(self, position: list, disc_type:Disc):
        """Place a disc on the board"""
        pass

    def flip_disc(self, postion:list , disc_type:Disc):
        """flip a disc on the board"""
        pass