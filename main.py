import os
import sys
import json

import pygame
from pygame import *
import lvls.lvl_1 as lvl1
import option_menu as options

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


if __name__ == "__main__":
    # __________________________________-DOWNLOAD OPTIONS-________________________________

    json_file_object = open("options.json", "r")
    json_dict = json.load(json_file_object)
    FPS = json_dict['FPS']

    # __________________________________-DOWNLOAD OPTIONS-________________________________

    pygame.init()  # Инициация PyGame, обязательная строчка
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
                        lvl1.DrawLvl()
                    if now_menu == 2:
                        options.launch_menu()
                    if now_menu == 3:
                        running = False
                if event.key == K_DOWN:
                    now_menu += 1
                if event.key == K_UP:
                    now_menu -= 1

            if now_menu >= 4:
                now_menu = 3
            if now_menu <= 0:
                now_menu = 1

        screen.blit(pygame.transform.scale(load_image("bg_night_town.png"), (1280, 720)), (0, 0))

        main_label = main_font.render('Dungeon Adventure', False, (153, 24, 24))
        screen.blit(main_label, (310, 50))

        if now_menu == 1:
            Start_label = base_font.render('Start', False, (153, 24, 24))
            screen.blit(Start_label, (580, 200))

            Start_label = base_font.render('Options', False, (255, 255, 255))
            screen.blit(Start_label, (565, 260))

            Start_label = base_font.render('Exit', False, (255, 255, 255))
            screen.blit(Start_label, (590, 320))

        elif now_menu == 2:
            Start_label = base_font.render('Start', False, (255, 255, 255))
            screen.blit(Start_label, (580, 200))

            Start_label = base_font.render('Options', False, (153, 24, 24))
            screen.blit(Start_label, (565, 260))

            Start_label = base_font.render('Exit', False, (255, 255, 255))
            screen.blit(Start_label, (590, 320))

        elif now_menu == 3:
            Start_label = base_font.render('Start', False, (255, 255, 255))
            screen.blit(Start_label, (580, 200))

            Start_label = base_font.render('Options', False, (255, 255, 255))
            screen.blit(Start_label, (565, 260))

            Start_label = base_font.render('Exit', False, (153, 24, 24))
            screen.blit(Start_label, (590, 320))

        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
        # print(clock.get_fps())
