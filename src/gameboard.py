import pygame  # 导入 pygame 库，用于图形界面
from typing import Optional  # 导入 Optional 类型，用于类型提示

class GameBoard:
    """井字棋游戏板类
    
    此类处理井字棋游戏板的创建、显示和状态管理。
    
    属性:
        grid: 表示游戏板的 3x3 矩阵。
    """

    def __init__(self) -> None:
        """初始化一个新的井字棋游戏板。"""
        self.grid = [[None for _ in range(3)] for _ in range(3)]  # 初始化 3x3 的网格，初始值为 None 表示空单元格

    def draw_board(self, screen: pygame.Surface) -> None:
        """在屏幕上绘制井字棋游戏板。

        参数:
            screen: 用于绘制游戏板的 Pygame 表面。
        """
        for row in range(1, 3):  # 绘制水平线
            pygame.draw.line(screen, (0, 0, 0), (0, row * 100), (300, row * 100), 3)
            pygame.draw.line(screen, (0, 0, 0), (row * 100, 0), (row * 100, 300), 3)  # 绘制垂直线
        
        for row in range(3):  # 遍历网格行
            for col in range(3):  # 遍历网格列
                if self.grid[row][col] == 'X':  # 如果单元格是 'X'
                    pygame.draw.line(screen, (255, 0, 0),   # 绘制 'X' 的第一条线
                                     (col * 100 + 15, row * 100 + 15), 
                                     (col * 100 + 85, row * 100 + 85), 3)
                    pygame.draw.line(screen, (255, 0, 0),   # 绘制 'X' 的第二条线
                                     (col * 100 + 85, row * 100 + 15), 
                                     (col * 100 + 15, row * 100 + 85), 3)
                elif self.grid[row][col] == 'O':  # 如果单元格是 'O'
                    pygame.draw.circle(screen, (0, 0, 255),   # 绘制 'O'
                                       (col * 100 + 50, row * 100 + 50), 
                                       40, 3)

    def mark_cell(self, row: int, col: int, player_symbol: str) -> bool:
        """在游戏板上标记一个单元格，如果该单元格为空。

        参数:
            row: 要标记的单元格的行索引。
            col: 要标记的单元格的列索引。
            player_symbol: 要放置在单元格中的符号（'X' 或 'O'）。

        返回:
            bool: 如果单元格成功标记则返回 True，如果单元格已被占用则返回 False。
        """
        if not (0 <= row < 3 and 0 <= col < 3):  # 检查行和列的边界条件
            raise ValueError("行和列必须在 0-2 的范围内。")
        
        if self.grid[row][col] is None:  # 如果单元格为空
            self.grid[row][col] = player_symbol  # 标记单元格
            print(f"单元格 ({row}, {col}) 被标记为 '{player_symbol}'。")
            return True
        
        print(f"单元格 ({row}, {col}) 已被占用。")
        return False

    def check_winner(self) -> Optional[str]:
        """检查游戏板上是否有赢家，通过评估行、列和对角线。

        返回:
            str 或 None: 赢家的符号（'X' 或 'O'），如果还没有赢家则返回 None。
        """
        for i in range(3):  # 检查行和列
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] is not None:
                print(f"在第 {i} 行找到赢家：'{self.grid[i][0]}'")
                return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] is not None:
                print(f"在第 {i} 列找到赢家：'{self.grid[0][i]}'")
                return self.grid[0][i]
        
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:  # 检查主对角线
            print("在对角线（左上到右下）找到赢家。")
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:  # 检查副对角线
            print("在对角线（右上到左下）找到赢家。")
            return self.grid[0][2]
        
        return None  # 没有找到赢家

    def is_full(self) -> bool:
        """检查游戏板是否已满（即所有单元格都被占用）。

        返回:
            bool: 如果游戏板已满则返回 True，如果还有空单元格则返回 False。
        """
        for row in self.grid:  # 遍历网格的每一行
            if None in row:  # 如果行中有空单元格
                return False
        
        print("游戏板已满。")
        return True

    def reset(self) -> None:
        """重置游戏板，清空所有单元格。"""
        self.grid = [[None for _ in range(3)] for _ in range(3)]  # 重置网格，将所有单元格设为 None
        print("游戏板已被重置。")