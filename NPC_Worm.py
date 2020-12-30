from pygame import *
import playanim as pyganim
import os

MOVE_SPEED = 1
WIDTH = 15
HEIGHT = 48
COLOR = "#888888"
GRAVITY = 0.35
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
RUN = [
    ('%s/data/animations/npc_worm/movement/1.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/movement/2.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/movement/3.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/movement/4.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/movement/5.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/movement/6.png' % ICON_DIR)
]

IDLE_RIGHT = [
    ('%s/data/animations/npc_worm/idle_right/1.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/2.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/3.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/4.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/5.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/6.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/7.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/8.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_right/9.png' % ICON_DIR)
]

IDLE_LEFT = [
    ('%s/data/animations/npc_worm/idle_left/1.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/2.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/3.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/4.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/5.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/6.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/7.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/8.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/idle_left/9.png' % ICON_DIR),
]

HIT = [
    ('%s/data/animations/npc_worm/hit/1.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/hit/2.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/hit/3.png' % ICON_DIR)
]

ATTACK = [
    ('%s/data/animations/npc_worm/attack/1.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/attack/2.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/attack/3.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/attack/4.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/attack/5.png' % ICON_DIR),
    ('%s/data/animations/npc_worm/attack/6.png' % ICON_DIR)
]


class Worm(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.POSITION_RIGHT = True
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH + 10, HEIGHT + 15))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT + 15)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо

        boltAnim = []
        for anim in RUN:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltRun = pyganim.PygAnimation(boltAnim)
        self.boltRun.play()

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
        for anim in HIT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltHit = pyganim.PygAnimation(boltAnim)
        self.boltHit.play()

        boltAnim = []
        for anim in ATTACK:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAttack = pyganim.PygAnimation(boltAnim)
        self.boltAttack.play()

    def worm_behavior(self, hero_x, hero_y, platforms):
        if -1000 <= int(self.rect.x) - int(hero_x) <= 1000:
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = True
            self.boltIdleRight.blit(self.image, (0, 0))
        elif -1000 <= int(self.rect.x) - int(hero_x) <= 0:
            self.xvel = 0
            self.POSITION_RIGHT = False
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