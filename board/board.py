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
            board[1][col] = ["PW", count]
            count += 1 

        count = 1
        for col in range(8):
            board[6][col] = ["PB",count]
            count += 1

        #init kings
        board[0][4] = ["KW",1]
        board[7][4] = ["KW",1]

        #init queens
        board[0][3] = ["QW",1]
        board[7][3] = ["QW",1]
 
        #init Bishop 
        board[0][2] = ["BW",1]
        board[0][5] = ["BW",2]
        board[7][2] = ["BB",1]
        board[7][5] = ["BB",2]
 
        #init Knights
        board[0][1] = ["KW",1]
        board[0][6] = ["KW",2]
        board[7][1] = ["KB",1]
        board[7][6] = ["KB",2]
 
        #init rooks
        board[0][0] = ["RW",1]
        board[0][7] = ["RW",2]
        board[7][0] = ["RB",1]
        board[7][7] = ["RB",2]
        return board 


    def print(self):
        for row in reversed(self.board):
            print("|", end = '')

            for col in row:
                print(col[0] + "|", end = '')
            print("")

# board[0][0] - unten links
# board[7][7] - oben rechts 
# board y  x 
