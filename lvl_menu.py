import json
import os
import sys
import lvls.lvl_1 as lvl1
import lvls.lvl_2 as lvl2

import pygame
from pygame import *

WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"


def load_bg(name, colorkey=None):
    fullname = os.path.join(("%s/../data/assets/" % __file__), name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    LI_image = pygame.image.load(fullname)
    if colorkey is not None:
        LI_image = LI_image.convert()
        if colorkey == -1:
            colorkey = LI_image.get_at((0, 0))
        LI_image.set_colorkey(colorkey)
    else:
        LI_image = LI_image.convert_alpha()
    return LI_image


def lvl_menu():
    # __________________________________-DOWNLOAD OPTIONS-________________________________
    json_file_object = open("options.json", "r")
    json_dict = json.load(json_file_object)
    FPS = json_dict["FPS"]
    Music_Value = json_dict["music_value"]
    if json_dict["Location_1"] == "open":
        L1 = True
    else:
        L1 = False
    if json_dict["Location_2"] == "open":
        L2 = True
    else:
        L2 = False
    if json_dict["Location_3"] == "open":
        L3 = True
    else:
        L3 = False

    json_file_object.close()
    # __________________________________-DOWNLOAD OPTIONS-________________________________

    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Dungeon adventure")  # Пишем в шапку
    background = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    background.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    pygame.font.init()  # you have to call this at the start,

    now_menu = 1
    arrow_font = pygame.font.SysFont('Comic Sans MS', 150)
    head_font = pygame.font.SysFont('Comic Sans MS', 80)
    label_font = pygame.font.SysFont('Comic Sans MS', 50)
    min_font = pygame.font.SysFont('Comic Sans MS', 35)

    Right_arrow = arrow_font.render('>', False, (255, 255, 255))
    Left_arrow = arrow_font.render('<', False, (255, 255, 255))
    Select_label = head_font.render('Select Location', False, (255, 255, 255))
    Voodoo_forest_label = label_font.render('Voodoo Forest', False, (170, 255, 75))
    Witch_City_label = label_font.render('City of witches', False, (153, 24, 24))
    Castle_label = label_font.render('Dark Castle', False, (155, 155, 50))

    flag_draw_lock = False

    clock = pygame.time.Clock()
    running = True
    while running:  # Основной цикл программы
        clock.tick(FPS)
        screen.blit(background, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                running = False
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    now_menu += 1
                    flag_draw_lock = False
                if event.key == K_LEFT:
                    now_menu -= 1
                    flag_draw_lock = False
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_RETURN:
                    if now_menu == 1:
                        if L1:
                            lvl1.DrawLvl()
                        else:
                            flag_draw_lock = True
                    if now_menu == 2:
                        if L2:
                            lvl2.DrawLvl()
                        else:
                            flag_draw_lock = True
                    if now_menu == 3:
                        if L3:
                            pass
                        else:
                            flag_draw_lock = True

        if now_menu > 3:
            now_menu = 3
        if now_menu < 1:
            now_menu = 1

        if now_menu == 1:
            screen.blit(pygame.transform.scale(load_bg("background_images/bg_tree_2.png"), (1280, 720)), (0, 0))
            screen.blit(Right_arrow, (1200, 250))
            screen.blit(Voodoo_forest_label, (475, 600))
            if not L1:
                screen.blit(pygame.transform.scale(load_bg("lock.png"), (400, 300)), (440, 200))

        elif now_menu == 2:
            screen.blit(pygame.transform.scale(load_bg("background_images/bg_night_town.png"), (1280, 720)), (0, 0))
            screen.blit(Right_arrow, (1200, 250))
            screen.blit(Left_arrow, (50, 250))
            screen.blit(Witch_City_label, (475, 625))
            if not L2:
                screen.blit(pygame.transform.scale(load_bg("lock.png"), (400, 300)), (440, 200))

        elif now_menu == 3:
            screen.blit(pygame.transform.scale(load_bg("background_images/bg_castle.png"), (1280, 720)), (0, 0))
            screen.blit(Left_arrow, (50, 250))
            screen.blit(Castle_label, (500, 625))
            if not L3:
                screen.blit(pygame.transform.scale(load_bg("lock.png"), (400, 300)), (440, 200))

        if flag_draw_lock:
            transparent_lock = pygame.Surface((260, 53))
            transparent_lock.set_alpha(80)
            transparent_lock.fill((255, 80, 70))
            Save_label_name = min_font.render("Open Location", False, (255, 255, 255))
            screen.blit(Save_label_name, (520, 540))
            screen.blit(transparent_lock, (510, 540))

        screen.blit(Select_label, (360, 0))

        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
