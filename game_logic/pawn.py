from game_logic.piece import Piece

class Pawn(Piece):
    def __init__(self, name, color, pos):
        super().__init__(name, color, pos, "P")
