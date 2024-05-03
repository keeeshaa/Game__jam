import pygame

pygame.init()

def display_pause_message(screen, font, WINDOW_WIDTH, WINDOW_HEIGHT):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen.fill(BLACK)
    pause_text = font.render("пауза", True, WHITE)
    text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    screen.blit(pause_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(30)