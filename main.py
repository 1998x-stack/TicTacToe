import pygame  # 导入pygame库
from src.player import Player  # 从src.player模块导入Player类
from src.gameboard import GameBoard  # 从src.gameboard模块导入GameBoard类
from src.gamestate import GameState  # 从src.gamestate模块导入GameState类
from src.handle_events import handle_events  # 从src.handle_events模块导入handle_events函数
from src.update_screen import update_screen  # 从src.update_screen模块导入update_screen函数
from src.sound import play_background_music, stop_background_music # 从src.sound模块导入play_background_music和stop_background_music函数

def main() -> None:  # 定义主函数
    """Main function to run the Tic-Tac-Toe game."""  # 函数文档字符串
    # 初始化Pygame并创建屏幕
    pygame.init()  # 初始化pygame
    screen = pygame.display.set_mode((300, 300))  # 创建300x300像素的游戏窗口
    pygame.display.set_caption("Tic-Tac-Toe")  # 设置窗口标题为"Tic-Tac-Toe"
    print("Pygame initialized and screen created.")  # 打印初始化完成信息
    
    play_background_music() # 播放背景音乐

    # 创建Player对象
    player_x = Player('X')  # 创建玩家X
    player_o = Player('O')  # 创建玩家O
    print("Players X and O created.")  # 打印玩家创建完成信息

    # 创建GameBoard和GameState对象
    game_board = GameBoard()  # 创建游戏板
    game_state = GameState(player_x, player_o)  # 创建游戏状态
    print("GameBoard and GameState initialized.")  # 打印游戏板和游戏状态初始化完成信息

    # 游戏主循环
    while not game_state.game_over:  # 当游戏未结束时循环
        # 处理事件
        winner = handle_events(game_state, game_board)  # 处理游戏事件并获取赢家（如果有）

        # 更新屏幕
        update_screen(screen, game_board)  # 更新游戏屏幕显示

        # 检查游戏是否结束
        if game_state.game_over:  # 如果游戏结束
            if winner:  # 如果有赢家
                print(f"The winner is {winner}!")  # 打印赢家信息
            else:  # 如果没有赢家（平局）
                print("It's a draw!")  # 打印平局信息
            break  # 跳出游戏循环
    
    stop_background_music() # 停止背景音乐

    # 等待几秒后退出
    pygame.time.wait(3000)  # 等待3秒
    pygame.quit()  # 退出pygame
    print("Game ended. Pygame quit.")  # 打印游戏结束信息

if __name__ == "__main__":  # 如果这个脚本是作为主程序运行
    main()  # 调用main函数