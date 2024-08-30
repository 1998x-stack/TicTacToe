# TicTacToe

A Python implementation of the classic Tic-Tac-Toe game.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
TicTacToe
├── README.md
├── __init__.py
├── main.py
├── remove_files.sh
├── src
│   ├── __init__.py
│   ├── gameboard.py
│   ├── gamestate.py
│   ├── handle_events.py
│   ├── player.py
│   └── update_screen.py
└── test
    ├── __init__.py
    ├── test_gameboard.py
    ├── test_gamestate.py
    ├── test_handle_events.py
    ├── test_player.py
    └── test_update_screen.py
```

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TicTacToe.git
   cd TicTacToe
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the game, run the following command from the project root:

```bash
python main.py
```

Follow the on-screen instructions to play the game.

## Features

- Classic Tic-Tac-Toe gameplay
- Modular code structure for easy maintenance and extension
- Comprehensive test suite

## Testing

To run the tests, execute the following command from the project root:

```bash
python -m unittest discover test
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides a good starting point based on the structure of your TicTacToe project. You may want to customize it further by:

1. Adding more specific details about how to play the game.
2. Describing any special features or game modes your implementation might have.
3. Explaining the purpose of each module in the `src` directory.
4. Providing information about any dependencies your project might have.
5. Adding badges (e.g., build status, test coverage) if you're using any CI/CD tools.
6. Including screenshots or GIFs of the game in action.

---

### 详细展开各个类及其函数逻辑

在设计井字棋游戏时，每个类的职责和函数的设计至关重要。下面是各个类需要的函数及其详细的逻辑展开。

---

### 1. **GameBoard 类**

**职责**: 负责表示和管理井字棋的棋盘状态，包括绘制棋盘、标记棋盘、检查胜利条件等。

**属性**:
- `grid`: 一个二维列表（3x3），用于表示棋盘的当前状态。每个元素可以是 `'X'`、`'O'` 或 `None`（表示该位置为空）。

**函数及其逻辑**:

1. **`__init__()`**
   - **逻辑**: 初始化棋盘，将 `grid` 设置为一个 3x3 的空矩阵，即每个单元格的初始值为 `None`。

2. **`draw_board(screen)`**
   - **逻辑**:
     - 该函数负责在屏幕上绘制棋盘。
     - 使用 Pygame 的绘图函数在指定的 `screen` 上绘制棋盘的线条。
     - 遍历 `grid`，在每个单元格中检查是否有 `'X'` 或 `'O'`，并在相应的位置绘制这些符号。

3. **`mark_cell(row, col, player_symbol)`**
   - **逻辑**:
     - 检查 `grid[row][col]` 是否为 `None`，即该单元格是否为空。
     - 如果为空，将该单元格标记为 `player_symbol`（即 `'X'` 或 `'O'`）。
     - 返回布尔值，表示标记是否成功（用于判断该位置是否已被占用）。

4. **`check_winner()`**
   - **逻辑**:
     - 该函数用于检查当前棋盘是否有胜利者。
     - 检查所有行、列和对角线是否存在相同的非 `None` 符号（即三个 `'X'` 或三个 `'O'`）。
     - 如果找到胜利条件，返回胜利者的符号（`'X'` 或 `'O'`）；否则返回 `None`。

5. **`is_full()`**
   - **逻辑**:
     - 遍历 `grid` 中的所有单元格。
     - 如果存在 `None` 值，表示棋盘未满，返回 `False`。
     - 如果所有单元格都已被占用，返回 `True`。

6. **`reset()`**
   - **逻辑**:
     - 重置棋盘，将 `grid` 中的所有值设为 `None`，以便开始新的一局游戏。

---

### 2. **Player 类**

**职责**: 负责管理玩家的状态和操作，主要包括玩家的符号以及在棋盘上的操作。

**属性**:
- `symbol`: 玩家所使用的符号，可能是 `'X'` 或 `'O'`。

**函数及其逻辑**:

1. **`__init__(symbol)`**
   - **逻辑**: 初始化玩家的符号，将 `symbol` 属性设置为传入的值（`'X'` 或 `'O'`）。

2. **`make_move(board, row, col)`**
   - **逻辑**:
     - 调用 `board.mark_cell(row, col, self.symbol)`，尝试在指定位置标记当前玩家的符号。
     - 返回标记的结果（成功或失败），用于在游戏逻辑中判断是否需要切换玩家或重试。

3. **`get_symbol()`**
   - **逻辑**: 返回玩家的符号（`'X'` 或 `'O'`），用于显示或其他逻辑判断。

---

### 3. **GameState 类**

**职责**: 管理游戏的整体状态，包括当前玩家、游戏是否结束等。

**属性**:
- `current_player`: 当前正在进行操作的玩家对象（`Player` 实例）。
- `game_over`: 布尔值，指示游戏是否结束。

**函数及其逻辑**:

1. **`__init__(player1, player2)`**
   - **逻辑**: 初始化游戏状态，设置 `player1` 为当前玩家，`game_over` 为 `False`。

2. **`switch_player()`**
   - **逻辑**:
     - 切换 `current_player`，在 `player1` 和 `player2` 之间切换。
     - 更新 `current_player` 为另一个玩家对象。

3. **`check_game_over(board)`**
   - **逻辑**:
     - 调用 `board.check_winner()` 检查是否有玩家获胜。
     - 如果存在胜利者，设置 `game_over` 为 `True`，并可能返回胜利者的符号。
     - 如果 `board.is_full()` 返回 `True`，且没有胜利者，设置 `game_over` 为 `True`，表示平局。

4. **`restart_game()`**
   - **逻辑**:
     - 重置 `game_over` 为 `False`。
     - 可能重置棋盘和玩家的状态，以便开始新游戏。

---

### 4. **函数**

除了以上的类之外，还需要一些全局函数来管理事件处理、屏幕更新等功能。

**函数及其逻辑**:

1. **`handle_events(game_state, game_board)`**
   - **逻辑**:
     - 使用 Pygame 的事件处理函数捕获用户输入（如鼠标点击）。
     - 检查点击的位置是否在棋盘范围内，并将其转换为棋盘上的行列坐标。
     - 调用 `game_state.current_player.make_move(game_board, row, col)` 来处理当前玩家的移动。
     - 如果移动成功，检查游戏是否结束（调用 `game_state.check_game_over()`），并在必要时切换玩家。

2. **`update_screen(screen, game_board)`**
   - **逻辑**:
     - 清空屏幕或背景（用一种颜色填充屏幕）。
     - 调用 `game_board.draw_board(screen)` 绘制棋盘和所有标记。
     - 调用 Pygame 的屏幕刷新函数（如 `pygame.display.flip()`）来更新显示。

3. **`main()`**
   - **逻辑**:
     - 初始化 Pygame 库，创建屏幕窗口并设置基本参数。
     - 创建 `Player` 对象、`GameBoard` 对象、和 `GameState` 对象。
     - 进入游戏循环，重复调用 `handle_events()` 和 `update_screen()` 直到 `game_state.game_over` 为 `True`。
     - 在游戏结束后，显示结果并等待用户输入决定是否重新开始或退出游戏。

---

### 5. **流程总结**

通过以上类和函数的详细设计，可以确保井字棋游戏的每个部分都有明确的职责和清晰的逻辑。各类之间的职责分离、模块化设计不仅提高了代码的可读性和可维护性，也为将来可能的扩展（如引入 AI 玩家或增加其他功能）提供了便利。

---

### 各个函数之间的引用关系详细展开

在设计井字棋游戏时，理解各个函数之间的相互引用关系有助于明确整个游戏的工作流程。以下是详细的函数引用关系及其在游戏中的作用。

---

### 1. **`main()` 函数**

**`main()`** 是游戏的入口点，它调用和管理游戏的主要流程。

- **调用顺序**：
  1. **初始化 Pygame**：设置窗口、加载资源等。
  2. **创建对象**：
     - 创建 `Player` 对象（两个玩家）。
     - 创建 `GameBoard` 对象（游戏棋盘）。
     - 创建 `GameState` 对象（管理游戏状态）。
  3. **游戏循环**：
     - **`handle_events(game_state, game_board)`**: 每一帧调用一次，处理用户输入（如鼠标点击），并相应地更新游戏状态。
     - **`update_screen(screen, game_board)`**: 每一帧调用一次，重新绘制游戏屏幕，更新显示。
  4. **游戏结束**：
     - 判断 `game_state.game_over` 是否为 `True`，如果是，则终止游戏循环，显示游戏结果。

---

### 2. **`handle_events(game_state, game_board)` 函数**

**`handle_events()`** 负责处理用户输入（如鼠标点击），并通过调用其他类的方法更新游戏状态。

- **引用关系**：
  1. **捕获事件**：
     - 使用 Pygame 的 `pygame.event.get()` 来捕获用户输入事件（如鼠标点击）。
  2. **处理点击事件**：
     - 根据鼠标点击的位置，计算相应的棋盘坐标（`row` 和 `col`）。
     - 调用 `game_state.current_player.make_move(game_board, row, col)` 来尝试在棋盘上标记玩家的符号。
  3. **检查游戏状态**：
     - 如果玩家的移动成功，调用 `game_state.check_game_over(game_board)` 来检查游戏是否结束（胜利或平局）。
     - 如果游戏未结束，调用 `game_state.switch_player()` 来切换当前玩家。

- **关联的类和方法**：
  - **`Player.make_move()`**: 尝试在指定位置标记玩家的符号。
  - **`GameState.check_game_over()`**: 检查游戏是否有胜利者或平局。
  - **`GameState.switch_player()`**: 切换当前玩家。

---

### 3. **`update_screen(screen, game_board)` 函数**

**`update_screen()`** 负责在每一帧重新绘制游戏界面。

- **引用关系**：
  1. **清空屏幕**：用一种背景颜色（如白色）填充屏幕，以清除上一帧的内容。
  2. **绘制棋盘**：
     - 调用 `game_board.draw_board(screen)` 在屏幕上绘制当前棋盘状态，包括所有玩家的标记。
  3. **刷新显示**：
     - 使用 Pygame 的 `pygame.display.flip()` 或 `pygame.display.update()` 来更新显示内容。

- **关联的类和方法**：
  - **`GameBoard.draw_board()`**: 绘制当前棋盘和标记。

---

### 4. **`Player.make_move(game_board, row, col)` 函数**

**`Player.make_move()`** 负责在玩家点击时尝试在棋盘上标记玩家的符号。

- **引用关系**：
  1. **尝试标记**：
     - 调用 `game_board.mark_cell(row, col, self.symbol)` 来标记棋盘上的指定位置。
  2. **返回结果**：根据 `mark_cell()` 的返回值（成功或失败）决定是否需要继续其他操作。

- **关联的类和方法**：
  - **`GameBoard.mark_cell()`**: 尝试在棋盘的指定位置标记玩家的符号。

---

### 5. **`GameBoard.mark_cell(row, col, player_symbol)` 函数**

**`GameBoard.mark_cell()`** 负责更新棋盘状态，在指定位置标记玩家的符号。

- **引用关系**：
  1. **检查单元格状态**：检查 `grid[row][col]` 是否为空（`None`）。
  2. **标记单元格**：
     - 如果单元格为空，将其设置为 `player_symbol`（即 `'X'` 或 `'O'`）。
     - 返回布尔值，表示标记是否成功。

- **被调用**：
  - **`Player.make_move()`**: 用于在棋盘上标记玩家的符号。

---

### 6. **`GameBoard.draw_board(screen)` 函数**

**`GameBoard.draw_board()`** 负责在屏幕上绘制棋盘和标记。

- **引用关系**：
  1. **绘制网格**：
     - 使用 Pygame 的绘图函数在 `screen` 上绘制 3x3 的网格线。
  2. **绘制标记**：
     - 遍历 `grid`，在每个单元格中检查是否有 `'X'` 或 `'O'`，并在相应的位置绘制这些符号。

- **被调用**：
  - **`update_screen()`**: 在每一帧重新绘制棋盘和标记。

---

### 7. **`GameState.check_game_over(game_board)` 函数**

**`GameState.check_game_over()`** 负责检查游戏是否结束（是否有胜利者或棋盘已满）。

- **引用关系**：
  1. **检查胜利者**：
     - 调用 `game_board.check_winner()` 来检查当前是否有胜利者。
  2. **检查平局**：
     - 如果没有胜利者，调用 `game_board.is_full()` 来判断棋盘是否已满（是否平局）。
  3. **更新状态**：
     - 如果游戏结束（胜利或平局），将 `game_over` 属性设置为 `True`。

- **关联的类和方法**：
  - **`GameBoard.check_winner()`**: 检查当前棋盘是否有胜利者。
  - **`GameBoard.is_full()`**: 检查棋盘是否已满。

---

### 8. **`GameState.switch_player()` 函数**

**`GameState.switch_player()`** 负责在玩家回合之间切换当前玩家。

- **引用关系**：
  1. **切换当前玩家**：根据当前 `current_player`，将其切换为另一个玩家。
  2. **更新属性**：更新 `current_player` 属性。

- **被调用**：
  - **`handle_events()`**: 在当前玩家完成操作且游戏未结束时调用，用于切换玩家。

---

### 总结

通过以上对各个函数之间引用关系的详细展开，可以清晰地看到游戏的整体流程如何通过各个函数之间的相互调用来实现。各个函数之间的引用关系如下：

- **`main()`** 调用 `handle_events()` 和 `update_screen()` 来处理游戏的主要流程。
- **`handle_events()`** 通过调用 `Player.make_move()` 和 `GameState.check_game_over()` 来处理用户输入，并在必要时调用 `GameState.switch_player()` 切换玩家。
- **`update_screen()`** 通过调用 `GameBoard.draw_board()` 来更新屏幕显示。
- **`Player.make_move()`** 调用 `GameBoard.mark_cell()` 来在棋盘上标记玩家的符号。
- **`GameState.check_game_over()`** 调用 `GameBoard.check_winner()` 和 `GameBoard.is_full()` 来检查游戏是否结束。