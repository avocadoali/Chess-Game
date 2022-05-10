
from game_logic.piece import Piece


class Rook(Piece):
    def __init__(self, name, color, abbrev, pos_x, pos_y):
        super().__init__(name, color, abbrev, pos_x, pos_y)

    def check_up(self, pos_x, pos_y, color, maxsteps, board):
        pos_y += 1
        while (pos_y <= 7 and not (color in board[pos_x][pos_y]["name"])):
            if board[pos_x][pos_y]["name"] != "--":
                board[pos_x][pos_y]["name"] = "XX"
                break

            board[pos_x][pos_y]["name"] = "XX"
            
            try:
                board[pos_x][pos_y+1]["name"] != "--"
            except:
                break
            pos_y = pos_y + 1
        return 0

    def check_down(self, pos_x, pos_y, color, maxsteps, board):
        pos_y -= 1
        while (pos_y >= 0 and not (color in board[pos_x][pos_y]["name"])):
            if board[pos_x][pos_y]["name"] != "--":
                board[pos_x][pos_y]["name"] = "XX"
                break

            board[pos_x][pos_y]["name"] = "XX"
            
            try:
                board[pos_x][pos_y-1]["name"] != "--"
            except:
                break
            pos_y -= 1
        return 0
    



   
