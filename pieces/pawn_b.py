
from pieces.crossed_p import Crossed_P
from pieces.piece import Piece

import copy

class Pawn_B (Piece):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(name, "B", pos_x, pos_y)
        self.en_passant = True

    
    def check(self, board):
        e_board = Board()
        e_board.board = copy.deepcopy(board)

        self.check_down(e_board.board)
        self.check_down_right(e_board.board)
        self.check_down_left(e_board.board)
        self.check_en_passant_down_right(e_board.board)
        self.check_en_passant_down_left(e_board.board)

        print("")
        e_board.print()
        return e_board

    def check_down(self, board):
        steps = False
                # Check if pawn is in front row
        # for double steps on the first move
        if self.pos_y == 1:
            steps = True

        pos_y = self.pos_y
        pos_x = self.pos_x
        crossed_piece = Crossed_P()

        # Check if one step foward is possible
        if pos_y-1 >= 0 and board[pos_x][pos_y-1].name == "--":
            board[pos_x][pos_y-1] = crossed_piece

            # Check if second step foward is possible
            if steps and pos_y-2 >= 0 and board[pos_x][pos_y-2].name == "--":
                board[pos_x][pos_y-2] = crossed_piece

        return 0 


    def check_down_right(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x + 1

        if (pos_y >= 0 and pos_x <= 7
                and board[pos_x][pos_y].name != "--"
                and self.color != board[pos_x][pos_y].color):

            board[pos_x][pos_y] = Crossed_P()

        return 0

    def check_down_left(self, board):
        pos_y = self.pos_y - 1
        pos_x = self.pos_x - 1

        if (pos_y >= 0
                and pos_x >= 0
                and board[pos_x][pos_y].name != "--"
                and self.color != board[pos_x][pos_y].color):

            board[pos_x][pos_y] = Crossed_P()

        return 0

    def check_en_passant_down_right(self, board):
        pos_y = self.pos_y
        pos_x = self.pos_x + 1

        if (pos_y == 3
                and "P" in board[pos_x][pos_y].name
                and board[pos_x][pos_y].en_passant
                and self.color != board[pos_x][pos_y].color):

            board[pos_x][pos_y-1] = Crossed_P()

        return 0


    def check_en_passant_down_left(self, board):
        pos_y = self.pos_y
        pos_x = self.pos_x - 1

        if (pos_y == 3
                and "P" in board[pos_x][self.pos_y].name
                and board[pos_x][pos_y].en_passant
                and self.color != board[pos_x][pos_y].color):

            board[pos_x][pos_y-1] = Crossed_P()


        return 0
