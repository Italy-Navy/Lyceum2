from pygame import *
import playanim as pyganim
import os

MOVE_SPEED = 5
WIDTH = 51
HEIGHT = 48
COLOR = "#888888"
JUMP_POWER = 9
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ANIMATION_DELAY_ATTACK = 0.05  # скорость смены кадров
ANIMATION_DELAY_JUMP = 0.15  # скорость смены кадров прыжков
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
RUN_RIGHT = [
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

RUN_LEFT = [
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

IDLE_RIGHT = [
    ('%s/data/animations/Main_Hero/idle_r/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_r/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_r/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_r/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_r/1.png' % ICON_DIR),
]

IDLE_LEFT = [
    ('%s/data/animations/Main_Hero/idle_l/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_l/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_l/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_l/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/idle_l/1.png' % ICON_DIR),
]

JUMP_RIGHT = [
    ('%s/data/animations/Main_Hero/idle_r/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_r/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_r/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_r/5.png' % ICON_DIR),
]

JUMP_LEFT = [
    ('%s/data/animations/Main_Hero/idle_l/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_l/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_l/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/jump_l/5.png' % ICON_DIR),
]

ATTACK_RIGHT = [
    ('%s/data/animations/Main_Hero/attack_r/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_r/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_r/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_r/5.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_r/6.png' % ICON_DIR),
]

ATTACK_LEFT = [
    ('%s/data/animations/Main_Hero/attack_l/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_l/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_l/4.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_l/5.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/attack_l/6.png' % ICON_DIR),
]

CROUCH_RIGHT = [
    ('%s/data/animations/Main_Hero/crouch_r/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_r/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_r/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_r/1.png' % ICON_DIR),
]

CROUCH_LEFT = [
    ('%s/data/animations/Main_Hero/crouch_l/1.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_l/3.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_l/2.png' % ICON_DIR),
    ('%s/data/animations/Main_Hero/crouch_l/1.png' % ICON_DIR),
]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.POSITION_RIGHT = True
        self.attack = False
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.flag_attack_left = False
        self.image = Surface((WIDTH + 50, HEIGHT))
        self.image.fill(Color(COLOR))
        self.return_update = 0
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
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
        for anim in JUMP_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY_JUMP))
        self.boltJumpRight = pyganim.PygAnimation(boltAnim)
        self.boltJumpRight.play()

        boltAnim = []
        for anim in JUMP_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY_JUMP))
        self.boltJumpLeft = pyganim.PygAnimation(boltAnim)
        self.boltJumpLeft.play()

        boltAnim = []
        for anim in ATTACK_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY_ATTACK))
        self.boltAttackRight = pyganim.PygAnimation(boltAnim)
        self.boltAttackRight.play()

        boltAnim = []
        for anim in ATTACK_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY_ATTACK))
        self.boltAttackLeft = pyganim.PygAnimation(boltAnim)
        self.boltAttackLeft.play()

        boltAnim = []
        for anim in CROUCH_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltCrouchRight = pyganim.PygAnimation(boltAnim)
        self.boltCrouchRight.play()

        boltAnim = []
        for anim in CROUCH_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltCrouchLeft = pyganim.PygAnimation(boltAnim)
        self.boltCrouchLeft.play()

    def update(self, x, y, left, right, up, attack, platforms):
        self.attack = attack
        if self.flag_attack_left and not attack:
            self.rect = Rect(int(x + 30), int(y), int(WIDTH), int(HEIGHT))  # прямоугольный объект
            self.flag_attack_left = False
            self.return_update = 0

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                if self.POSITION_RIGHT:
                    self.boltIdleRight.blit(self.image, (0, 0))
                else:
                    self.boltIdleLeft.blit(self.image, (0, 0))

        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            if self.POSITION_RIGHT:
                self.boltJumpRight.blit(self.image, (0, 0))
            else:
                self.boltJumpLeft.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = False
            if up:
                self.boltJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltRunLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = True
            if up:
                self.boltJumpRight.blit(self.image, (0, 0))
            else:
                self.boltRunRight.blit(self.image, (0, 0))

        if attack:
            self.image.fill(Color(COLOR))
            if self.POSITION_RIGHT:
                self.boltAttackRight.blit(self.image, (0, 0))
            else:
                if not self.flag_attack_left:
                    self.xvel -= 30
                    self.flag_attack_left = True
                    self.return_update = 30
                self.boltAttackLeft.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
        return self.return_update

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

    def get_x_y(self):
        s = str(self.rect)
        s_arr = s[6:-2].split(',')
        x_sr = (int(s_arr[0]) + int(s_arr[0])) / 2
        if self.flag_attack_left and self.attack:
            x_sr += 30
        return int(x_sr), int(s_arr[0]), int(s_arr[1])
