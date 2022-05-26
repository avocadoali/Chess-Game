from pieces.piece import Piece
from pieces.crossed_p import Crossed_P

import copy

class Knight(Piece):
    def __init__(self, name, color, pos_x, pos_y):
        super().__init__(name, color, pos_x, pos_y)


    def check(self, board):
        e_board = Board()
        e_board.board = copy.deepcopy(board)
        self.check_right_up(e_board.board)
        self.check_left_up(e_board.board)
        self.check_right_down(e_board.board)
        self.check_left_down(e_board.board)

        self.check_up_right(e_board.board)
        self.check_up_left(e_board.board)
        self.check_down_right(e_board.board)
        self.check_down_left(e_board.board)
        print("")
        e_board.print()
        return e_board

    def check_right_up(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x + 2
        
        if pos_y<=7 and pos_x <= 7 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_left_up(self, board):
        pos_y = self.pos_y + 1
        pos_x = self.pos_x - 2
        
        if pos_y<=7 and pos_x >= 0 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_right_down(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x + 2
        
        if pos_y >= 0 and pos_x <= 7 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_left_down(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x - 2
        
        if pos_y >= 0 and pos_x >= 0 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_up_right(self, board):
        pos_y = self.pos_y + 2 
        pos_x = self.pos_x + 1
        
        if pos_y<=7 and pos_x <= 7 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_up_left(self, board):
        pos_y = self.pos_y + 2 
        pos_x = self.pos_x - 1
        
        if pos_y <= 7 and pos_x >= 0 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_down_right(self, board):
        pos_y = self.pos_y - 2 
        pos_x = self.pos_x + 1
        
        if pos_y>=0 and pos_x <= 7 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

    def check_down_left(self, board):
        pos_y = self.pos_y - 2 
        pos_x = self.pos_x - 1
        
        if pos_y>=0 and pos_x>=0 and self.color != board[pos_x][pos_y].color:
            board[pos_x][pos_y] = Crossed_P()
        return 0 

