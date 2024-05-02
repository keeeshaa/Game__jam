import pygame
import sys
from pygame.locals import *
import random
from player import *

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 7

#Setting up Fonts
font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)
game_over = font.render("Game Over", True, WHITE)
game_win = font.render("You win!!!", True, WHITE)
#pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\main\sounds\area12-131883.mp3').play() 

background = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\background_rain.JPG'),(401, 605)) #background image
invisible_line_y = 550

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Save the stars")


class drop(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\rain.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20,SCREEN_WIDTH-20), 0) 

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
    
      def respawn(self):
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)


#Creating a player's sprite and functions for it
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\pixel_sprite_rain.png'),(70,90))# image of the player's sprite
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    #Function to move the sprite
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-8, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(8, 0)
                  

#Setting up Sprites        
P1 = Player()
D1 = drop()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
drops = pygame.sprite.Group()
drops.add(D1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(D1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

#Game Loop
def Rain(player):
    SCORE = 0
    SPEED = 7
    while True:
        #Cycles through all events occuring  
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                  SPEED += 0.5      
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        DISPLAYSURF.blit(background, (0,0))
        scores = font_small.render(str(SCORE), True, WHITE)
        DISPLAYSURF.blit(scores, (10,10))
        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)
        for entity in drops:
            if entity.rect.bottom > invisible_line_y:
                DISPLAYSURF.blit(game_over, (30, 250))
                pygame.display.update() 
                pygame.time.delay(1000)
                pygame.quit()
                from meadow import Meadow
                Meadow(player)
        
        if pygame.sprite.spritecollideany(P1, drops):
              pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\main\sounds\voda-kaplya-odinochnyiy-korotkiy-myagkiy-blizkiy.mp3').play()
              SCORE += 1  
              for entity in drops:
                    entity.respawn() 
              pygame.display.update()
        pygame.display.update()
        if SCORE == 20:
            DISPLAYSURF.blit(game_win, (30, 250))  
            pygame.display.update()  
            pygame.time.delay(1000)
            from meadow import Meadow
            x = 600
            y = 500
            player.change('star')
            player.coord(x, y)
            Meadow(player)
    
        FramePerSec.tick(FPS)
