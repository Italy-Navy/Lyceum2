import os
import sys
import json
from random import randint
import lvl_menu

import pygame
from pygame import *

import option_menu as options
import lvls.lvl_1 as lvl1
import lvls.lvl_2 as lvl2

WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"


def load_image(name, colorkey=None):
    fullname = os.path.join(("%s/../data/assets/background_images/" % __file__), name)
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


def menu_music():
    # __________________________________-DOWNLOAD OPTIONS-________________________________
    json_file_object_music = open("options.json", "r")
    json_dict_music = json.load(json_file_object_music)
    json_file_object_music.close()
    # __________________________________-DOWNLOAD OPTIONS-________________________________
    if randint(1, 2) == 1:
        pygame.mixer.music.load('data/music/menu_1.mp3')
    else:
        pygame.mixer.music.load('data/music/menu_2.mp3')

    pygame.mixer.music.set_volume(json_dict_music["music_value"])
    pygame.mixer.music.play(-1)


def prepare_save_file(js_dict):
    return js_dict["Save"]["x_hero"], js_dict["Save"]["y_hero"], js_dict["Save"]["hp_hero"]


if __name__ == "__main__":
    # __________________________________-DOWNLOAD OPTIONS-________________________________

    json_file_object = open("options.json", "r")
    json_dict = json.load(json_file_object)
    FPS = json_dict['FPS']
    json_file_object.close()
    if json_dict["Save"] is None:
        is_save = False
    else:
        is_save = True

    # __________________________________-DOWNLOAD OPTIONS-________________________________

    pygame.init()  # Инициация PyGame, обязательная строчка

    menu_music()

    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Dungeon adventure")  # Пишем в шапку
    background = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    background.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    pygame.font.init()  # you have to call this at the start,

    now_menu = 1

    # if you want to use this module.
    base_font = pygame.font.SysFont('Comic Sans MS', 30)
    main_font = pygame.font.SysFont('Comic Sans MS', 72)

    clock = pygame.time.Clock()
    running = True
    while running:  # Основной цикл программы
        clock.tick(FPS)
        screen.blit(background, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if now_menu == 1:
                        if json_dict["last_lvl"] == 1:
                            lvl1.DrawLvl(*prepare_save_file(json_dict))
                        if json_dict["last_lvl"] == 2:
                            lvl2.DrawLvl(*prepare_save_file(json_dict))
                    if now_menu == 2:
                        lvl_menu.lvl_menu()
                        menu_music()
                        json_file_object = open("options.json", "r")
                        json_dict = json.load(json_file_object)
                        FPS = json_dict['FPS']
                        json_file_object.close()
                        if json_dict["Save"] is None:
                            is_save = False
                        else:
                            is_save = True
                    if now_menu == 3:
                        options.launch_menu()
                        menu_music()
                    if now_menu == 4:
                        running = False
                if event.key == K_DOWN:
                    now_menu += 1
                if event.key == K_UP:
                    now_menu -= 1

            if now_menu > 4:
                now_menu = 4
            if now_menu < 1:
                now_menu = 1
            if not is_save and now_menu == 1:
                now_menu = 2

        screen.blit(pygame.transform.scale(load_image("bg_night_town.png"), (1280, 720)), (0, 0))

        main_label = main_font.render('Dungeon Adventure', False, (153, 24, 24))
        screen.blit(main_label, (310, 50))

        if now_menu == 1:
            if is_save:
                Start_label = base_font.render('Continue', False, (153, 24, 24))
                screen.blit(Start_label, (555, 190))
            else:
                Start_label = base_font.render('Continue', False, (100, 100, 100))
                screen.blit(Start_label, (555, 190))

            Start_label = base_font.render('New Game', False, (255, 255, 255))
            screen.blit(Start_label, (550, 250))

            Start_label = base_font.render('Options', False, (255, 255, 255))
            screen.blit(Start_label, (565, 310))

            Start_label = base_font.render('Exit', False, (255, 255, 255))
            screen.blit(Start_label, (585, 370))

        elif now_menu == 2:
            if is_save:
                Start_label = base_font.render('Continue', False, (255, 255, 255))
                screen.blit(Start_label, (555, 190))
            else:
                Start_label = base_font.render('Continue', False, (100, 100, 100))
                screen.blit(Start_label, (555, 190))

            Start_label = base_font.render('New Game', False, (153, 24, 24))
            screen.blit(Start_label, (550, 250))

            Start_label = base_font.render('Options', False, (255, 255, 255))
            screen.blit(Start_label, (565, 310))

            Start_label = base_font.render('Exit', False, (255, 255, 255))
            screen.blit(Start_label, (585, 370))

        elif now_menu == 3:
            if is_save:
                Start_label = base_font.render('Continue', False, (255, 255, 255))
                screen.blit(Start_label, (555, 190))
            else:
                Start_label = base_font.render('Continue', False, (100, 100, 100))
                screen.blit(Start_label, (555, 190))

            Start_label = base_font.render('New Game', False, (255, 255, 255))
            screen.blit(Start_label, (550, 250))

            Start_label = base_font.render('Options', False, (153, 24, 24))
            screen.blit(Start_label, (565, 310))

            Start_label = base_font.render('Exit', False, (255, 255, 255))
            screen.blit(Start_label, (585, 370))

        elif now_menu == 4:
            if is_save:
                Start_label = base_font.render('Continue', False, (255, 255, 255))
                screen.blit(Start_label, (555, 190))
            else:
                Start_label = base_font.render('Continue', False, (100, 100, 100))
                screen.blit(Start_label, (555, 190))

            Start_label = base_font.render('New Game', False, (255, 255, 255))
            screen.blit(Start_label, (550, 250))

            Start_label = base_font.render('Options', False, (255, 255, 255))
            screen.blit(Start_label, (565, 310))

            Start_label = base_font.render('Exit', False, (153, 24, 24))
            screen.blit(Start_label, (585, 370))

        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
        # print(clock.get_fps())
