# TicTacToe Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the broken `GameState` test module (on `src.cgameboard` typo) so its logic is actually verified, and remove the 28 debug `print()` calls from `src/`. No move/return-value changes.

**Architecture:** Change only `test/test_gamestate.py` (import fix) plus `src/*.py` (drop `print()` noise). Optionally add `src/config.py` for geometry constants. Public API unchanged.

**Tech Stack:** Python 3.9+, pygame. Tests are `unittest` under `test/`.

## Global Constraints

- Public method signatures and return values unchanged; only stdout noise removed.
- `mark_cell` keeps raising `ValueError` on out-of-bounds.
- Chinese comments preserved.
- Repo root: `/Users/x/Desktop/1998x-stack/00-仓库/15-游戏与趣味/TicTacToe`. Run tests with `python3 -m unittest test.test_gameboard test.test_player test.test_update_screen test.test_handle_events test.test_gamestate`.

---

### Task 1: Fix the GameState import typo (correctness)

**Files:**
- Modify: `test/test_gamestate.py:2` (typo `cgameboard` → `gameboard`)

**Interfaces:**
- Consumes: `src.gameboard.GameBoard`, `src.player.Player`, `src.gamestate.GameState`
- Produces: a runnable `test.test_gamestate` module (6 tests)

- [ ] **Step 1: Capture red state**

Run: `python3 -m unittest test.test_gamestate 2>&1 | tail -4`
Expected: `ModuleNotFoundError: No module named 'src.cgameboard'`.

- [ ] **Step 2: Fix the import**

In `test/test_gamestate.py`, change `from src.cgameboard import GameBoard` to `from src.gameboard import GameBoard`.

- [ ] **Step 3: Run the module**

Run: `python3 -m unittest test.test_gamestate -v 2>&1 | tail -10`
Expected: 6 tests all PASS (winner, draw, ongoing, switch, game-over-flag). If any FAIL, fix the underlying `gamestate.py` bug (don't weaken tests) and note the bug fixed.

- [ ] **Step 4: Commit**

```bash
git add test/test_gamestate.py src/gamestate.py
git commit -m "fix(test): correct cgameboard import so GameState tests run"
```

---

### Task 2: Remove debug print() noise from src/

**Files:**
- Modify: `src/gameboard.py`, `src/gamestate.py`, `src/player.py`, `src/handle_events.py`, `src/update_screen.py`, `src/sound.py`, `main.py`
- Test: `test/test_gameboard.py` (add a stdout-silence guard)

**Interfaces:**
- Produces: public methods/functions with identical signatures and returns; no `print()` remains in `src/`.

- [ ] **Step 1: Write the failing test (stdout-silence guard)**

Add to `test/test_gameboard.py` (add `import io` and `import contextlib` at top):

```python
    def test_mark_cell_is_quiet(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.board.mark_cell(0, 0, 'X')
            _ = self.board.mark_cell(0, 1, 'X')
            _ = self.board.reset()
        self.assertEqual(buf.getvalue(), "")
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m unittest test.test_gameboard.TestGameBoard.test_mark_cell_is_quiet -v 2>&1 | tail -4`
Expected: FAIL (stdout still contains `单元格 ...` debug lines).

- [ ] **Step 3: Remove debug prints**

In each listed `src/` module, delete every `print(...)` line (and any `import sys` present only for printing). Keep comments and logic/returns exactly.

- [ ] **Step 4: Run to verify it passes**

Run: `python3 -m unittest test.test_gameboard test.test_player test.test_update_screen test.test_handle_events test.test_gamestate 2>&1 | tail -4`
Expected: all PASS (27 tests).

- [ ] **Step 5: Commit**

```bash
git add src/ test/test_gameboard.py
git commit -m "cleanup(src): remove debug print noise; add stdout-silence guard"
```

---

### Task 3: Verify end-to-end

**Files:**
- Test: all five modules

- [ ] **Step 1: Run full suite**

Run: `python3 -m unittest discover test -v 2>&1 | tail -8`
Expected: 27 tests pass.

- [ ] **Step 2: Confirm no prints remain in src/**

Run: `grep -rn "print(" src/ | grep -v "#" | wc -l`
Expected: `0`.

- [ ] **Step 3: Confirm working tree clean**

Run: `git status -s` → empty (only git-ignored `.superpowers/`).

- [ ] **Step 4: Commit any residual**

If nothing to commit, skip. Otherwise describe and commit.
