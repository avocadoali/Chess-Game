from game_logic.empty_p import Empty_P


class Board:

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

        #init with pawns
#        count = 1
#        for col in range(8):
#            board[col][1] = ["PW", count]
#            count += 1
#
#        count = 1
#        for col in range(8):
#            board[col][6] = ["PB",count]
#            count += 1
#
#        #init kings
#        board[4][0] = ["KW",1]
#        board[4][7] = ["KW",1]
#
#        #init queens
#        board[3][0] = ["QW",1]
#        board[3][7] = ["QW",1]
#
#        #init Bishop
#        board[2][0] = ["BW",1]
#        board[5][0] = ["BW",2]
#        board[2][7] = ["BB",1]
#        board[5][7] = ["BB",2]
#
#        #init Knights
#        board[1][0] = ["KW",1]
#        board[6][0] = ["KW",2]
#        board[1][7] = ["KB",1]
#        board[6][7] = ["KB",2]
#
#
#        #init rooks
#        board[0][0] = ["RW",1]
#        board[7][0] = ["RW",2]
#        board[0][7] = ["RB",1]
#        board[7][7] = ["RB",2]
        return board 


    def print(self):
        for x in reversed(range(8)):
            for row in (self.board):
                print(str(row[x].abbrev) + "|", end ='')
            print("")

    def insert(self, piece):
        if self.board[piece.pos_x][piece.pos_y].abbrev == "--":
            self.board[piece.pos_x][piece.pos_y] = piece 
        else:
            print("")
            print("")
            print("Kannt da keine Figue einfügen")
            print("")
            print("")
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
