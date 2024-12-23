from pyray import *
from raylib import KEY_DOWN, KEY_UP

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def update(self):
        if is_key_down(KEY_UP) and self.y > 0:
            self.y -= self.speed
        if is_key_down(KEY_DOWN) and self.y + self.height < 800:
            self.y += self.speed

    def draw(self):
        draw_rectangle(self.x, self.y, self.width, self.height, WHITE)