class Piece:
    def __init__(self, name, color, abbrev, pos_x, pos_y):
        self.name = name
        self.color = color
        self.abbrev = abbrev
        self.pos_x= pos_x 
        self.pos_y= pos_y 

    def print(self):
        print(self.name, self.color, self.pos)
