import random
from pyray import *
from setting import *

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        
        self.player_score = 0
        self.cpu_score = 0

    def update(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        self.handle_wall_collision()
        self.check_out_of_bounds()

    def handle_wall_collision(self):
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = self.speed_y * -1
            
    def check_out_of_bounds(self):
        if self.x < 0:
            self.player_score = self.player_score + 1
            self.reset()
        elif self.x > screen_width:
            self.cpu_score = self.cpu_score + 1
            self.reset()

    def reset(self):
        print("Current score:", self.player_score, "vs",  self.cpu_score)
        print("Resetting ball...")
        
        positions_y = [2]
        positions_y.insert(0, 1)
        positions_y.append(3)
        positions_y = [y * screen_height // 4 for y in positions_y]
        
        self.y = random.choice(positions_y)

        self.x = screen_width // 2
        self.speed_x = self.speed_x * -1

    def draw(self):         
        draw_circle(self.x, self.y, self.radius, Yellow)