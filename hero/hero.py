import pygame
from pygame import *
from hero import playanim as pyganim
import os
from random import randint as rnd

COLOR = "#888888"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

RUN_RIGHT = [
    ('%s/../data/animations/Main_Hero/run_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_right/8.png' % ICON_DIR),
]

RUN_LEFT = [
    ('%s/../data/animations/Main_Hero/run_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/run_left/8.png' % ICON_DIR),
]

IDLE_RIGHT = [
    ('%s/../data/animations/Main_Hero/idle_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/12.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/13.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/14.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_right/15.png' % ICON_DIR),
]

IDLE_LEFT = [
    ('%s/../data/animations/Main_Hero/idle_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/12.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/13.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/14.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/idle_left/15.png' % ICON_DIR),
]

JUMP_RIGHT = [
    ('%s/../data/animations/Main_Hero/jump_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_right/7.png' % ICON_DIR),
]

JUMP_LEFT = [
    ('%s/../data/animations/Main_Hero/jump_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/jump_left/7.png' % ICON_DIR),
]

ATTACK_HEW_RIGHT = [
    ('%s/../data/animations/Main_Hero/attack_hew_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_right/10.png' % ICON_DIR),
]

ATTACK_HEW_LEFT = [
    ('%s/../data/animations/Main_Hero/attack_hew_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_hew_left/10.png' % ICON_DIR),
]

ATTACK_PRICK_RIGHT = [
    ('%s/../data/animations/Main_Hero/attack_prick_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_right/8.png' % ICON_DIR),
]

ATTACK_PRICK_LEFT = [
    ('%s/../data/animations/Main_Hero/attack_prick_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_prick_left/8.png' % ICON_DIR),
]

ATTACK_SLASH_RIGHT = [
    ('%s/../data/animations/Main_Hero/attack_slash_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_right/12.png' % ICON_DIR),
]

ATTACK_SLASH_LEFT = [
    ('%s/../data/animations/Main_Hero/attack_slash_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/attack_slash_left/12.png' % ICON_DIR),
]

DEATH_RIGHT = [
    ('%s/../data/animations/Main_Hero/death_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/12.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/13.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/14.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_right/15.png' % ICON_DIR),
]

DEATH_LEFT = [
    ('%s/../data/animations/Main_Hero/death_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/12.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/13.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/14.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/death_left/15.png' % ICON_DIR),
]

ROLL_RIGHT = [
    ('%s/../data/animations/Main_Hero/roll_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/12.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/13.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/14.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_right/15.png' % ICON_DIR),
]

ROLL_LEFT = [
    ('%s/../data/animations/Main_Hero/roll_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/7.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/8.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/9.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/10.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/11.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/12.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/13.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/14.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/roll_left/15.png' % ICON_DIR),
]

SHIELD_RIGHT = [
    ('%s/../data/animations/Main_Hero/shield_right/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_right/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_right/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_right/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_right/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_right/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_right/7.png' % ICON_DIR),
]

SHIELD_LEFT = [
    ('%s/../data/animations/Main_Hero/shield_left/1.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_left/2.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_left/3.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_left/4.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_left/5.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_left/6.png' % ICON_DIR),
    ('%s/../data/animations/Main_Hero/shield_left/7.png' % ICON_DIR),
]


class Player(sprite.Sprite):
    def __init__(self, x, y, hero_hp=250):
        # ____________________________-HERO FEATURES-______________________________

        self.MOVE_SPEED = 4
        self.JUMP_POWER = 8
        self.GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
        self.now_health_points = hero_hp
        self.max_health_points = 250

        # ____________________________-HERO FEATURES-______________________________

        self.WIDTH = 28
        self.HEIGHT = 48

        self.ANIMATION_DELAY = 0.1  # скорость смены кадров
        self.ANIMATION_DELAY_ATTACK = 0.09  # скорость смены кадров
        self.ANIMATION_DELAY_JUMP = 0.15  # скорость смены кадров прыжков
        self.ANIMATION_DELAY_CROUCH = 0.1
        self.ANIMATION_DELAY_DIE = 0.35

        # _________________________________-FLAG-_________________________________

        self.POSITION_RIGHT = True
        self.onGround = False  # На земле ли я?

        self.flag_attack = False
        self.attack_damage = 100
        self.atack_now = 0.00
        self.is_damage = True

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

        self.image1 = Surface((self.WIDTH + 50, self.HEIGHT))
        self.image1.fill(Color(COLOR))
        self.image = Surface((self.WIDTH + 50, self.HEIGHT))
        self.image.fill(Color(COLOR))
        self.return_update = 0
        self.rect = Rect(x, y - 10, self.WIDTH, self.HEIGHT)  # прямоугольный объект
        self.image1.set_colorkey(Color(COLOR))  # делаем фон прозрачным
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
        for anim in ATTACK_HEW_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackHewRight = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in ATTACK_HEW_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackHewLeft = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in ATTACK_PRICK_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackPrickRight = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in ATTACK_PRICK_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackPrickLeft = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in ATTACK_SLASH_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttaclSlashRight = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in ATTACK_SLASH_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_ATTACK))
        self.boltAttackSlashLeft = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in DEATH_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY_DIE))
        self.boltDieRight = pyganim.PygAnimation(boltAnim, loop=False)

        boltAnim = []
        for anim in DEATH_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY_DIE))
        self.boltDieLeft = pyganim.PygAnimation(boltAnim, loop=False)

    def update(self, x, y, left, right, up, key_attack, ability, platforms):
        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image1.fill(Color(COLOR))
                if self.POSITION_RIGHT:
                    self.boltIdleRight.blit(self.image1, (0, -10))
                else:
                    self.boltIdleLeft.blit(self.image1, (15, -10))

        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -self.JUMP_POWER
            self.image1.fill(Color(COLOR))
            if self.POSITION_RIGHT:
                self.boltJumpRight.blit(self.image1, (-18, 0))
            else:
                self.boltJumpLeft.blit(self.image1, (-35, 0))

        if left:
            self.xvel = -self.MOVE_SPEED  # Лево = x- n
            self.image1.fill(Color(COLOR))
            self.POSITION_RIGHT = False
            if up:
                self.boltJumpLeft.blit(self.image1, (-35, 0))
            else:
                self.boltRunLeft.blit(self.image1, (10, -10))

        if right:
            self.xvel = self.MOVE_SPEED  # Право = x + n
            self.image1.fill(Color(COLOR))
            self.POSITION_RIGHT = True
            if up:
                self.boltJumpRight.blit(self.image1, (-18, 0))
            else:
                self.boltRunRight.blit(self.image1, (-18, -10))

        if key_attack:
            self.flag_attack = True

        if ability and self.flag_ability:
            if self.POSITION_RIGHT:
                self.xvel += 50
                self.flag_ability = False
            else:
                self.xvel -= 50
                self.flag_ability = False
        else:
            self.flag_ability = True

        if self.now_health_points <= 0:
            self._all_stop()
            if self.POSITION_RIGHT:
                self.boltDieRight.blit(self.image1, (0, -10))
                self.boltDieRight.play()
            else:
                self.boltDieLeft.blit(self.image1, (0, -10))
                self.boltDieLeft.play()

        if not self.onGround:
            self.yvel += self.GRAVITY

        if self.flag_attack:
            self.image1.fill(Color(COLOR))
            if self.POSITION_RIGHT:
                self.boltAttackPrickRight.blit(self.image1, (-33, -10))
                self.boltAttackPrickRight.play()
                if self.boltAttackPrickRight.elapsed >= self.boltAttackPrickRight._startTimes[-1] - 0.1:
                    self.flag_attack = False
                    self.is_damage = True
            else:
                self.boltAttackPrickLeft.blit(self.image1, (-30, -10))
                self.boltAttackPrickLeft.play()
                if self.boltAttackPrickLeft.elapsed >= self.boltAttackPrickLeft._startTimes[-1] - 0.1:
                    self.flag_attack = False
                    self.is_damage = True

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.image.fill(Color(COLOR))
        self.image.blit(self.image1, (-20, 0))

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.yvel = 0

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.yvel = 0

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def _all_stop(self):
        self.boltJumpLeft.stop()
        self.boltRunLeft.stop()
        self.boltIdleLeft.stop()

        self.boltIdleRight.stop()
        self.boltJumpRight.stop()
        self.boltRunRight.stop()

    def get_x_y(self):
        s = str(self.rect)
        s_arr = s[6:-2].split(',')
        x_sr = (int(s_arr[0]) + int(s_arr[0])) / 2
        x_sr += 0
        return int(x_sr), int(s_arr[0]), int(s_arr[1])

    def give_damage(self, value):
        if value != 0:
            self.image1.fill(Color(COLOR))
            self.now_health_points -= value
            if self.POSITION_RIGHT:
                # self.boltCrouchRight.blit(self.image, (0, 10))
                # self.boltCrouchRight.play()
                self.on_attack = True
            else:
                # self.boltCrouchLeft.blit(self.image, (0, 10))
                # self.boltCrouchLeft.play()
                self.on_attack = True

    def make_damage(self):
        if self.flag_attack and self.is_damage:
            self.is_damage = False
            print(1)
            if self.POSITION_RIGHT:
                return rnd(self.attack_damage - 3, self.attack_damage + 3), 50
            return rnd(self.attack_damage - 3, self.attack_damage + 3), -50
        return None, None

    def get_hp(self):
        return self.now_health_points, self.max_health_points

    def flag_to_stop(self):
        if self.now_health_points <= 0:
            return True
        return False
