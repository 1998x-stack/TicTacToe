from typing import Optional  # 导入Optional类型

class GameState:
    """游戏状态类，表示井字棋游戏的状态。

    该类管理当前玩家、游戏状态，并决定游戏何时结束。
    
    属性：
        current_player: 当前轮到哪个玩家实例进行游戏。
        game_over: 布尔值，表示游戏是否结束。
        player_x: 代表'X'玩家的实例。
        player_o: 代表'O'玩家的实例。
    """

    def __init__(self, player_x: 'Player', player_o: 'Player') -> None:
        """初始化游戏状态，包含两个玩家。

        参数：
            player_x: 代表'X'玩家的实例。
            player_o: 代表'O'玩家的实例。
        """
        self.player_x = player_x  # 设置X玩家
        self.player_o = player_o  # 设置O玩家
        self.current_player = player_x  # 设置当前玩家为X
        self.game_over = False  # 初始化游戏未结束
        print("游戏初始化完成。X玩家先手。")

    def switch_player(self) -> None:
        """切换当前玩家到另一个玩家。"""
        if self.current_player == self.player_x:
            self.current_player = self.player_o  # 如果当前是X玩家，切换到O玩家
        else:
            self.current_player = self.player_x  # 否则切换到X玩家
        print(f"玩家切换。现在轮到{self.current_player.get_symbol()}玩家。")

    def check_game_over(self, board: 'GameBoard') -> Optional[str]:
        """检查游戏是否因胜利或平局而结束。

        参数：
            board: 用于检查胜者或平局的游戏板实例。

        返回：
            str或None: 获胜玩家的符号，如果是平局或游戏仍在进行则返回None。
        """
        winner = board.check_winner()  # 检查是否有胜者
        if winner:
            self.game_over = True  # 如果有胜者，游戏结束
            print(f"游戏结束！胜者是{winner}。")
            return winner
        
        if board.is_full():  # 检查棋盘是否已满
            self.game_over = True  # 如果棋盘已满，游戏结束
            print("游戏结束！平局。")
            return None
        
        return None  # 游戏继续