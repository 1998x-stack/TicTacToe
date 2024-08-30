import unittest
from src.player import Player
from src.cgameboard import GameBoard
from src.gamestate import GameState

class TestGameState(unittest.TestCase):
    """Unit tests for the GameState class."""

    def setUp(self) -> None:
        """Set up a new GameState instance with two players and a GameBoard for each test."""
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.board = GameBoard()
        self.game_state = GameState(self.player_x, self.player_o)

    def test_initial_state(self):
        """Test the initial state of the GameState."""
        self.assertFalse(self.game_state.game_over)
        self.assertEqual(self.game_state.current_player, self.player_x)

    def test_switch_player(self):
        """Test that the switch_player method correctly switches the current player."""
        self.assertEqual(self.game_state.current_player, self.player_x)
        self.game_state.switch_player()
        self.assertEqual(self.game_state.current_player, self.player_o)
        self.game_state.switch_player()
        self.assertEqual(self.game_state.current_player, self.player_x)

    def test_check_game_over_with_winner(self):
        """Test that check_game_over correctly identifies a winner."""
        # Simulate a winning condition for player X
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(0, 1, 'X')
        self.board.mark_cell(0, 2, 'X')
        winner = self.game_state.check_game_over(self.board)
        self.assertEqual(winner, 'X')
        self.assertTrue(self.game_state.game_over)

    def test_check_game_over_with_draw(self):
        """Test that check_game_over correctly identifies a draw."""
        # Fill the board with no winners
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'X'), (1, 1, 'O'), (1, 2, 'X'),
            (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'O'),
        ]
        for row, col, symbol in moves:
            self.board.mark_cell(row, col, symbol)
        
        winner = self.game_state.check_game_over(self.board)
        self.assertIsNone(winner)
        self.assertTrue(self.game_state.game_over)

    def test_check_game_over_still_ongoing(self):
        """Test that check_game_over returns None when the game is still ongoing."""
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(1, 1, 'O')
        winner = self.game_state.check_game_over(self.board)
        self.assertIsNone(winner)
        self.assertFalse(self.game_state.game_over)

    def test_switch_player_does_not_change_game_over(self):
        """Test that switching players does not reset the game_over flag."""
        # Simulate a game that has already ended
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(0, 1, 'X')
        self.board.mark_cell(0, 2, 'X')
        self.game_state.check_game_over(self.board)
        self.assertTrue(self.game_state.game_over)
        
        # Switch players
        self.game_state.switch_player()
        
        # The game should still be over
        self.assertTrue(self.game_state.game_over)
        self.assertEqual(self.game_state.current_player, self.player_o)

if __name__ == '__main__':
    unittest.main()