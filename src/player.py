class Player:
    """表示井字棋游戏中的玩家的类。

    这个类管理玩家的符号和在游戏板上进行移动的动作。
    
    属性：
        symbol: 玩家使用的符号（'X' 或 'O'）。
    """

    def __init__(self, symbol: str) -> None:
        """初始化具有特定符号的玩家。

        参数：
            symbol: 表示玩家符号的字符串（'X' 或 'O'）。
        """
        if symbol not in ['X', 'O']:  # 检查符号是否有效
            raise ValueError("Player symbol must be 'X' or 'O'.")  # 如果符号无效，抛出异常
        self.symbol = symbol  # 设置玩家的符号
        print(f"Player initialized with symbol: {self.symbol}")  # 打印初始化信息

    def make_move(self, board: 'GameBoard', row: int, col: int) -> bool:
        """尝试在游戏板上进行移动。

        该方法尝试用玩家的符号标记指定的单元格。

        参数：
            board: 将进行移动的GameBoard实例。
            row: 将进行移动的行索引。
            col: 将进行移动的列索引。

        返回：
            bool: 如果移动成功则为True，如果单元格已被占用则为False。
        """
        print(f"Player {self.symbol} attempting to move at ({row}, {col})")  # 打印尝试移动的信息
        success = board.mark_cell(row, col, self.symbol)  # 尝试标记单元格
        if success:  # 如果移动成功
            print(f"Player {self.symbol} successfully marked ({row}, {col}).")  # 打印成功信息
        else:  # 如果移动失败
            print(f"Player {self.symbol} failed to mark ({row}, {col}) - cell already occupied.")  # 打印失败信息
        return success  # 返回移动是否成功

    def get_symbol(self) -> str:
        """返回玩家的符号。

        返回：
            str: 玩家的符号（'X' 或 'O'）。
        """
        return self.symbol  # 返回玩家的符号