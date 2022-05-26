from pieces.bishop import Bishop
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.pawn_b import Pawn_B
from pieces.pawn_w import Pawn_W
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.king import King
from pieces.empty_p import Empty_P


class Board():

    def __init__(self) :
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
        board[4][0] = King("KW", "W", 4,0)
        board[4][7] = King("KB", "B", 4,7)

        #init queens
        board[3][0] = Queen("QW", "W", 3, 0)
        board[3][7] = Queen("QB", "B", 3, 7)

        #init Bishop
        board[2][0] = Bishop("BW", "W", 2, 0)
        board[5][0] = Bishop("BW", "W", 5, 0)
        board[2][7] = Bishop("BB", "B", 2, 7)
        board[5][7] = Bishop("BB", "B", 5, 7)

        #init Knights
        board[1][0] = Knight("KW", "W", 1,0)
        board[6][0] = Knight("KW", "W", 6,0)
        board[1][7] = Knight("KB", "B", 1,7)
        board[6][7] = Knight("KB", "B", 6,7)


        #init rooks
        board[0][0] = Rook("RW", "W", 0,0)
        board[7][0] = Rook("RW", "W", 7,0)
        board[0][7] = Rook("RB", "B", 0,7)
        board[7][7] = Rook("RB", "B", 7,7)

        #init white pawns
        for pos_x in range(8):
            board[pos_x][1] = Pawn_W("PW", pos_x,1)

       #init black pawns
        for pos_x in range(8):
            board[pos_x][6] = Pawn_B("PB", pos_x,6)

        return board


    def print(self):
        for x in reversed(range(8)):
            for row in (self.board):
                print(str(row[x].name) + "|", end ='')
            print("")
        return 0

    def insert(self, piece):
        if self.board[piece.pos_x][piece.pos_y].name == "--":
            self.board[piece.pos_x][piece.pos_y] = piece 
        else:
            print("")
            print("There is already another pieces")
            print("")
        return self.board

    def check_for_field(self, pos_x, pos_y):
        if (self.board[pos_x][pos_y]).name!= "--":
            self.board[pos_x][pos_y].check(self.board)

        return self.board

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
