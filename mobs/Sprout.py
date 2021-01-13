from pygame import *
from hero import playanim as pyganim
import os

MOVE_SPEED = 1
WIDTH = 15
HEIGHT = 48
COLOR = "#888888"
GRAVITY = 0.35
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
RUN_RIGHT = [
    ('%s/../data/animations/sprout/run_right/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_right/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_right/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_right/4.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_right/5.png' % ICON_DIR)
]

RUN_LEFT = [
    ('%s/../data/animations/sprout/run_left/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_left/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_left/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_left/4.png' % ICON_DIR),
    ('%s/../data/animations/sprout/run_left/5.png' % ICON_DIR)
]

IDLE_RIGHT = [
    ('%s/../data/animations/sprout/idle_right/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/idle_right/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/idle_right/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/idle_right/4.png' % ICON_DIR)
]

IDLE_LEFT = [
    ('%s/../data/animations/sprout/idle_left/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/idle_left/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/idle_left/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/idle_left/4.png' % ICON_DIR)
]

HIT_RIGHT = [
    ('%s/../data/animations/sprout/hit_right/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_right/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_right/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_right/4.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_right/5.png' % ICON_DIR)
]

HIT_LEFT = [
    ('%s/../data/animations/sprout/hit_left/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_left/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_left/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_left/4.png' % ICON_DIR),
    ('%s/../data/animations/sprout/hit_left/5.png' % ICON_DIR)
]

ATTACK_LEFT = [
    ('%s/../data/animations/sprout/attack_left/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_left/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_left/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_left/4.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_left/5.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_left/6.png' % ICON_DIR)
]

ATTACK_RIGHT = [
    ('%s/../data/animations/sprout/attack_right/1.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_right/2.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_right/3.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_right/4.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_right/5.png' % ICON_DIR),
    ('%s/../data/animations/sprout/attack_right/6.png' % ICON_DIR)
]


class Sprout(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.POSITION_RIGHT = False
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH + 65, HEIGHT + 30))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT + 30)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо

        boltAnim = []
        for anim in RUN_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltRunRight = pyganim.PygAnimation(boltAnim)
        self.boltRunRight.play()

        boltAnim = []
        for anim in RUN_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltRunLeft = pyganim.PygAnimation(boltAnim)
        self.boltRunLeft.play()

        boltAnim = []
        for anim in IDLE_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltIdleRight = pyganim.PygAnimation(boltAnim)
        self.boltIdleRight.play()

        boltAnim = []
        for anim in IDLE_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltIdleLeft = pyganim.PygAnimation(boltAnim)
        self.boltIdleLeft.play()

        boltAnim = []
        for anim in HIT_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltHitLeft = pyganim.PygAnimation(boltAnim)
        self.boltHitLeft.play()

        boltAnim = []
        for anim in HIT_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltHitRight = pyganim.PygAnimation(boltAnim)
        self.boltHitRight.play()

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

    def sprout_behavior(self, hero_x, hero_y, platforms):
        if -50 <= int(hero_y) - 30 - self.rect.y <= 50 and 20 <= int(hero_x) - (int(self.rect.x) + 10) <= 60 \
                and self.POSITION_RIGHT:
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = True
            self.boltAttackRight.blit(self.image, (0, 0))
        elif -50 <= int(hero_y) - 30 - self.rect.y <= 50 and -10 <= int(hero_x) - int(self.rect.x) <= 20 \
                and not self.POSITION_RIGHT:
            self.xvel = 0
            self.POSITION_RIGHT = False
            self.image.fill(Color(COLOR))
            self.boltAttackLeft.blit(self.image, (0, 0))
        elif -50 <= int(hero_y) - 30 - self.rect.y <= 50 and -400 <= int(hero_x) - int(self.rect.x) <= 0:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = False
            self.boltRunLeft.blit(self.image, (0, 0))
        elif -50 <= int(hero_y) - 30 - self.rect.y <= 50 and 0 <= int(hero_x) - int(self.rect.x) <= 400:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = True
            self.boltRunRight.blit(self.image, (0, 0))
        elif self.POSITION_RIGHT:
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.boltIdleRight.blit(self.image, (0, 0))
        elif not self.POSITION_RIGHT:
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.boltIdleLeft.blit(self.image, (0, 0))

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
