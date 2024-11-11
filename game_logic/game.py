import random
from game_logic.tile import Tile
from game_logic.board import Board
from game_logic.deck import Deck

class Game:
    def __init__(self):
        self.board = Board()
        self.deck = Deck()
        self.players = ['human', 'AI']
        self.turn = 0
        self.current_player = self.players[self.turn]
        self.human_hand = []
        self.ai_hand = []

        # Deal 7 tiles to each player
        self.deal_tiles()

    def deal_tiles(self):
        """Deal 7 tiles to each player."""
        for _ in range(7):
            self.human_hand.append(self.deck.draw())
            self.ai_hand.append(self.deck.draw())

    def player_turn(self, player, tile=None, end=None):
        """Handle a player's turn."""
        if player == 'human':
            # Human places the tile manually (assume tile and end are provided)
            if tile and end:
                self.board.add_tile(tile, end)
                self.human_hand.remove(tile)
        elif player == 'AI':
            # AI makes a decision based on available tiles
            tile = self.ai_decision()
            end = 'right'  # For simplicity, let's always place on the right side for now
            if tile:
                self.board.add_tile(tile, end)
                self.ai_hand.remove(tile)

    def ai_decision(self):
        """AI selects a tile to play (random for now)."""
        possible_tiles = [tile for tile in self.ai_hand if self.can_play(tile)]
        if not possible_tiles:
            return None  # No valid move for the AI
        return random.choice(possible_tiles)  # Randomly select a valid tile

    def can_play(self, tile):
        """Check if a tile can be placed on the board."""
        return tile.matches(self.board.ends[0]) or tile.matches(self.board.ends[1])

    def game_over(self):
        """Check if the game is over."""
        if not self.human_hand or not self.ai_hand:  # No more tiles for any player
            return True
        if not self.deck.tiles and all(self.can_play(tile) is False for tile in self.human_hand + self.ai_hand):
            return True  # No valid moves left
        return False

    def switch_turn(self):
        """Switch to the next player's turn."""
        self.turn = (self.turn + 1) % len(self.players)
        self.current_player = self.players[self.turn]

    def play_game(self):
        """Play the game until someone wins."""
        while not self.game_over():
            print(f"Turn: {self.current_player}")
            if self.current_player == 'human':
                print(f"Your hand: {[str(tile) for tile in self.human_hand]}")
                # For simplicity, the human chooses the first tile and the right end
                tile = self.human_hand[0]
                self.player_turn('human', tile, 'right')
            else:
                self.player_turn('AI')

            print(f"Board: {self.board.display()}")
            self.switch_turn()

        if not self.human_hand:
            print("Human wins!")
        elif not self.ai_hand:
            print("AI wins!")
        else:
            print("It's a draw!")
