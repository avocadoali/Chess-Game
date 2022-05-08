from board.board import Board
from game_logic.pawn import Pawn
from game_logic.piece import Piece
from game_logic.rook import Rook



def main():
    board = []
    for r in range(8):
        row = []
        for c in range(8):
            row.append(["--",])
        board.append(row)
    
    board[0][3] = ["KB",1]
    
    for x in reversed(range(8)):
            print("|", end="")
            for r in (board):
                print(str(r[x][0]) + "|", end ='')
            print("") 


    print("")
    print(board[0][0][0])
    newrook = Rook("RW1", "W", "RW")
    newrook.up(0,0,newrook.color, 8, board)

    for x in reversed(range(8)):
            print("|", end="")
            for r in (board):
                print(str(r[x][0]) + "|", end ='')
            print("") 



if __name__ == "__main__":
    main()