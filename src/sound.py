"""Optional game music; absence of an audio device is not fatal."""
from pathlib import Path
import pygame

DEFAULT_MUSIC = Path(__file__).resolve().parents[1] / "data" / "background.mp3"

def play_background_music(file=None) -> bool:
    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        pygame.mixer.music.load(str(file or DEFAULT_MUSIC))
        pygame.mixer.music.play(loops=-1)
        return True
    except (pygame.error, OSError):
        # e.g. headless runner with no audio backend or missing local asset
        return False

def stop_background_music() -> None:
    if pygame.mixer.get_init() is not None:
        pygame.mixer.music.stop()
