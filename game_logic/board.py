# game_logic/board.py
from .tile import Tile

class Board:
    def __init__(self):
        self.played_tiles = []  # Keeps track of tiles on the board
        self.ends = []          # Keeps track of the two ends of the board where new tiles can be placed

    def add_tile(self, tile, end):
        """
        Adds a tile to the specified end of the board.
        'end' should be either 'left' or 'right'.
        """
        if not self.played_tiles:
            # First tile to be placed
            self.played_tiles.append(tile)
            self.ends = [tile.side1, tile.side2]
        else:
            if end == 'left' and tile.matches(self.ends[0]):
                self.played_tiles.insert(0, tile)
                self.ends[0] = tile.side1 if tile.side2 == self.ends[0] else tile.side2
            elif end == 'right' and tile.matches(self.ends[1]):
                self.played_tiles.append(tile)
                self.ends[1] = tile.side1 if tile.side2 == self.ends[1] else tile.side2
            else:
                raise ValueError("The tile does not match the board ends.")

    def display(self):
        """Displays the current state of the board."""
        return " - ".join(str(tile) for tile in self.played_tiles)
