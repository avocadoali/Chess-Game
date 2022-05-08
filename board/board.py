class Board:

    def __init__(self) :
        self.board = self.make_board()

    def make_board(self):
        board = []
        for r in range(8):
            row = []
            for c in range(8):
                row.append(["--",])

            board.append(row)

        #init with pawns
        count = 1
        for col in range(8):
            board[col][1] = ["PW", count]
            count += 1 

        count = 1
        for col in range(8):
            board[col][6] = ["PB",count]
            count += 1

        #init kings
        board[4][0] = ["KW",1]
        board[4][7] = ["KW",1]

        #init queens
        board[3][0] = ["QW",1]
        board[3][7] = ["QW",1]
 
        #init Bishop 
        board[2][0] = ["BW",1]
        board[5][0] = ["BW",2]
        board[2][7] = ["BB",1]
        board[5][7] = ["BB",2]

        #init Knights
        board[1][0] = ["KW",1]
        board[6][0] = ["KW",2]
        board[1][7] = ["KB",1]
        board[6][7] = ["KB",2]
 
 
        #init rooks
        board[0][0] = ["RW",1]
        board[7][0] = ["RW",2]
        board[0][7] = ["RB",1]
        board[7][7] = ["RB",2]
        return board 


    def print(self):
        for x in reversed(range(8)):
            print("|", end="")
            for r in (self.board):
                print(str(r[x][0]) + "|", end ='')
            print("")

# board[0][0] - unten links
# board[7][7] - oben rechts 
# board y  x 

#|70|71|72|73|74|75|76|77|
#|60|61|62|63|64|65|66|67|
#|50|51|52|53|54|55|56|57|
#|40|41|42|43|44|45|46|47|
#|30|31|32|33|34|35|36|37|
#|20|21|22|23|24|25|26|27|
#|10|11|12|13|14|15|16|17|
#|00|01|02|03|04|05|06|07|