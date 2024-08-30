import unittest
from unittest.mock import patch, MagicMock
import pygame
from src.player import Player
from src.gameboard import GameBoard
from src.gamestate import GameState
from src.handle_events import handle_events

class TestHandleEvents(unittest.TestCase):
    """Unit tests for the handle_events function."""

    def setUp(self) -> None:
        """Set up a new game state and game board for each test."""
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.board = GameBoard()
        self.game_state = GameState(self.player_x, self.player_o)

    @patch('pygame.event.get')
    def test_handle_quit_event(self, mock_pygame_event_get):
        """Test that the game quits when a QUIT event is received."""
        mock_pygame_event_get.return_value = [pygame.event.Event(pygame.QUIT)]
        
        with self.assertRaises(SystemExit):
            handle_events(self.game_state, self.board)

    @patch('pygame.event.get')
    def test_handle_valid_move(self, mock_pygame_event_get):
        """Test that a valid move is handled correctly."""
        # Simulate a mouse click at position (50, 50) which corresponds to board (0, 0)
        mock_pygame_event_get.return_value = [
            pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(50, 50))
        ]
        
        result = handle_events(self.game_state, self.board)
        
        # Check that the move was made and the player switched
        self.assertEqual(self.board.grid[0][0], 'X')
        self.assertEqual(self.game_state.current_player, self.player_o)
        self.assertIsNone(result)
    
    @patch('pygame.event.get')
    def test_handle_invalid_move(self, mock_pygame_event_get):
        """Test that an invalid move (on an occupied cell) is handled correctly."""
        # Simulate two mouse clicks at position (50, 50) which corresponds to board (0, 0)
        self.board.mark_cell(0, 0, 'X')  # Manually mark the cell to simulate the first move
        
        mock_pygame_event_get.return_value = [
            pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(50, 50))
        ]
        
        result = handle_events(self.game_state, self.board)
        
        # The move should fail, and the player should not switch
        self.assertEqual(self.board.grid[0][0], 'X')
        self.assertEqual(self.game_state.current_player, self.player_x)
        self.assertIsNone(result)

    @patch('pygame.event.get')
    def test_handle_winning_move(self, mock_pygame_event_get):
        """Test that a winning move is handled correctly."""
        # Set up a winning condition for X
        self.board.mark_cell(0, 0, 'X')
        self.board.mark_cell(0, 1, 'X')
        
        mock_pygame_event_get.return_value = [
            pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(250, 50))  # (0, 2) should be winning move
        ]
        
        result = handle_events(self.game_state, self.board)
        
        # Check that the game recognizes the winner
        self.assertEqual(self.board.grid[0][2], 'X')
        self.assertTrue(self.game_state.game_over)
        self.assertEqual(result, 'X')

    @patch('pygame.event.get')
    def test_handle_draw(self, mock_pygame_event_get):
        """Test that a draw is handled correctly."""
        # Fill the board except for one cell, ensuring no winners
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'X'), (1, 1, 'O'), (1, 2, 'X'),
            (2, 0, 'O'), (2, 1, 'X')
        ]
        for row, col, symbol in moves:
            self.board.mark_cell(row, col, symbol)
        
        # Manually set the current player to 'O' for the last move
        self.game_state.current_player = self.player_o

        # Mock the last move to fill the board and cause a draw
        mock_pygame_event_get.return_value = [
            pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(250, 250))  # (2, 2) last move, draw
        ]
        
        result = handle_events(self.game_state, self.board)
        
        # Check that the game ends in a draw
        self.assertEqual(self.board.grid[2][2], 'O')  # 'O' should be placed here
        self.assertTrue(self.game_state.game_over)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()