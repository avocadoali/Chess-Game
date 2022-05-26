from board.board import Board

class Game():

    def __init__(self, ):
        self.board = Board()
        self.current_player = "W"

    def check_field(self, pos_x, pos_y):
        self.board.check_for_field(pos_x, pos_y)


    def print(self):
        self.board.print()
        return 0




    def check_legal_moves_left():
        return 0
