class Board:

    def __init__(self, pieces) :
        self.board = self.make_board()

    def make_board(self):
        board = []
        for r in range(8):
            row = []
            for c in range(8):
                row.append("--")

            board.append(row)

        #init with pawns
        for col in range(8):
            board[1][col] = "PW"
        for col in range(8):
            board[6][col] = "PB"

        #init kings
        board[0][4] = "KW"
        board[7][4] = "KW"

        #init queens
        board[0][3] = "QW"
        board[7][3] = "QW"
 
        #init Bishop 
        board[0][2] = "BW"
        board[0][5] = "BW"
        board[7][2] = "BB"
        board[7][5] = "BB"
 
        #init Knights
        board[0][1] = "KW"
        board[0][6] = "KW"
        board[7][1] = "KB"
        board[7][6] = "KB"
 
        #init rooks
        board[0][0] = "RW"
        board[0][7] = "RW"
        board[7][0] = "RB"
        board[7][7] = "RB"

        
       
        return board 


    def print(self):
        for row in reversed(self.board):
            print(row)

# board[0][0] - unten links
# board[7][7] - oben rechts 
# board y  x 
