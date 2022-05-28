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

    for p in b.white_p:
        print(p.name)
        print(p.pos_x)
        print(p.pos_y)
        print("")


    print("5")
    b.move_from_to("W", 3,1 ,3,3)
    b.print()

    print("6")
    #b.check_for_field(2,3)
    b.move_from_to("B", 2,3 ,3,2)
    b.print()


    b.move_from_to("W", 3,0,1,2)
    b.print()

    b.check_for_field(1,2)
    b.move_from_to("W", 1,2,5,6)
    b.print()

    b.check_for_field(5,6)
    b.move_from_to("B", 1,7,0,5)
    b.print()

    print("Checked")
    b.is_checked("W")

if __name__ == "__main__":
    main()
