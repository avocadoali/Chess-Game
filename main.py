from board.board import Board
from game_logic.pawn import Pawn
from game_logic.piece import Piece



def main():
    first_pawn = Pawn("1", "Black", {1,0})
    test = Board()
    test.print()
    

    
if __name__ == "__main__":
    main()