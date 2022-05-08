class Piece:
    def __init__(self, name, color, abbrev):
        self.name = name
        self.color = color
        self.abbrev = abbrev

    def print(self):
        print(self.name, self.color, self.pos)
