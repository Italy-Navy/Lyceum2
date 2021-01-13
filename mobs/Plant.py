from pygame import *
from hero import playanim as pyganim
import os

MOVE_SPEED = 1
WIDTH = 51
HEIGHT = 48
COLOR = "#888888"
GRAVITY = 0.35
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

IDLE = [
    ('%s/../data/animations/plant/idle/1.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/2.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/3.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/4.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/5.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/6.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/7.png' % ICON_DIR),
    ('%s/../data/animations/plant/idle/8.png' % ICON_DIR)
]

HIT = [
    ('%s/../data/animations/plant/hit/1.png' % ICON_DIR),
    ('%s/../data/animations/plant/hit/2.png' % ICON_DIR),
    ('%s/../data/animations/plant/hit/3.png' % ICON_DIR)
]

ATTACK_LEFT = [
    ('%s/../data/animations/plant/attack_left/1.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/2.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/3.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/4.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/5.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/6.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/7.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_left/8.png' % ICON_DIR)
]

ATTACK_RIGHT = [
    ('%s/../data/animations/plant/attack_right/1.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/2.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/3.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/4.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/5.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/6.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/7.png' % ICON_DIR),
    ('%s/../data/animations/plant/attack_right/8.png' % ICON_DIR)
]


class Plant(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.POSITION_RIGHT = True
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH + 10, HEIGHT + 20))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT + 15)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо

        boltAnim = []
        for anim in IDLE:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltIdle = pyganim.PygAnimation(boltAnim)
        self.boltIdle.play()

        boltAnim = []
        for anim in HIT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltHit = pyganim.PygAnimation(boltAnim)
        self.boltHit.play()

        boltAnim = []
        for anim in ATTACK_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAttackLeft = pyganim.PygAnimation(boltAnim)
        self.boltAttackLeft.play()

        boltAnim = []
        for anim in ATTACK_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAttackRight = pyganim.PygAnimation(boltAnim)
        self.boltAttackRight.play()

    def plant_behavior(self, hero_x, hero_y, platforms):
        if int(hero_y) - 15 == self.rect.y and 0 <= int(hero_x) - int(self.startX) <= 50:
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = False
            self.boltAttackLeft.blit(self.image, (0, 0))
        elif int(hero_y) - 15 == self.rect.y and -45 <= int(hero_x) - int(self.startX) <= 0:
            self.xvel = 0
            self.POSITION_RIGHT = True
            self.image.fill(Color(COLOR))
            self.boltAttackRight.blit(self.image, (0, 0))
        else:
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.boltIdle.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает