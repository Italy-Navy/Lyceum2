from pygame import *
import playanim as pyganim
import os

COLOR = "#888888"
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
        # ____________________________-HERO FEATURES-______________________________

        self.MOVE_SPEED = 4
        self.JUMP_POWER = 7
        self.GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
        self.health_points = 250

        # ____________________________-HERO FEATURES-______________________________

        self.WIDTH = 30
        self.HEIGHT = 48

        self.ANIMATION_DELAY = 0.1  # скорость смены кадров
        self.ANIMATION_DELAY_ATTACK = 0.15  # скорость смены кадров
        self.ANIMATION_DELAY_JUMP = 0.15  # скорость смены кадров прыжков
        self.ANIMATION_DELAY_CROUCH = 0.3

        # _________________________________-FLAG-_________________________________

        self.POSITION_RIGHT = True
        self.onGround = False  # На земле ли я?

        self.hero_attack = False
        self.flag_attack_left = False

        self.on_attack = False

        self.flag_ability = True

        # _________________________________-FLAG-_________________________________

        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения

        self.image = Surface((self.WIDTH + 50, self.HEIGHT))
        self.image.fill(Color(COLOR))
        self.return_update = 0
        self.rect = Rect(x, y, self.WIDTH, self.HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным

        #        Анимация движения вправо
        boltAnim = []
        for anim in RUN_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltRunRight = pyganim.PygAnimation(boltAnim)
        self.boltRunRight.play()

        boltAnim = []
        for anim in RUN_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltRunLeft = pyganim.PygAnimation(boltAnim)
        self.boltRunLeft.play()

        boltAnim = []
        for anim in IDLE_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltIdleRight = pyganim.PygAnimation(boltAnim)
        self.boltIdleRight.play()

        boltAnim = []
        for anim in IDLE_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltIdleLeft = pyganim.PygAnimation(boltAnim)
        self.boltIdleLeft.play()

        boltAnim = []
        for anim in JUMP_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_JUMP))
        self.boltJumpRight = pyganim.PygAnimation(boltAnim)
        self.boltJumpRight.play()

        boltAnim = []
        for anim in JUMP_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_JUMP))
        self.boltJumpLeft = pyganim.PygAnimation(boltAnim)
        self.boltJumpLeft.play()

        boltAnim = []
        for anim in ATTACK_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackRight = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in ATTACK_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackLeft = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in CROUCH_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_CROUCH))
        self.boltCrouchRight = pyganim.PygAnimation(boltAnim, loop=False)
        self.boltCrouchRight.play()

        boltAnim = []
        for anim in CROUCH_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_CROUCH))
        self.boltCrouchLeft = pyganim.PygAnimation(boltAnim, loop=False)
        self.boltCrouchLeft.play()

    def update(self, x, y, left, right, up, key_attack, ability, platforms):
        self.hero_attack = key_attack
        if self.flag_attack_left and not key_attack:
            self.rect = Rect(int(x + 30), int(y), int(self.WIDTH), int(self.HEIGHT))  # прямоугольный объект
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
                self.yvel = -self.JUMP_POWER
            self.image.fill(Color(COLOR))
            if self.POSITION_RIGHT:
                self.boltJumpRight.blit(self.image, (0, 0))
            else:
                self.boltJumpLeft.blit(self.image, (0, 0))

        if left:
            self.xvel = -self.MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = False
            if up:
                self.boltJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltRunLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = self.MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            self.POSITION_RIGHT = True
            if up:
                self.boltJumpRight.blit(self.image, (0, 0))
            else:
                self.boltRunRight.blit(self.image, (0, 0))

        if key_attack:
            self.image.fill(Color(COLOR))
            if self.POSITION_RIGHT:
                self.boltAttackRight.blit(self.image, (0, 0))
                self.boltAttackRight.play()
            else:
                if not self.flag_attack_left:
                    self.xvel -= 30
                    self.flag_attack_left = True
                    self.return_update = 30
                self.boltAttackLeft.blit(self.image, (0, 0))
                self.boltAttackLeft.play()

        if ability and self.flag_ability:
            if self.POSITION_RIGHT:
                self.xvel += 50
                self.flag_ability = False
            else:
                self.xvel -= 50
                self.flag_ability = False
        else:
            self.flag_ability = True

        if not self.onGround:
            self.yvel += self.GRAVITY

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
        if self.flag_attack_left and self.hero_attack:
            x_sr += 30
        return int(x_sr), int(s_arr[0]), int(s_arr[1])

    def give_damage(self, value):
        print(self.health_points)
        if value != 0:
            self.image.fill(Color(COLOR))
            self.health_points -= value
            if self.POSITION_RIGHT:
                self.boltCrouchRight.blit(self.image, (0, 10))
                self.boltCrouchRight.play()
                self.on_attack = True
            else:
                self.boltCrouchLeft.blit(self.image, (0, 10))
                self.boltCrouchLeft.play()
                self.on_attack = True
