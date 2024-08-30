import unittest
from src.player import Player
from src.gameboard import GameBoard

class TestPlayer(unittest.TestCase):
    """Unit tests for the Player class."""

    def setUp(self) -> None:
        """Set up a new Player instance and GameBoard for each test."""
        self.board = GameBoard()
        self.player_x = Player('X')
        self.player_o = Player('O')

    def test_player_initialization(self):
        """Test that the player initializes with the correct symbol."""
        self.assertEqual(self.player_x.get_symbol(), 'X')
        self.assertEqual(self.player_o.get_symbol(), 'O')

        with self.assertRaises(ValueError):
            Player('A')  # Invalid symbol should raise ValueError

    def test_player_make_move_success(self):
        """Test that a player can successfully make a move."""
        success = self.player_x.make_move(self.board, 0, 0)
        self.assertTrue(success)
        self.assertEqual(self.board.grid[0][0], 'X')

    def test_player_make_move_failure(self):
        """Test that a player cannot make a move in an occupied cell."""
        self.player_x.make_move(self.board, 0, 0)
        success = self.player_o.make_move(self.board, 0, 0)
        self.assertFalse(success)
        self.assertEqual(self.board.grid[0][0], 'X')  # Should remain 'X'

    def test_player_make_move_out_of_bounds(self):
        """Test that a player cannot make a move outside the board boundaries."""
        with self.assertRaises(ValueError):
            self.player_x.make_move(self.board, 3, 3)  # Out of bounds
        
        with self.assertRaises(ValueError):
            self.player_x.make_move(self.board, -1, 0)  # Out of bounds

    def test_player_get_symbol(self):
        """Test the get_symbol method."""
        self.assertEqual(self.player_x.get_symbol(), 'X')
        self.assertEqual(self.player_o.get_symbol(), 'O')

if __name__ == '__main__':
    unittest.main()