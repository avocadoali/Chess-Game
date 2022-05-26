from board.board import Board
from pieces.bishop import Bishop
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.pawn_b import Pawn_B
from pieces.pawn_w import Pawn_W
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.king import King


def main():
    board = Board()
    board.print()
    board.check_for_field(4,1)


    #king= King( "KW", "W", 4, 0)
    #board.insert(king)
    ##newrook2 = Rook( "RB", "B", 7, 0)
    ## board.insert(newrook2)

    #pawn2 = Pawn_W( "PW", "B", 2, 6)
    #board.insert(pawn2)
    #newrook3 = Rook( "RB", "B", 0, 0)
    #board.insert(newrook3)
    #board.print()
    #board.check_for_field(4,0)



    #pawn1 = Pawn_B( "PB", 3, 3)
    #board.insert(pawn1)
    #pawn2 = Pawn_W ( "PB", 4, 3)
    #board.insert(pawn2)
    #pawn3 = Pawn_W ( "PB", 2, 3)
    #board.insert(pawn3)
    #newrook3 = Rook( "RB", "B", 1, 4)
    #board.insert(newrook3)
    #board.print()
    #board.check_for_field(3,3)


    #knight =  Knight( "BW", "W", 3, 6)
    #board.insert(knight)
    #newrook2 = Rook( "AA", "B", 4, 7)
    #board.insert(newrook2)
    #board.print()    
    #board.check_for_field(3,6)


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
