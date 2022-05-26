class Piece:
    def __init__(self, name, color, pos_x, pos_y):
        self.name = name
        self.color = color
        self.pos_x= pos_x 
        self.pos_y= pos_y 

    def print(self):
        print(self.name, self.color, self.pos)
