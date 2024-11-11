# game_logic/tile.py
class Tile:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __repr__(self):
        return f"({self.side1}|{self.side2})"

    def is_double(self):
        return self.side1 == self.side2

    def matches(self, number):
        return self.side1 == number or self.side2 == number
