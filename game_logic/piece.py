class Piece:
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos

    def print(self):
        print(self.name, self.color, self.pos)
