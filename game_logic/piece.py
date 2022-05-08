class Piece:
    def __init__(self, name, color, pos, abbrev):
        self.name = name
        self.color = color
        self.pos = pos
        self.abbrev =  abbrev

    def print(self):
        print(self.name, self.color, self.pos)
