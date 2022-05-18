
from re import I
from game_logic.board import Board
from game_logic.crossed_p import Crossed_P
from game_logic.piece import Piece

import copy

class Pawn(Piece):
    def __init__(self, name, color, pos_x, pos_y):
        super().__init__(name, color, pos_x, pos_y)
        self.enpas = False

    
    def check(self, board):
        e_board = Board()
        e_board.board = copy.deepcopy(board)
        self.check_up(e_board.board)
        print("")
        e_board.print()
        return e_board

    def check_up(self, board):
        steps = 1

        # Check if pawn is in front row
        # for double steps on the first move
        if self.color == "W" and self.pos_y == 1:
            steps = 2 
        elif self.color == "B" and self.pos_y == 6:
            steps = 2

        pos_y = self.pos_y + 1
        pos_x = self.pos_x
        crossed_piece = Crossed_P()

        while (pos_y <= 7 and pos_y <= (self.pos_y+steps) and  board[pos_x][pos_y].name == "--"):
            board[pos_x][pos_y] = crossed_piece
            pos_y = pos_y + 1
        return 0