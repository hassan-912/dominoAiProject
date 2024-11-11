from game_logic.game import Game

def test_game_flow():
    game = Game()
    assert len(game.human_hand) == 7  # Human should have 7 tiles
    assert len(game.ai_hand) == 7      # AI should have 7 tiles
    assert len(game.board.played_tiles) == 0  # Board should be empty at the start

    game.play_game()  # Run the game
    assert game.game_over()  # The game should end after the loop

test_game_flow()
