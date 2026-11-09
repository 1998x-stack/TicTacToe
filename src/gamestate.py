from typing import Optional

class GameState:
    """The two-player turn and terminal-state machine."""

    def __init__(self, player_x: 'Player', player_o: 'Player') -> None:
        self.player_x = player_x
        self.player_o = player_o
        self.reset()

    def reset(self) -> None:
        self.current_player = self.player_x
        self.game_over = False

    def switch_player(self) -> None:
        # Keep this small method backwards-compatible with existing tests.
        self.current_player = self.player_o if self.current_player == self.player_x else self.player_x

    def check_game_over(self, board: 'GameBoard') -> Optional[str]:
        winner = board.check_winner()
        if winner or board.is_full():
            self.game_over = True
        return winner
