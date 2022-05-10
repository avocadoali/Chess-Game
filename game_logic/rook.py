
from board import Board
from game_logic.crossed_p import Crossed_P
from game_logic.piece import Piece

import copy


class Rook(Piece):
    def __init__(self, name, color, pos_x, pos_y):
        super().__init__(name, color, pos_x, pos_y)

    def check(self, board):
        e_board = Board()
        e_board.board = copy.deepcopy(board)
        e_board.print()
        print("")
        self.check_up(e_board.board)
        print("")
        self.check_down(e_board.board)
        e_board.print()
        return e_board

    def check_up(self, board):
        pos_y = self.pos_y
        pos_y += 1
        crossed_piece = Crossed_P()
        while (pos_y <= 7 and (self.color != board[self.pos_x][pos_y].color)):
            if board[self.pos_x][pos_y].name != "--":
                board[self.pos_x][pos_y] = crossed_piece
                break

            board[self.pos_x][pos_y] = crossed_piece
            
            try:
                board[self.pos_x][pos_y+1].name != "--"
            except:
                break
            pos_y = pos_y + 1
        return 0

    def check_down(self, board):
        pos_y = self.pos_y
        pos_y -= 1
        crossed_piece = Crossed_P()
        while (pos_y >= 0 and (self.color != board[self.pos_x][pos_y].color)):
            if board[self.pos_x][pos_y].name != "--":
                board[self.pos_x][pos_y] = crossed_piece
                break

            board[self.pos_x][pos_y] = crossed_piece
            
            try:
                board[self.pos_x][pos_y-1].name != "--"
            except:
                break
            pos_y = pos_y - 1
        return 0


    



   
