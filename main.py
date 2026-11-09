"""Run a replayable desktop Tic-Tac-Toe match."""
import pygame
from src.player import Player
from src.gameboard import GameBoard
from src.gamestate import GameState
from src.handle_events import handle_events
from src.update_screen import update_screen
from src.sound import play_background_music, stop_background_music


def main(max_frames=None) -> None:
    """Open a game window; max_frames is for headless CI smoke tests only."""
    pygame.init()
    screen = pygame.display.set_mode((300, 344))
    pygame.display.set_caption("Tic-Tac-Toe · R: restart, Esc: quit")
    clock = pygame.time.Clock()
    play_background_music()  # Optional: works with silent/headless CI too.
    board = GameBoard()
    state = GameState(Player("X"), Player("O"))
    result = None
    running = True
    frames = 0
    try:
        while running:
            action = handle_events(state, board)
            if action == "QUIT":
                running = False
            elif action == "RESTART":
                result = None
            elif action in ("X", "O"):
                result = action
            message = ("Winner: " + result + " · R: replay" if result else
                "Draw · R: replay" if state.game_over else
                "Turn: " + state.current_player.symbol + " · R: reset")
            update_screen(screen, board, message)
            clock.tick(30)
            frames += 1
            if max_frames is not None and frames >= max_frames:
                break
    finally:
        stop_background_music()
        pygame.quit()


if __name__ == "__main__":
    main()
