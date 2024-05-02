import pygame

pygame.font.init()

class Game:
    def __init__(self, goal_cell, tile):
        self.font = pygame.font.SysFont("comicsans", 35)
        self.message_color = pygame.Color("white")
        self.goal_cell = goal_cell
        self.tile = tile
        self.start_time = None
        self.game_duration = 45

    # add goal point for player to reach
    def add_goal_point(self, screen):
        # adding gate for the goal point
        img_path = r'C:\Users\Admin\Desktop\pp2\main\images\star.png'
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (self.tile, self.tile))
        screen.blit(img, (self.goal_cell.x * self.tile, self.goal_cell.y * self.tile))

    # winning message
    def message(self):
        msg = self.font.render('You Win!', True, self.message_color)
        return msg

    # checks if player reached the goal point
    def is_game_over(self, player):
        goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * self.tile, self.goal_cell.y * self.tile
        if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
            return True
        else:
            return False
        
    def start_timer(self):
        self.start_time = pygame.time.get_ticks() / 1000  # Преобразование миллисекунд в секунды

    # Проверка, истекло ли время
    def is_time_up(self):
        if self.start_time is not None:
            current_time = pygame.time.get_ticks() / 1000  # Текущее время в секундах
            elapsed_time = current_time - self.start_time
            return elapsed_time >= self.game_duration
        return False