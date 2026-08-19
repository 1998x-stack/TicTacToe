# TicTacToe — Optimization Design

Date: 2026-08-19
Repo-relative path: `docs/superpowers/specs/2026-08-19-tictactoe-design.md`

## Goal

Optimize the TicTacToe game. Priorities (user-ranked): **Performance →
Readability → Correctness → Polish.** Honest scoping: this is a tiny local
human-vs-human 3×3 game — no AI, and no meaningful performance surface. The
real value is **correctness** (a broken test module currently hides `GameState`
verification) and **readability** (28 scattered debug `print()` calls).

## Current state

- No AI — two human players alternate (`Player X`, `Player O`) via `GameState`.
  (The wave-plan note about "TicTacToe AI logic" does not apply.)
- `src/gameboard.py` (`GameBoard`: 3×3 grid, `mark_cell`, `check_winner`,
  `is_full`, `reset`, `draw_board`), `src/gamestate.py`, `src/player.py`,
  `src/handle_events.py`, `src/update_screen.py`, `src/sound.py`, `main.py`.
- Tests use `unittest` under `test/`.

### Key defect found

`test/test_gamestate.py` line 2 imports `from src.cgameboard import GameBoard`
— the module is `gameboard`, not `cgameboard`. The whole file fails to import,
so **none of the 6 `GameState` tests run**: `GameState` (winner detection,
draw detection, ongoing detection, turn switching, game-over flag) is
currently unverified.

### Secondary issue

28 `print()` debug statements in `src/` (e.g. every `mark_cell`, `check_winner`,
`switch_player`, `make_move`, `update_screen` step, sound) flood stdout — even
during tests. They are unused debug noise.

## Optimization plan

### B — Performance
- **None needed.** The board is 3×3; every operation is O(1). Recorded
  explicitly so reviewers don't invent perf work.

### A — Correctness
1. **Fix the `cgameboard` typo** in `test/test_gamestate.py` (→ `gameboard`) so
   the 6 GameState tests execute.
2. Run the previously-untested GameState logic; fix any genuine defects it
   reveals. Add coverage if any GameState edge is missed.

### C — Readability
3. **Remove the 28 debug `print()` calls** from `src/` (user-approved option A).
   Public method signatures and return values are unchanged; only stdout noise
   is removed. Tests do not assert on stdout.
4. Keep the Chinese comments (consistent with the repo).

### D — Polish (low-cost only)
5. If trivial while editing: extract the hardcoded board geometry (100px cell,
   300px window) used by `gameboard.draw_board`, `handle_events`, and `main.py`
   into a small `src/config.py` — only if it does not expand scope
   meaningfully. Otherwise leave for a follow-up.

## Architecture

- All changes are within existing `src/` and `test/` files (drop `print`s,
  fix one import), plus optional `src/config.py` for geometry constants.
- No public API/signature changes.

## Data flow

Unchanged: `main.py` loop → `handle_events` → `current_player.make_move` →
`check_game_over` → `switch_player` → `update_screen`.

## Error handling

- `mark_cell` keeps raising `ValueError` for out-of-bounds.
- Removing `print()` must not change values/returns; add a test asserting
  stdout is silent during a normal move (optional) to lock the cleanup.

## Testing & verification

Baseline: `python3 -m unittest test.test_gameboard test.test_player
test.test_update_screen test.test_handle_events`
(currently 20 pass; `test.test_gamestate` FAILS to import).

After (expected):
- `python3 -m unittest discover test` → all 5 modules pass (21 tests + any added).
- New: a `stdout`-silence test for a move (optional).

## Deliverable

Fixed `test/test_gamestate.py`, `print()`-clean `src/gameboard.py`,
`src/gamestate.py`, `src/player.py`, `src/handle_events.py`,
`src/update_screen.py`, `src/sound.py`, `main.py`; all tests green. Working
tree clean.