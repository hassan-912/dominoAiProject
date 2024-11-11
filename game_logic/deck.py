# game_logic/deck.py
from game_logic.tile import Tile
import random

class Deck:
    def __init__(self):
        self.tiles = [Tile(i, j) for i in range(7) for j in range(i, 7)]
        random.shuffle(self.tiles)

    def draw_tile(self):
        return self.tiles.pop() if self.tiles else None
