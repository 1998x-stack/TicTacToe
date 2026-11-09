"""Render the board and optional footer status."""
import pygame

def update_screen(screen: pygame.Surface, game_board: 'GameBoard', status=None) -> None:
    screen.fill((255, 255, 255))
    game_board.draw_board(screen)
    if status is not None:
        pygame.draw.rect(screen, (24, 34, 49), pygame.Rect(0, 300, 300, 44))
        label = pygame.font.Font(None, 26).render(status, True, (237, 248, 255))
        screen.blit(label, (8, 310))
    pygame.display.flip()
