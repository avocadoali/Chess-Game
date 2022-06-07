from board.board import Board

class Game():

    def __init__(self, ):
        self.board = Board()
        self.current_player = "W"


    def start(self):
        checkmate = False




        while (not checkmate):
            # print Board
            print("Player: " + self.current_player)
            self.board.print()
            print("")

            # ask what field user wants to play
            from_pos = input("Enter field coordinates(x,y):")

            # input to number[0] number[1]
            numbers = [int(x) for x in from_pos.split() if x.isnumeric()]
            print("")

            #check ic format is correct
            if len != 2 and not (numbers[0] >= 0 and numbers[0] <= 7 and numbers[1] >= 0 and numbers[1] <= 7):
                print("")
                print("Wrong coordinates")
                p = input("Enter field coordinates(x,y):")
                numbers = [int(x) for x in p.split() if x.isnumeric()]
                print("")

            x = numbers[0]
            y = numbers[1]

            print("")
            self.board.check_for_field(x,y).print()

            to_pos = input ("Enter field coordinates(x,y)")

            numbers = [int(x) for x in to_pos.split() if x.isnumeric()]
            print("")

            #check ic format is correct
            if len != 2 and not (numbers[0] >= 0 and numbers[0] <= 7 and numbers[1] >= 0 and numbers[1] <= 7):
                print("")
                print(numbers)
                print("Wrong")
                p = input("Enter field coordinates(x,y)")
                numbers = [int(x) for x in p.split() if x.isnumeric()]
                print("")


            to_x = numbers[0]
            to_y = numbers[1]

            print( x, y, to_x, to_y )

            #move piece
            self.board.move_from_to(self.current_player , x,y, to_x, to_y)


            # switch player
            if self.current_player == "W":
                self.current_player = "B"
            else:
                self.current_player = "W"

        return 0


    def print(self):
        self.board.print()
        return 0




    def check_legal_moves_left():
        return 0
