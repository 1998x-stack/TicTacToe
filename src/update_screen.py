import pygame  # 导入pygame库

def update_screen(screen: pygame.Surface, game_board: 'GameBoard') -> None:
    """更新游戏屏幕，重绘游戏板并刷新显示。

    此函数清空屏幕，绘制当前游戏板状态，并更新显示。

    参数：
        screen: 用于绘制游戏的Pygame表面。
        game_board: 表示当前游戏状态的GameBoard实例。
    """
    # 通过填充背景色（例如白色）来清空屏幕
    screen.fill((255, 255, 255))
    print("屏幕已清空并填充背景色。")

    # 在屏幕上绘制游戏板
    game_board.draw_board(screen)
    print("游戏板已绘制在屏幕上。")

    # 刷新显示以显示更新后的屏幕
    pygame.display.flip()
    print("显示已刷新。")