import pygame 
import sys
from player import *
#from rain import Rain

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 700

pygame.display.set_caption("Meadow")

invisible_teleport= pygame.Rect(10, 450, 100, 150)
background = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\поляна1.png'),(WIDTH, HEIGHT))

font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)

star = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звезда.png'),(80, 80))
star_dark = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звездат.png'),(80, 80))


def Meadow(player):
    x = 10
    y = 480
    player.coord(x, y)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if player.player_rect.colliderect(invisible_teleport) and  event.key == pygame.K_LEFT:
                    from forest import Main
                    x = 600
                    y = 460
                    player.coord(x, y)
                    Main(player)
                if event.key == pygame.K_SPACE and player.types_name == 'umbrella':
                    from rain import Rain
                    Rain(player)
        screen.fill((0,0,0))
        screen.blit(background,(0, 0))
        screen.blit(star, (920,525))
        invisible_star_rect = pygame.Rect(950, 550, 20, 20)
        timer = font_small.render(str(player.timercounter), True, (255, 255, 255))
        screen.blit(timer, (10,10))
        #pygame.draw.rect(screen, (255,255,255), invisible_star_rect)
        if player.player_rect.colliderect(invisible_star_rect):
            screen.blit(star_dark,(920, 525))
        player.update()
        player.draw(screen)
        pygame.display.flip()
        clock.tick(30)
