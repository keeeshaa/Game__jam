import pygame 
import sys
from player import *
#from rain import Rain

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 700


invisible_teleport= pygame.Rect(0, 450, 1, 150)
back = {
    1 : pygame.transform.scale(pygame.image.load(r'D:\main\images\meadow\meadow_day2.png'), (WIDTH, HEIGHT)),
    2 : pygame.transform.scale(pygame.image.load(r'D:\main\images\meadow\meadow_day1.png'), (WIDTH, HEIGHT)),
    3 : pygame.transform.scale(pygame.image.load(r'D:\main\images\meadow\meadow.png'), (WIDTH, HEIGHT))
}

font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)

star = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звезда.png'),(80, 80))
star_dark = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звездат.png'),(80, 80))
left = pygame.transform.scale(pygame.image.load(r'D:\main\images\влево.png'),(100,100))

def Meadow(player):
    x = 10
    y = 480
    player.coord(x, y)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    flag = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    flag = not flag
                if player.player_rect.colliderect(invisible_teleport) and  event.key == pygame.K_LEFT and flag:
                    from forest import Main
                    x = 920
                    y = 460
                    player.coord(x, y)
                    Main(player)
                if event.key == pygame.K_SPACE and player.types_name == 'umbrella' and player.rain == 0 and flag:
                    from rain import Rain
                    player.rain = 15
                    Rain(player)
        if flag:
            screen.fill((0,0,0))
            if player.timercounter <= 20:
                screen.blit(back[3], (0, 0))
            elif 20 < player.timercounter and player.timercounter <= 40:
                screen.blit(back[2], (0, 0))
            else: 
                screen.blit(back[1], (0, 0)) 

            screen.blit(star, (920,525))
            invisible_star_rect = pygame.Rect(950, 550, 20, 20)
            timer = font_small.render(str(player.timercounter), True, (255, 255, 255))
            screen.blit(timer, (10,10))
            #pygame.draw.rect(screen, (255,255,255), invisible_star_rect)
            if player.player_rect.colliderect(invisible_star_rect):
                screen.blit(star_dark,(920, 525))

            if player.player_rect.colliderect(invisible_teleport):
                screen.blit(left, (0, 400))
            player.update()
            player.draw(screen)
            pygame.display.flip()
            clock.tick(30)
        else: 
            from pause import display_pause_message
            display_pause_message(screen, pygame.font.Font(None, 45), WIDTH ,HEIGHT)
