"""Creates an Othello Board"""
import numpy as np
from othello.disc import Disc


class Board:
    """Othello Board
    """
    def __init__(self) -> None:
        self.board = np.zeros(shape=(8,8), dtype=Disc)
        self.board.fill('0')
        self.white_discs:int = 32
        self.black_discs:int = 32
        self.__set_board()
    def __update_disc_count(self, disc_type:Disc):
        """Update Disc count based on the disc type

        Args:
            disc_type (Disc): Type of disc
        """
        match disc_type:
            case Disc.BLACK:
                self.black_discs = self.black_discs -1
            case Disc.WHITE:
                self.white_discs = self.white_discs -1
    def __repr__(self) -> str:
        return '\n'.join([''.join([f'{item:4}' for item in row]) for row in self.board])

    def __str__(self) -> str:
        return '\n'.join([''.join([f'{item:4}' for item in row]) for row in self.board])

    def __set_board(self):
        self.add_disc(3,3,Disc.BLACK)
        self.add_disc(3,4,Disc.WHITE)
        self.add_disc(4,3,Disc.WHITE)
        self.add_disc(4,4,Disc.BLACK)

    def add_disc(self, x_axis: int, y_axis:int, disc_type:Disc) -> None:
        """Place a disc on the board

        Args:
            x_axis (int): x axis of the board
            y_axis (int): y axis of the board
            disc_type (Disc): type of disc type
        """
        self.board[x_axis, y_axis] = disc_type
        self.__update_disc_count(disc_type)

    def flip_disc(self,  x_axis: int, y_axis:int) -> None:
        """Flip a disc on the board

        Args:
            x_axis (int): x axis of the board
            y_axis (int): y axis of the board
        """
        self.board[x_axis, y_axis] = Disc.get_other_disc_type(self.board[x_axis, y_axis])
        