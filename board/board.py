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
        self.black_p = [King("GB", "B", 4,7),
            Queen("QB", "B", 3, 7),
            Bishop("BB", "B", 2, 7),
            Bishop("BB", "B", 5, 7),
            Knight("KB", "B", 1,7),
            Knight("KB", "B", 6,7),
            Rook("RB", "B", 0,7),
            Rook("RB", "B", 7,7)]

        self.white_p = [ King("GW", "W", 4,0),
            Queen("QW", "W", 3, 0),
            Bishop("BW", "W", 2, 0),
            Bishop("BW", "W", 5, 0),
            Knight("KW", "W", 1,0),
            Knight("KW", "W", 6,0),
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


    def print(self):
        for x in reversed(range(8)):
            for row in (self.board):
                print(str(row[x].name) + "|", end ='')
            print("")
        return 100

    def insert(self, piece):
        if self.board[piece.pos_x][piece.pos_y].name == "--":
            self.board[piece.pos_x][piece.pos_y] = piece 
        else:
            print("")
            print("There is already another pieces")
            print("")
        return self.board


    def check_for_field(self, pos_x, pos_y):
        checked_board = []
        if (self.board[pos_x][pos_y]).name!= "--":
            checked_board = (self.board[pos_x][pos_y].check(self.board))

        return checked_board

    def move_from_to(self, color, x, y, to_x, to_y):
        checked_board = self.check_for_field(x, y)

        # check piece to be moved is the right color
        if self.board[x][y].color != color:
            print("Piece is not allowed")
            return self.board

        # check if field to move to is marked as allowed field
        if "X" in checked_board.board[to_x][to_y].name:
            print("Move is allowed")

            #get piece that has to be moved and set its new position
            piece = self.board[x][y]
            piece.pos_x = to_x
            piece.pos_y = to_y

            #remove piece if it was taken
            dest_piece = self.board[to_x][to_y]
            if dest_piece.name != "--":
                self.rm_piece(dest_piece)

            self.board[to_x][to_y] = piece
            self.board[x][y] = Empty_P()


            # remove piece if en passant takes place
            if "E" in checked_board.board[to_x][to_y].name:
                print("Enpassent!")
                if color == "W":
                    print("white")

                    #remove piece from list
                    dest_piece = self.board[to_x][to_y-1]
                    self.rm_piece(dest_piece)

                    #set field to empty
                    self.board[to_x][to_y-1] = Empty_P()

                else:
                    print("black")

                    #remove piece from list
                    dest_piece = self.board[to_x][to_y+1]
                    self.rm_piece(dest_piece)
                    #
                    #set field to empty
                    self.board[to_x][to_y+1] = Empty_P()

        else:
            print("Move is not allowed")

        return self.board

    def rm_piece(self, dest_piece):
        if dest_piece.color == "W":
            index = 0
            for p in self.white_p:
                if p.pos_x == dest_piece.pos_x and p.pos_y == dest_piece.pos_y:
                    break
                index = index + 1

            del self.white_p[index]

        else:
            index = 0
            for p in self.black_p:
                if p.pos_x == dest_piece.pos_x and p.pos_y == dest_piece.pos_y:
                    break
                index = index + 1

            del self.black_p[index]

        return 1


    def is_checked(self, color):

        # returne board class
        # nimmt board list

        checked_board = Board()
        checked_board.board = copy.deepcopy(self.board)

        if color == "W":
            for piece in self.white_p:
                x = piece.pos_x
                y = piece.pos_y
                checked_board = self.check_for_field_two(x, y, checked_board.board)
        else:
            for piece in self.black_p:
                x = piece.pos_x
                y = piece.pos_y
                checked_board = self.check_for_field_two(x, y, checked_board.board)

        print("")
        print("")
        print("checked board")
        checked_board.print()


        return checked_board


    def check_for_field_two(self, pos_x, pos_y, board):
        checked_board = board
        if (self.board[pos_x][pos_y]).name!= "--":
            checked_board = self.board[pos_x][pos_y].check(checked_board)

        return checked_board


# board[0][0] - unten links
# board[7][7] - oben rechts 
# board x y

#|07|17|27|37|47|57|67|77|
#|06|16|26|36|46|56|66|76|
#|05|15|25|35|45|55|65|75|
#|04|14|24|34|44|54|64|74|
#|03|13|23|33|43|53|63|73|
#|02|12|22|32|42|52|62|72|
#|01|11|21|31|41|51|61|71|
#|00|10|20|30|40|50|60|70|
#
