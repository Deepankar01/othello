"""Discs in Othello Baord"""
import enum

class Disc(enum.Enum):
    """Type of discs in Othello

    Args:
        enum (_type_): _description_

    Returns:
        _type_: disc types
    """
    BLACK = 'B'
    WHITE = 'W'

    @classmethod
    def get_other_disc_type(cls, disc_type):
        """Get the alternative colour of the disc"""
        return [disc for disc in map(lambda c: c, cls) if disc.value != disc_type.value][0]
    def __repr__(self) -> str:
        return self.value
    def __str__(self) -> str:
        return self.value
