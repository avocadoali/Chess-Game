#from game_logic.game_logic import Game
from board.board import Board

def main():

    b = Board()
    b.print()
    b.move_from_to("W", 1,1,1,2)
    b.print()




if __name__ == "__main__":
    main()
