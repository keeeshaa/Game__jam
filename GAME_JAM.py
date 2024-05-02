import pygame
from player import *
# from player import Player, Player_Star, Player_Umbrella
import sys


pygame.init()

SCREEN = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\меню.jpg")
BG = pygame.transform.scale(BG, (1000, 700))  # Изменяем размер изображения на размер экрана


x = 0
y = 440
speed = 10

# Загрузка музыки
menu_music = pygame.mixer.Sound(r"C:\Users\Admin\Desktop\pp2\main\sounds\area12-131883.mp3")
#game_music = pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\main\sounds\Magic Melody - Es the Storyteller_(bomb-music.ru).mp3')
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    menu_music.play(-1) 
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        draw_text("LONG NIGHT", get_font(100), "#000000", SCREEN, 750, 425)

        # Draw buttons
        play_button_rect = pygame.Rect(700, 475, 200, 45)
        quit_button_rect = pygame.Rect(700, 525, 200, 45)

        #pygame.draw.rect(SCREEN, (215, 252, 212), play_button_rect)

        draw_text("PLAY", get_font(50), (0, 0, 0), SCREEN, 800, 500)
        draw_text("QUIT", get_font(50), (0, 0, 0), SCREEN, 800, 550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(4)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(MENU_MOUSE_POS):
                    menu_music.stop()  # Остановка музыки перед запуском игры
                    #game_music.play(-1)
                    from forest import Main
                    player = Player1(x, y, speed)
                    Main(player)
                if quit_button_rect.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()


