from board import Board
from game_logic.pawn import Pawn
from game_logic.piece import Piece
from game_logic.rook import Rook


def main():

    board = Board()
    e_board = Board()

    newrook2 = Rook( "RW", "W", 0, 5)

    newrook = Rook( "RB", "B", 0, 2 )

    board.insert(newrook)
    board.insert(newrook2)
    board.print()

    board.check_for_field(0,5)

#    newrook2.put(board.board)
#    newrook.put(board.board)
#    
#    board.print()
#    
#    e_board.board = copy.deepcopy(board.board)
#    
#    newrook.check_up(newrook.color, 8, e_board.board)
#
#    newrook.check_down(0,3,newrook.color, 8, e_board.board)
#
#    print("")
#    e_board.print()



if __name__ == "__main__":
    main()