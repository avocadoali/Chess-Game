from board.board import Board
from game_logic.pawn import Pawn
from game_logic.piece import Piece



def main():
    first_pawn = Pawn("1", "Black", {1,0})
    test = Board()
    test.print()

    for row in reversed(range(8)):
            print("|", end = '')
            for col in (range(8)):
                print(str(col) + str(row)  + "|", end = '')
            print("")
   
    
if __name__ == "__main__":
    main()