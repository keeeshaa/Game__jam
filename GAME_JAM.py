import pygame
from player import *
# from player import Player, Player_Star, Player_Umbrella
import sys


pygame.init()

SCREEN = pygame.display.set_mode((1000, 700))

pygame.display.set_caption("Long Night")
pygame.display.set_icon(pygame.image.load(r"D:\main\images\player.png"))
BG = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\меню.jpg")
BG = pygame.transform.scale(BG, (1000, 700))  # Изменяем размер изображения на размер экрана

player_img = pygame.transform.scale(pygame.image.load(r'D:\main\images\player.png'),(160,250))

x = 0
y = 440
speed = 10


def get_font(size): 
    return pygame.font.SysFont("comicsans", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(player_img, (850,450))
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        draw_text("LONG NIGHT", get_font(80), "#000000", SCREEN, 730, 425)

        # Draw buttons
        play_button_rect = pygame.Rect(700, 475, 200, 45)
        quit_button_rect = pygame.Rect(700, 525, 200, 45)

        #pygame.draw.rect(SCREEN, (215, 252, 212), play_button_rect)

        draw_text("PLAY", get_font(40), (0, 0, 0), SCREEN, 800, 500)
        draw_text("QUIT", get_font(40), (0, 0, 0), SCREEN, 800, 550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(4)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(MENU_MOUSE_POS):
                    from forest import Main
                    player = Player1(x, y, speed)
                    Main(player)
                if quit_button_rect.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()


