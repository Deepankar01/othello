"""Rule engine for Othello game"""
from othello.board import Board, Disc


class RuleEngine:
    """Othello rule engine
    """
    def __init__(self, board:Board) -> None:
        self.board = board

    def cross(self,disc_type: Disc):
        """Find the Diagonal pattern on the board matching with color

        Args:
            disc_type (Disc): type of disc to check pattern for
        """
        pass

    def horizontal(self,disc_type: Disc):
        """Find the horizontal pattern on the board matching with the color of the disc

        Args:
            disc_type (Disc): type of disc to check pattern for
        """
        pass

    def vertical(self,disc_type: Disc):
        """Find the vertical pattern on the board matching with the colour of the disc

        Args:
            disc_type (Disc): type of disc to check pattern for
        """
        pass
