
from game_logic.piece import Piece


class Rook(Piece):
    def __init__(self, name, color, abbrev):
        super().__init__(name, color, abbrev)

    def up(self, pos_x, pos_y, color, maxsteps, board):
        pos_y += 1
        while (pos_y <= 7 and not (color in board[pos_x][pos_y][0])):
            if board[pos_x][pos_y][0] != "--":
                board[pos_x][pos_y][0] = "XX"
                break

            board[pos_x][pos_y][0] = "XX"
            
            try:
                board[pos_x][pos_y+1][0] != "--"
            except:
                break
            pos_y = pos_y + 1
        
        return 0 