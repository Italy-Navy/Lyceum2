#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import pygame
from pygame import *

PLATFORM_WIDTH = 10
PLATFORM_HEIGHT = 10
PLATFORM_COLOR = "#FF6262"


def load_image(name, directory, colorkey=None):
    fullname = os.path.join(directory, name)
    koef = 20
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (koef, koef))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = load_image("wall.png", "data/assets", colorkey=True)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Empty(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = load_image("empty.png", "data/assets", colorkey=True)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

# class Water(sprite.Sprite):
#    def __init__(self, x, y):
#        sprite.Sprite.__init__(self)
##        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
#       self.image.fill(Color(PLATFORM_COLOR))
#       self.image = load_image("water.png", "assets", colorkey=True)
#       self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
