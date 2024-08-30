import unittest
import pygame
from src.gameboard import GameBoard

class TestGameBoard(unittest.TestCase):
    """Unit tests for the GameBoard class."""

    def setUp(self) -> None:
        """Set up a new GameBoard instance for each test."""
        pygame.init()
        self.board = GameBoard()

    def tearDown(self) -> None:
        """Clean up after each test."""
        pygame.quit()

    def test_initial_state(self):
        """Test that the initial state of the board is empty."""
        for row in self.board.grid:
            self.assertEqual(row, [None, None, None])

    def test_mark_cell(self):
        """Test marking cells on the board."""
        success = self.board.mark_cell(0, 0, 'X')
        self.assertTrue(success)
        self.assertEqual(self.board.grid[0][0], 'X')

        success = self.board.mark_cell(0, 0, 'O')
        self.assertFalse(success)  # Cell already marked, should return False

    def test_mark_cell_out_of_bounds(self):
        """Test marking a cell that is out of bounds."""
        with self.assertRaises(ValueError):
            self.board.mark_cell(3, 3, 'X')

        with self.assertRaises(ValueError):
            self.board.mark_cell(-1, 0, 'X')

    def test_check_winner_row(self):
        """Test checking for a winner in a row."""
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(0, 1, 'X')
        self.board.mark_cell(0, 2, 'X')
        winner = self.board.check_winner()
        self.assertEqual(winner, 'X')

    def test_check_winner_column(self):
        """Test checking for a winner in a column."""
        self.board.mark_cell(0, 0, 'O')
        self.board.mark_cell(1, 0, 'O')
        self.board.mark_cell(2, 0, 'O')
        winner = self.board.check_winner()
        self.assertEqual(winner, 'O')

    def test_check_winner_diagonal(self):
        """Test checking for a winner in a diagonal."""
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(1, 1, 'X')
        self.board.mark_cell(2, 2, 'X')
        winner = self.board.check_winner()
        self.assertEqual(winner, 'X')

        # Test the other diagonal
        self.board.reset()
        self.board.mark_cell(0, 2, 'O')
        self.board.mark_cell(1, 1, 'O')
        self.board.mark_cell(2, 0, 'O')
        winner = self.board.check_winner()
        self.assertEqual(winner, 'O')

    def test_no_winner(self):
        """Test that there is no winner when the board is partially filled."""
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(0, 1, 'O')
        self.board.mark_cell(0, 2, 'X')
        winner = self.board.check_winner()
        self.assertIsNone(winner)

    def test_is_full(self):
        """Test checking if the board is full."""
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'O'), (1, 1, 'X'), (1, 2, 'O'),
            (2, 0, 'X'), (2, 1, 'O'), (2, 2, 'X'),
        ]
        for row, col, symbol in moves:
            self.board.mark_cell(row, col, symbol)
        
        self.assertTrue(self.board.is_full())

    def test_reset(self):
        """Test resetting the board."""
        self.board.mark_cell(0, 0, 'X')
        self.board.reset()
        for row in self.board.grid:
            self.assertEqual(row, [None, None, None])

if __name__ == '__main__':
    unittest.main()
