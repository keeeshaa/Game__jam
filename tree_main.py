import pygame 
import sys
from player import *
import random
from maze_main import maze

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tree")

font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)

background = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\tree.jpeg'),(WIDTH, HEIGHT))

atmo = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\light.png')

star = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звезда.png'),(80, 80))
star_dark = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звездат.png'),(80, 80))

def get_font(size): 
    return pygame.font.SysFont("minecraft.otf", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)



class MovingImage:
    def __init__(self):
        self.x = random.randint(-30, WIDTH - 30)
        self.y = random.randint(-30, HEIGHT - 30)
        self.speed_x = random.randint(1, 2) or random.randint(-1, 0)  
        self.speed_y = random.randint(-1, 0) or random.randint(1, 2) 

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y


    def draw(self):
        screen.blit(atmo, (self.x, self.y))


objects = []


def Tree(player):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    x = 800
    y = 450
    player.coord(x, y)
    running = True
    while running:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    from forest import Main
                    Main(player)
                if event.key == pygame.K_SPACE:
                    if player.player_rect.colliderect(invisible_star_rect):
                        maze(player)

        screen.fill((0,0,0))
        screen.blit(background,(0, 0))
        invisible_star_rect = pygame.Rect(30, 450, 20, 20)
        screen.blit(star, (10,425))
        #pygame.draw.rect(screen, (255,255,255), invisible_star_rect)

        if player.player_rect.colliderect(invisible_star_rect):
            screen.blit(star_dark,(10, 425))

        player.update()
        player.draw(screen)

        if random.random() < 0.012:
            new_object = MovingImage()
            objects.append(new_object)
        for obj in objects:
            obj.update()
            obj.draw()
        timer = font_small.render(str(player.timercounter), True, (255, 255, 255))
        screen.blit(timer, (10,10))
        pygame.display.flip()
        clock.tick(30)


