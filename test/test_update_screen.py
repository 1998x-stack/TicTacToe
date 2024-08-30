import unittest
from unittest.mock import MagicMock, patch
import pygame
from src.gameboard import GameBoard
from src.update_screen import update_screen

class TestUpdateScreen(unittest.TestCase):
    """Unit tests for the update_screen function."""

    def setUp(self) -> None:
        """Set up a mock screen and GameBoard instance for each test."""
        # Initialize a mock Pygame screen
        self.mock_screen = MagicMock(spec=pygame.Surface)
        
        # Create a mock GameBoard
        self.mock_game_board = MagicMock(spec=GameBoard)
        
    @patch('pygame.display.flip')
    def test_update_screen(self, mock_flip):
        """Test that update_screen correctly fills the screen, draws the board, and flips the display."""
        # Call the update_screen function with the mock screen and game board
        update_screen(self.mock_screen, self.mock_game_board)
        
        # Check that the screen was filled with the background color
        self.mock_screen.fill.assert_called_once_with((255, 255, 255))
        
        # Check that the game board's draw_board method was called
        self.mock_game_board.draw_board.assert_called_once_with(self.mock_screen)
        
        # Check that the display was flipped
        mock_flip.assert_called_once()

if __name__ == '__main__':
    unittest.main()