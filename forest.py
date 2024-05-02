import pygame
import sys
import random
from maze_main import maze
from player import *
pygame.init()

clock = pygame.time.Clock()

#pygame.mixer.Sound(r'').play() #background sound

invisible_enter_rect = pygame.Rect(720, 450, 100, 100)
invisible_meadow_rect = pygame.Rect(1000, 450, 1, 100)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

atmo = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\light.png')

back = {
    1 : pygame.transform.scale(pygame.image.load(r'D:\main\images\forest\forest_day2.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    2 : pygame.transform.scale(pygame.image.load(r'D:\main\images\forest\forest_day1.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    3 : pygame.transform.scale(pygame.image.load(r'D:\main\images\forest\forest.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
}
enter = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\деревосвет.png')
enter = pygame.transform.scale(enter, (SCREEN_WIDTH, SCREEN_HEIGHT))



font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)

#Buttons
up = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\вверх.png'),(750,750))
down = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\вниз.png'),(750,750))
right = pygame.transform.scale(pygame.image.load(r'D:\main\images\вправо.png'),(750,750))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


class MovingImage:
    def __init__(self):
        self.x = random.randint(-30, SCREEN_WIDTH - 30)
        self.y = random.randint(-30, SCREEN_HEIGHT - 30)
        self.speed_x = random.randint(1, 2) or random.randint(-1, 0)  # Случайная скорость по оси X
        self.speed_y = random.randint(-1, 0) or random.randint(1, 2) # Случайная скорость по оси Y

    def update(self):
        # Движение изображения
        self.x += self.speed_x
        self.y += self.speed_y


    def draw(self):
        screen.blit(atmo, (self.x, self.y))


objects = []


def Main(player):
    running = True
    while running:

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if player.player_rect.colliderect(invisible_enter_rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        from tree_main import Tree
                        Tree(player)
                    if event.key == pygame.K_DOWN:
                        from den import Den
                        Den(player)
            if player.player_rect.colliderect(invisible_meadow_rect):
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_RIGHT:
                        from meadow import Meadow
                        Meadow(player)

        # Generate new objects randomly
        if random.random() < 0.012:
            new_object = MovingImage()
            objects.append(new_object)

        screen.fill((0,0,0))
        if player.timercounter <= 20:
            screen.blit(back[3], (0, 0))
        elif 20 < player.timercounter and player.timercounter <= 40:
            screen.blit(back[2], (0, 0))
        else: 
            screen.blit(back[1], (0, 0)) 

        #player_rect = pygame.Rect(x, y, 200, 200)  # Прямоугольник для игрока
        if player.player_rect.colliderect(invisible_enter_rect):
            screen.blit(enter, (0, 0))
            screen.blit(up,(300,70))
            screen.blit(down,(300,70))

        if player.player_rect.colliderect(invisible_meadow_rect):
            screen.blit(right, (300,70))
        player.update()
        player.draw(screen)
        #pygame.draw.rect(screen, (255,255,255), invisible_meadow_rect)
        #pygame.draw.rect(screen, (255,255,255), invisible_enter_rect)
        #pygame.draw.rect(screen, (215, 252, 212), up_button_rect)
        #pygame.draw.rect(screen, (215, 252, 212), down_button_rect)

        for obj in objects:
            obj.update()
            obj.draw()
        # Draw the main character on top
        # Draw the player character
        timer = font_small.render(str(player.timercounter), True, (255, 255, 255))
        screen.blit(timer, (10,10))
        pygame.display.update()
        clock.tick(30)



        

