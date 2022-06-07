#from game_logic.game_logic import Game
from board.board import Board
from game_logic.game_logic import Game
from tqdm import tqdm

def main():
    game = Game()

    game.start()
    #b = Board()

    #print("board")
    #b.print()
    #b.move_from_to("W", 4,1,4,3)
    #b.move_from_to("B", 5,6,5,4)
    #b.move_from_to("B", 5,4,4,3)
    #b.move_from_to("W", 3,0,5,2)
    #print("")
    #b.print()

    ##b.all_moves("W").print()
    #print("")
    #b.legal_moves(4,7,b.board).print()


    #print("")
    #print("all moves for black ")
    #test = b.all_moves("B")
    #test.print()


    #b.move_from_to("W", 1,1 ,1,3)
    #print("1")
    #b.print()

    #b.move_from_to("B", 1,6 ,1,4)
    #print("2")
    #b.print()

    #b.move_from_to("W", 2,1 ,2,3)
    #print("3")
    #b.print()

    #b.move_from_to("B", 1,4 ,2,3)
    #print("4")
    #b.print()

    #print("5")
    #b.move_from_to("W", 3,1 ,3,3)
    #b.print()

    #print("6")
    ##b.check_for_field(2,3)
    #b.move_from_to("B", 2,3 ,3,2)
    #b.print()


    #print("7")
    #b.move_from_to("W", 3,0,1,2)
    #b.print()

    #print("8")
    #b.check_for_field(1,2)
    #b.move_from_to("W", 1,2,5,6)
    #b.print()

    #print("9")
    #b.check_for_field(5,6)
    #b.move_from_to("B", 1,7,0,5)
    #b.print()

    #test = b.is_checked("B")
    #print(test)

    #b.print()

    #test = b.legal_moves("B")
    #test.print()

if __name__ == "__main__":
    main()
