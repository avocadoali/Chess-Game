import board.board as b

from pieces.piece import Piece
from pieces.crossed_p import Crossed_P

import copy


class King(Piece):
    def __init__(self, name, color, pos_x, pos_y):
        super().__init__(name, color, pos_x, pos_y)
        self.rochade_allowed= True

    def check(self, board):
        e_board = b.Board()
        e_board.board = copy.deepcopy(board)
        self.check_rochade_left(e_board.board)
        self.check_rochade_right(e_board.board)
        self.check_up(e_board.board)
        self.check_down(e_board.board)
        self.check_left(e_board.board)
        self.check_right(e_board.board)
        self.check_up_right(e_board.board)
        self.check_up_left(e_board.board)
        self.check_down_left(e_board.board)
        self.check_down_right(e_board.board)
        #e_board.print()

        return e_board

    def check_up(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x

        if (pos_y <= 7 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P()
        return 0

    def check_down(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x
        if (pos_y >= 0 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P()

        return 0

    def check_left(self, board):
        pos_x = self.pos_x - 1
        pos_y = self.pos_y

        if (pos_x >= 0 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P() 

        return 0

    def check_right(self, board):
        pos_x = self.pos_x + 1
        pos_y = self.pos_y

        if (pos_x <= 7 and self.color != board[pos_x][pos_y].color):
            board[pos_x][pos_y] = Crossed_P()
        
        return 0

    def check_up_right(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x + 1

        if (pos_y <= 7 
                and pos_x <= 7 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P()
        return 0

    def check_up_left(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x - 1

        if (pos_y <= 7 
                and pos_x >= 0 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P()
        return 0

    def check_down_left(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x - 1

        if (pos_y >= 0 
                and pos_x >= 0 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P() 
        return 0

    def check_down_right(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x + 1

        if (pos_y >= 0 
                and pos_x <= 7 
                and (self.color != board[pos_x][pos_y].color)):

            board[pos_x][pos_y] = Crossed_P()
        return 0

    def check_rochade_left(self, board):
        pos_x = self.pos_x 
        pos_y = self.pos_y


        # check if fields in between are not covered by other pieces
        if (self.rochade_allowed 
                and  "--" == board[pos_x-1][pos_y].name 
                and  "--" == board[pos_x-2][pos_y].name 
                and "R" in board[0][pos_y].name):

            board[pos_x-1][pos_y] = Crossed_P()
            board[pos_x-2][pos_y] = Crossed_P()
        return 0

    def check_rochade_right(self, board):
        pos_x = self.pos_x 
        pos_y = self.pos_y


        # check if fields in between are not covered by other pieces
        if (self.rochade_allowed 
                and  "--" == board[pos_x+1][pos_y].name 
                and  "--" == board[pos_x+2][pos_y].name
                and "R" in board[7][pos_y].name):

            board[pos_x+1][pos_y] = Crossed_P()
            board[pos_x+2][pos_y] = Crossed_P()
        return 0





