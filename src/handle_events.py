import pygame
from typing import Optional

def handle_events(game_state: 'GameState', game_board: 'GameBoard') -> Optional[str]:
    """处理用户输入事件并相应地更新游戏状态。"""
    
    for event in pygame.event.get():  # 遍历所有待处理的事件
        if event.type == pygame.QUIT:  # 如果事件类型是退出
            pygame.quit()  # 退出pygame
            exit()  # 退出程序
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # 如果事件类型是鼠标按下
            x, y = event.pos  # 获取鼠标点击位置的坐标
            print(f"鼠标点击位置：({x}, {y})")  # 打印鼠标点击位置
            
            # 将屏幕坐标转换为棋盘行列
            row = y // 100  # 计算行号
            col = x // 100  # 计算列号
            print(f"点击转换为棋盘坐标：({row}, {col})")  # 打印棋盘坐标

            # 确保点击在有效的网格区域内
            if 0 <= row < 3 and 0 <= col < 3:  # 检查行列是否在有效范围内
                # 尝试进行移动
                if game_state.current_player.make_move(game_board, row, col):  # 如果当前玩家成功下棋
                    # 检查游戏是否结束（胜利或平局）
                    winner = game_state.check_game_over(game_board)  # 检查是否有胜者
                    if winner:  # 如果有胜者
                        print(f"游戏结束！胜者：{winner}")  # 打印胜者信息
                        return winner  # 返回胜者
                    elif game_state.game_over:  # 如果游戏结束但没有胜者（平局）
                        print("游戏结束！平局。")  # 打印平局信息
                        return None  # 返回None表示平局
                    
                    # 如果游戏未结束，切换玩家
                    game_state.switch_player()  # 切换到下一个玩家
            else:  # 如果点击在有效区域外
                print("点击位置在有效网格区域外。")  # 打印提示信息
    
    return None  # 如果没有发生任何导致游戏结束的事件，返回None