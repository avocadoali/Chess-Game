from game_logic.pawn import Pawn



def main():
    print("Start the game")

    myPawn = Pawn("hi", "black", {1,1})
    
    myPawn.print()

if __name__ == "__main__":
    main()