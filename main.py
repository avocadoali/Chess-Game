#from game_logic.game_logic import Game
from board.board import Board

def main():

    b = Board()
    b.print()
    b.move_from_to("W", 1,1 ,1,3)
    print("1")
    b.print()
    b.move_from_to("B", 1,6 ,1,4)
    print("2")
    b.print()
    b.move_from_to("W", 2,1 ,2,3)
    print("3")
    b.print()
    b.move_from_to("B", 1,4 ,2,3)
    print("4")
    b.print()

    print("5")
    b.move_from_to("W", 3,1 ,3,3)
    b.print()

    print("6")
    b.move_from_to("B", 2,3 ,3,2)
    b.print()


    b.check_for_field(3,0)





if __name__ == "__main__":
    main()
