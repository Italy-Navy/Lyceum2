from pygame import *
import playanim as pyganim
import os

MOVE_SPEED = 5
WIDTH = 51
HEIGHT = 48
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.07  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
ANIMATION_RIGHT = [
    ('%s/data/animations/Main_Hero/run_r/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/5.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/6.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/7.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/8.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/9.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/10.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/11.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_r/12.png' % ICON_DIR),
]

ANIMATION_LEFT = [
    ('%s/data/animations/Main_Hero/run_l/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/5.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/6.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/7.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/8.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/9.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/10.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/11.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/run_l/12.png' % ICON_DIR),
]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
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
