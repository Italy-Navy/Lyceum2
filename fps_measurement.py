import sys

import pygame
from pygame import *
import os

MOVE_SPEED = 1
WIDTH = 120
HEIGHT = 15
COLOR = "#888888"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class fps_measure(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        self.font = pygame.font.SysFont('Comic Sans MS', 10)

    def update_fps(self, fps, camera_x):
        self.image.fill(Color(COLOR))
        fps_label = self.font.render(str("fps:"), False, (255, 255, 255))
        self.image.blit(fps_label, (0, 0))
        fps_label = self.font.render(str(fps), False, (255, 255, 255))
        self.image.blit(fps_label, (20, 0))
        self.rect.x = abs(camera_x) + 1220
