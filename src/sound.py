import pygame  # 导入pygame库

def play_background_music(file: str='data/background.mp3') -> None:
    """播放循环背景音乐。

    参数:
        file: 音乐文件的路径（例如：'background.mp3'）。
    """
    # 初始化声音混音器
    pygame.mixer.init()
    print(f"Pygame混音器已初始化。")

    # 加载音乐文件
    pygame.mixer.music.load(file)
    print(f"背景音乐'{file}'已加载。")

    # 循环播放音乐（-1表示无限循环）
    pygame.mixer.music.play(loops=-1)
    print(f"背景音乐开始循环播放。")

def stop_background_music() -> None:
    """停止背景音乐。"""
    pygame.mixer.music.stop()  # 停止音乐播放
    print(f"背景音乐已停止。")