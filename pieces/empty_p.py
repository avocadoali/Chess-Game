from pieces.piece import Piece


class Empty_P(Piece):
    def __init__(self):
        super().__init__("--", None, None, None)
