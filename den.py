import pygame
import sys
from player import *

#from counter import Counter

pygame.init()


invisible_eng_rect = pygame.Rect(240, 500, 50, 175)
invisible_umb_rect = pygame.Rect(700, 600, 25, 50)
invisible_back_rect = pygame.Rect(500,250,50,50)

took_umbrella = False

clock = pygame.time.Clock()
WIDTH = 1000
HEIGHT= 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Den")

font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)

umb = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\лист.png'),(400,400))
umb_light = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\листсвет.png'),(400,400))

pers = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\player.png')
pers = pygame.transform.scale(pers, (200, 200))

background = pygame.transform.scale(pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\пещера.png"),(WIDTH, HEIGHT))

eng_light = pygame.transform.scale(pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\пещерасвет.png"),(WIDTH,HEIGHT))

up_button = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\up_button.png'),(50,50))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


def Den(player):
    x = 400
    y = 450
    player.coord(x, y)
    
    global took_umbrella

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                from forest import Main
                x = 500
                y = 600
                Main(player)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.player_rect.colliderect(invisible_umb_rect):
                    # При нажатии пробела и коллизии с зонтиком
                    took_umbrella = True  # Персонаж взял зонтик
                    player.change('umbrella')
                    player.coord(x, y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.player_rect.colliderect(invisible_eng_rect) and player.types_name == 'star':
                        took_umbrella = False
                        pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\main\sounds\catch (1).mp3').play()
                        player.change('static')
                        player.give_timer()
                        

            

        screen.fill((0,0,0))
        screen.blit(background,(0, 0))
        #pygame.draw.rect(screen, (255,255,255), invisible_back_rect)
        screen.blit(up_button,(500,250))
        

        #pygame.draw.rect(screen, (255,255,255), invisible_eng_rect)
        #pygame.draw.rect(screen, (255,255,255), invisible_umb_rect)

        player.update()
        
        timer = font_small.render(str(player.timercounter), True, (255, 255, 255))
        screen.blit(timer, (10,10))

        player.draw(screen)
        if not took_umbrella:
            screen.blit(umb, (500, 325))
        
        if player.player_rect.colliderect(invisible_eng_rect):
            screen.blit(eng_light,(0,0))
            

        if player.player_rect.colliderect(invisible_umb_rect):
            if not took_umbrella:
                screen.blit(umb_light,(500,325))
                took_button_rect = pygame.Rect(750, 600, 150, 50)
                pygame.draw.rect(screen, (255, 255, 255), took_button_rect)
                draw_text("TAKE", get_font(30), (0, 0, 0), screen, 825, 625)
        pygame.display.flip()
        clock.tick(30)