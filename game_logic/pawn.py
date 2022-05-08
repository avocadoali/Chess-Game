
from game_logic.piece import Piece

class Pawn(Piece):
    def __init__(self, name, color, abbre):
        super().__init__(name, color, abbre)
        self.enpas = False

