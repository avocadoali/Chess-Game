
from pieces.board import Board
from pieces.crossed_p import Crossed_P
from pieces.piece import Piece

import copy


class Rook(Piece):
    def __init__(self, name, color, pos_x, pos_y):
        super().__init__(name, color, pos_x, pos_y)

    def check(self, board):
        e_board = Board()
        e_board.board = copy.deepcopy(board)
        self.check_up(e_board.board)
        self.check_down(e_board.board)
        self.check_left(e_board.board)
        self.check_right(e_board.board)
        print("")
        e_board.print()
        return e_board

    def check_up(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x
        crossed_piece = Crossed_P()

        while (pos_y <= 7 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_y = pos_y + 1
        return 0

    def check_down(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x
        crossed_piece = Crossed_P()
        while (pos_y >= 0 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_y = pos_y - 1
        return 0

    def check_left(self, board):
        pos_x = self.pos_x - 1
        pos_y = self.pos_y
        crossed_piece = Crossed_P()

        while (pos_x >= 0 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_x = pos_x - 1
        return 0

    def check_right(self, board):
        pos_x = self.pos_x + 1
        pos_y = self.pos_y
        crossed_piece = Crossed_P()

        while (pos_x <= 7 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_x = pos_x + 1
        return 0
