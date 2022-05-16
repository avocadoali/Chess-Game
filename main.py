from game_logic.board import Board
from game_logic.bishop import Bishop
from game_logic.pawn import Pawn
from game_logic.piece import Piece
from game_logic.queen import Queen
from game_logic.rook import Rook
from game_logic.knight import Knight


def main():

    board = Board()

    knight =  Knight( "BW", "W", 3, 6)
    board.insert(knight)
    newrook2 = Rook( "AA", "B", 4, 7)
    board.insert(newrook2)
    board.print()    
    board.check_for_field(3,6)


    #queen = Queen( "BW", "W", 3, 5)
    #board.insert(queen)
    #newrook2 = Rook( "AA", "W", 5, 7)
    #board.insert(newrook2)
    #board.print()
    #board.check_for_field(3,5)

    #bishop1 = Bishop( "BW", "W", 3, 5)
    #newrook2 = Rook( "AA", "B", 5, 7)
    #newrook = Rook( "RB", "B", 7, 1 )
    #board.insert(newrook)
    #board.insert(newrook2)
    #board.insert(bishop1)
    #board.print()
    #board.check_for_field(3,5)


    #newrook2 = Rook( "AA", "W", 3, 5)
    #newrook = Rook( "RB", "W", 5, 5 )
    #newrook3 = Rook( "RB", "W", 3, 6 )
    #newrook4 = Rook( "RB", "B", 6, 5 )
    #newrook5 = Rook( "RB", "W", 0, 5 )
    #board.insert(newrook)
    #board.insert(newrook2)
    #board.insert(newrook4)
    #board.insert(newrook3)
    #print("")
    #board.print()

    #board.check_for_field(3,5)

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