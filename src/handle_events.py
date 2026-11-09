"""Map UI events into state transitions; never terminate the interpreter."""
import pygame
from typing import Optional

def handle_events(game_state: 'GameState', game_board: 'GameBoard') -> Optional[str]:
    """Return 'QUIT', a winner symbol, 'RESTART', or None.

    A terminal board rejects further moves until the player explicitly presses R.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                return "QUIT"
            if event.key == pygame.K_r:
                game_board.reset()
                game_state.reset()
                return "RESTART"
        if event.type == pygame.MOUSEBUTTONDOWN and getattr(event, "button", 1) == 1:
            if game_state.game_over:
                continue
            x, y = event.pos
            row, col = y // 100, x // 100
            if 0 <= row < 3 and 0 <= col < 3:
                if game_state.current_player.make_move(game_board, row, col):
                    winner = game_state.check_game_over(game_board)
                    if winner:
                        return winner
                    if game_state.game_over:
                        return None  # draw: game_over distinguishes this from ongoing
                    game_state.switch_player()
    return None
