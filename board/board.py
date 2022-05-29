from pieces.bishop import Bishop
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.pawn_b import Pawn_B
from pieces.pawn_w import Pawn_W
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.king import King
from pieces.empty_p import Empty_P

import copy

class Board():

    def __init__(self) :
        self.black_p = [King("KB", "B", 4,7),
            Queen("QB", "B", 3, 7),
            Bishop("BB", "B", 2, 7),
            Bishop("BB", "B", 5, 7),
            Knight("kB", "B", 1,7),
            Knight("kB", "B", 6,7),
            Rook("RB", "B", 0,7),
            Rook("RB", "B", 7,7)]

        self.white_p = [ King("KW", "W", 4,0),
            Queen("QW", "W", 3, 0),
            Bishop("BW", "W", 2, 0),
            Bishop("BW", "W", 5, 0),
            Knight("kW", "W", 1,0),
            Knight("kW", "W", 6,0),
            Rook("RW", "W", 0,0)  ,
            Rook("RW", "W", 7,0)  ,

        ]

        self.board = self.make_board()

    def make_board(self):
        board = []
        empty_piece = Empty_P()
        for r in range(8):
            row = []
            for c in range(8):
                row.append(empty_piece)

            board.append(row)

        #init kings
        board[4][0] = self.white_p[0]
        board[4][7] = self.black_p[0]

        #init queens
        board[3][0] = self.white_p[1]
        board[3][7] = self.black_p[1]

        #init Bishop
        board[2][0] = self.white_p[2]
        board[5][0] = self.white_p[3]
        board[2][7] = self.black_p[2]
        board[5][7] = self.black_p[3]

        #init Knights
        board[1][0] = self.white_p[4]
        board[6][0] = self.white_p[5]
        board[1][7] = self.black_p[4]
        board[6][7] = self.black_p[5]

        #init rooks
        board[0][0] = self.white_p[6]
        board[7][0] = self.white_p[7]
        board[0][7] = self.black_p[6]
        board[7][7] = self.black_p[7]

        #init white pawns
        for pos_x in range(8):
            self.white_p.append(Pawn_W("PW", pos_x,1))
            board[pos_x][1] = self.white_p[8+pos_x]

       #init black pawns
        for pos_x in range(8):
            self.black_p.append(Pawn_B("PB", pos_x,6))
            board[pos_x][6] = self.black_p[8+pos_x]

        return board


    #print the board
    def print(self):
        for x in reversed(range(8)):
            for row in (self.board):
                print(str(row[x].name) + "|", end ='')
            print("")
        return 0

    #insert a piece into the board
    def insert(self, piece):
        if self.board[piece.pos_x][piece.pos_y].name == "--":
            self.board[piece.pos_x][piece.pos_y] = piece 
        else:
            print("There is already another pieces")

        return self.board


    #check allowed move if there is a piece on that field
    def check_for_field(self, pos_x, pos_y):
        checked_board = Board()
        if (self.board[pos_x][pos_y]).name!= "--":
            checked_board = (self.board[pos_x][pos_y].check(self.board))

        return checked_board

    #shows if the king of specific color is currently checked
    def is_checked(self, color ):

        if color == "B":
            checked_board = self.all_moves("W")

            # check if black king is attacked(checked)
            KB_pos_x = self.black_p[0].pos_x
            KB_pos_y = self.black_p[0].pos_y

            return checked_board.board[KB_pos_x][KB_pos_y].name == "XX"

        else:
            checked_board = self.all_moves("B")

            # check if white king is attacked(checked)
            KW_pos_x = self.white_p[0].pos_x
            KW_pos_y = self.white_p[0].pos_y

            return checked_board.board[KW_pos_x][KW_pos_y].name == "XX"

    def check_for_field_b(self, pos_x, pos_y, b):
        checked_board = Board()
        checked_board.board = copy.deepcopy(b)
        if (checked_board.board[pos_x][pos_y]).name!= "--":
            checked_board = (checked_board.board[pos_x][pos_y].check(checked_board.board))

        return checked_board

    #check allowed move if there is a piece on that field
    #but with external board
    def legal_moves(self, pos_x, pos_y, b):
        checked_board = Board()
        checked_board.board = copy.deepcopy(b)

        if self.board[pos_x][pos_y].name!= "--":
            checked_board = self.board[pos_x][pos_y].check(checked_board.board)

        color = self.board[pos_x][pos_y].color

        for x in range(8):
            for y in range(8):
                if "X" in checked_board.board[x][y].name:
                    #make move
                    self.move_from_to(color, pos_x,pos_y, x,y)
                    #check if is checked
                    if self.is_checked(color):
                        checked_board.board[x][y] = Empty_P()
                        return checked_board
                    #undo move
                    self.move_from_to(color, x,y,pos_x,pos_y)

        return checked_board


    # move a piece from in field to another
    def move_from_to(self, color, x, y, to_x, to_y):

        # init temporary board
        checked_board = self.check_for_field(x, y)

        # check piece to be moved is the right color
        if self.board[x][y].color != color:
            print("Piece is not allowed")

            return self.board

            # check if field to move to is marked as allowed field
        if "X" in checked_board.board[to_x][to_y].name:
            #print("Move is allowed")

            #get piece that has to be moved and set its new position
            piece = self.board[x][y]
            piece.pos_x = to_x
            piece.pos_y = to_y

            #remove piece if it was taken
            dest_piece = self.board[to_x][to_y]
            if dest_piece.name != "--":
                self.rm_piece(dest_piece)

            #set original field to empty field
            self.board[to_x][to_y] = piece
            self.board[x][y] = Empty_P()


            # remove piece if en passant takes place
            if "E" in checked_board.board[to_x][to_y].name:
                if color == "W":
                    #remove piece from list
                    dest_piece = self.board[to_x][to_y-1]
                    self.rm_piece(dest_piece)

                    #set field to empty
                    self.board[to_x][to_y-1] = Empty_P()
                else:
                    #remove piece from list
                    dest_piece = self.board[to_x][to_y+1]
                    self.rm_piece(dest_piece)

                    #set field to empty
                    self.board[to_x][to_y+1] = Empty_P()

        else:
            print("Move is not allowed")

        return self.board

    #remove a piece from the pieces list
    def rm_piece(self, dest_piece):

        #check which color the piece is
        if dest_piece.color == "W":

            #index of piece to be removed
            index = 0

            #search for the right piece object in list by position
            for p in self.white_p:
                if p.pos_x == dest_piece.pos_x and p.pos_y == dest_piece.pos_y:
                    break
                index = index + 1

            #remove piece by index
            del self.white_p[index]


        else:

            #index of piece to be removed
            index = 0

            #search for the right piece object in list by position
            for p in self.black_p:
                if p.pos_x == dest_piece.pos_x and p.pos_y == dest_piece.pos_y:
                    break
                index = index + 1

            #remove piece by index
            del self.black_p[index]

        return 0

    #shows if the king of specific color is currently checked
    def is_checked(self, color ):

        if color == "B":
            checked_board = self.all_moves("W")
            # check if black king is attacked(checked)
            KB_pos_x = self.black_p[0].pos_x
            KB_pos_y = self.black_p[0].pos_y

            return checked_board.board[KB_pos_x][KB_pos_y].name == "XX"

        else:
            checked_board = self.all_moves("B")

            # check if white king is attacked(checked)
            KW_pos_x = self.white_p[0].pos_x
            KW_pos_y = self.white_p[0].pos_y

            return checked_board.board[KW_pos_x][KW_pos_y].name == "XX"

    #marks another board with all the legal move of specific color
    def all_moves(self, color):

        # init temporary board
        checked_board = Board()
        checked_board.board = copy.deepcopy(self.board)

        # decides which color should be checked
        if color == "W":
            # iterate through all pieces an check for all valid moves
            for piece in self.white_p:
                x = piece.pos_x
                y = piece.pos_y
                checked_board = self.check_for_field_b(x, y,checked_board.board)

            return checked_board

        else:
            # iterate through all pieces an check for all valid moves
            for piece in self.black_p:
                x = piece.pos_x
                y = piece.pos_y
                checked_board = self.check_for_field_b(x, y,checked_board.board)
            return checked_board

        return checked_board
