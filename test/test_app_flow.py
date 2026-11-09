"""Regression tests for game-over lock, restart and headless application boot."""
import unittest
from unittest.mock import patch
import pygame
from src.gameboard import GameBoard
from src.player import Player
from src.gamestate import GameState
from src.handle_events import handle_events
from main import main


class GameFlowTests(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.state = GameState(Player("X"), Player("O"))

    def event(self, event):
        with patch("pygame.event.get", return_value=[event]):
            return handle_events(self.state, self.board)

    def click(self, row, col):
        return self.event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,
            button=1, pos=(col * 100 + 50, row * 100 + 50)))

    def test_winner_lock_and_restart(self):
        self.board.grid[0] = ["X", "X", None]
        self.assertEqual(self.click(0, 2), "X")
        self.assertTrue(self.state.game_over)
        self.assertIsNone(self.click(1, 0))
        self.assertIsNone(self.board.grid[1][0])
        self.assertEqual(self.event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)), "RESTART")
        self.assertFalse(self.state.game_over)
        self.assertTrue(all(cell is None for row in self.board.grid for cell in row))
        self.assertEqual(self.state.current_player.symbol, "X")
        self.assertIsNone(self.click(0, 0))
        self.assertEqual(self.board.grid[0][0], "X")

    def test_quit_does_not_raise_or_exit_process(self):
        self.assertEqual(self.event(pygame.event.Event(pygame.QUIT)), "QUIT")
        self.assertEqual(self.event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)), "QUIT")

    def test_secondary_button_and_outside_click_do_nothing(self):
        self.assertIsNone(self.event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=3, pos=(50, 50))))
        self.assertIsNone(self.click(3, 0))
        self.assertEqual(self.state.current_player.symbol, "X")
        self.assertIsNone(self.board.grid[0][0])

    def test_draw_replay(self):
        self.board.grid = [
            ["X", "O", "X"], ["X", "O", "X"], ["O", "X", None]]
        self.state.current_player = self.state.player_o
        self.assertIsNone(self.click(2, 2))
        self.assertTrue(self.state.game_over)
        self.assertIsNone(self.click(0, 0))
        self.assertEqual(self.event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)), "RESTART")
        self.assertFalse(self.state.game_over)

    def test_headless_window_smoke(self):
        # Does not claim physical monitor/audio device availability.
        main(max_frames=1)


if __name__ == "__main__":
    unittest.main()
