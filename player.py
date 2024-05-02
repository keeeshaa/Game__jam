import pygame
import time
import sys

x = 0
y = 480
speed = 10
types2 = {
    'star' :{    
    "lumen" : pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда1.png'), (200, 200)),

    'walk_frames_left' : [
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда2.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда3.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда4.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда5.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда6.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звезда7.png'), (200, 200))
    ],

    "walk_frames_right" : [
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звездар2.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звездар3.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звездар4.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звездар5.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звездар6.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\star_animation\звездар7.png'), (200, 200))
    ]},

    "static" :

    {
    "lumen" : pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\player.png'), (200, 200)),

    'walk_frames_left' : [
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\1_move_left.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\2_move_left.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\3_move_left.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\4_move_left.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\5_move_left.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\6_move_left.png'), (200, 200))
    ],

    "walk_frames_right" : [
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\1_move_right.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\2_move_right.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\3_move_right.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\4_move_right.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\5_move_right.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\6_move_right.png'), (200, 200))
    ]
},
    "umbrella" : {
    "lumen" : pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист1.png'), (200, 200)),

    'walk_frames_left' : [
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист2 copy.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист3.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист4.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист5.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист6.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист7.png'), (200, 200))
    ],

    "walk_frames_right" : [
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр2.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр3.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр4.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр5.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр6.png'), (200, 200)),
        pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр7.png'), (200, 200))
    ]}
}

class Player1:
    def __init__(self, x , y , speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.check_time = 0
        self.types_name = 'static'
        self.player_rect = pygame.Rect(x, y, types2[self.types_name]['lumen'].get_width(), types2[self.types_name]['lumen'].get_height())
        self.walk_count = 0  
        self.last_update_time = pygame.time.get_ticks() 
        self.animation_delay = 100
        self.static_image = types2[self.types_name]['lumen']
        self.timercounter = 60

    def update(self):
        self.time123()
        if self.timercounter < 0:
            print("Game Over")
            pygame.quit() 
            sys.exit()   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.is_moving = True
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.is_moving = True
            self.direction = 'right'
        else:
            self.is_moving = False

        current_time = pygame.time.get_ticks()
        if self.is_moving and current_time - self.last_update_time > self.animation_delay:
            self.walk_count = (self.walk_count + 1) % len(types2[self.types_name]['walk_frames_left'])
            self.last_update_time = current_time

        self.player_rect.update(self.x, self.y, types2[self.types_name]['lumen'].get_width(), types2[self.types_name]['lumen'].get_height())
    def time123(self): 
        if(self.check_time != int(time.time())):
            self.check_time = int(time.time())
            self.timer()
    def change(self, type):
        self.types_name = type

    def timer(self):
        self.timercounter -= 1
    
    def give_timer(self):
        self.timercounter += 5
    
    def coord(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        if self.is_moving:
            if self.walk_count == 1:
                pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\main\sounds\walk.mp3').play()
            if self.direction == 'left':
                current_frame = types2[self.types_name]['walk_frames_left'][self.walk_count % len(types2[self.types_name]['walk_frames_left'])]
            elif self.direction == 'right':
                current_frame = types2[self.types_name]['walk_frames_right'][self.walk_count % len(types2[self.types_name]['walk_frames_right'])]
            screen.blit(current_frame, (int(self.x), int(self.y)))
        else:
            static_image = types2[self.types_name]['lumen']
            screen.blit(static_image, (int(self.x), int(self.y)))
