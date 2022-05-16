from game_logic.piece import Piece
from board import Board
from game_logic.crossed_p import Crossed_P

class Knight(Piece):
    def __init__(self, name, color, pos_x, pos_y):
        super().__init__(name, color, pos_x, pos_y)


    def check_up_right(self, board):
        pos_y = self.pos_y + 2 
        pos_x = self.pos_x + 1
        crossed_piece = Crossed_P()

        if board[pos_x][pos_y].name != "--":
            board[pos_x][pos_y] = crossed_piece

        board[pos_x][pos_y] = crossed_piece

    def check_up_left(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x - 1
        crossed_piece = Crossed_P()

        while (pos_y <= 7 and pos_x >= 0 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_y = pos_y + 1
            pos_x = pos_x - 1
        return 0

    def check_down_left(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x - 1
        crossed_piece = Crossed_P()

        while (pos_y >= 0 and pos_x >= 0 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_y = pos_y - 1
            pos_x = pos_x - 1
        return 0

    def check_down_right(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x + 1
        crossed_piece = Crossed_P()

        while (pos_y >= 0 and pos_x <= 7 and (self.color != board[pos_x][pos_y].color)):
            if board[pos_x][pos_y].name != "--":
                board[pos_x][pos_y] = crossed_piece
                break

            board[pos_x][pos_y] = crossed_piece
            pos_y = pos_y - 1
            pos_x = pos_x + 1
        return 0