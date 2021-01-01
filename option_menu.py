import json
import os
import sys

import pygame
from pygame import *

WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"


def load_image(name, colorkey=None):
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


def launch_menu():
    # __________________________________-DOWNLOAD OPTIONS-________________________________

    json_file_object = open("options.json", "r")
    json_dict = json.load(json_file_object)
    FPS = json_dict["FPS"]
    Music_Value = json_dict["music_value"]
    json_file_object.close()

    # __________________________________-DOWNLOAD OPTIONS-________________________________

    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Dungeon adventure")  # Пишем в шапку
    background = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    background.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    pygame.font.init()  # you have to call this at the start,

    FPS_add = Music_add = False
    FPS_sub = Music_sub = False
    save_flag = False

    now_menu = 1
    min_font = pygame.font.SysFont('Comic Sans MS', 20)
    base_font = pygame.font.SysFont('Comic Sans MS', 40)
    main_font = pygame.font.SysFont('Comic Sans MS', 130)

    transparent_rect = pygame.Surface((1280, 48))
    transparent_rect.set_alpha(80)
    transparent_rect.fill((252, 245, 224))

    clock = pygame.time.Clock()
    running = True
    while running:  # Основной цикл программы
        clock.tick(FPS)
        screen.blit(background, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if now_menu == 3:
                        # ______________________________________________-Save Changes-_________________________________
                        json_dict["FPS"] = FPS
                        json_dict["music_value"] = Music_Value
                        with open('options.json', 'w') as outfile:
                            json.dump(json_dict, outfile)
                        save_flag = True
                        # ______________________________________________-Save Changes-_________________________________
                    if now_menu == 4:
                        running = False
                if event.key == K_DOWN:
                    now_menu += 1
                    FPS_sub = False
                    FPS_add = False
                    Music_sub = False
                    Music_add = False
                    save_flag = False
                if event.key == K_UP:
                    now_menu -= 1
                    FPS_sub = False
                    FPS_add = False
                    Music_sub = False
                    Music_add = False
                    save_flag = False
                if event.key == K_RIGHT:
                    if now_menu == 1:
                        FPS_add = True
                    if now_menu == 2:
                        Music_add = True
                if event.key == K_LEFT:
                    if now_menu == 1:
                        FPS_sub = True
                    if now_menu == 2:
                        Music_sub = True

            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    if now_menu == 1:
                        FPS_add = False
                    if now_menu == 2:
                        Music_add = False
                if event.key == K_LEFT:
                    if now_menu == 1:
                        FPS_sub = False
                    if now_menu == 2:
                        Music_sub = False

            if now_menu > 4:
                now_menu = 4
            if now_menu < 1:
                now_menu = 1

        # __________________________________-FPS control-________________________________
        if FPS_add:
            FPS += 1
        if FPS_sub:
            FPS -= 1
        if FPS < 20:
            FPS = 20
        if FPS > 120:
            FPS = 120
        # __________________________________-FPS control-________________________________

        # __________________________________-FPS control-________________________________
        if Music_add:
            Music_Value += 1
        if Music_sub:
            Music_Value -= 1
        if Music_Value < 0:
            Music_Value = 0
        if Music_Value > 100:
            Music_Value = 100
        # __________________________________-FPS control-________________________________

        screen.blit(pygame.transform.scale(load_image("background_images/bg_tree.png"), (1280, 720)), (0, 0))

        if now_menu == 1:
            screen.blit(transparent_rect, (0, 322))
        if now_menu == 2:
            screen.blit(transparent_rect, (0, 386))
        if now_menu == 3:
            screen.blit(transparent_rect, (0, 490))
        if now_menu == 4:
            screen.blit(transparent_rect, (0, 558))

        main_label = main_font.render("Options", False, (100, 150, 150))
        screen.blit(main_label, (400, 50))

        # __________________________________________________-FPS-_________________________________________________

        fps_label_name = base_font.render("FPS", False, (80, 255, 70))
        screen.blit(fps_label_name, (420, 317))
        screen.blit(pygame.transform.scale(load_image("options_assets/bar.png"), (400, 30)), (520, 330))
        screen.blit(pygame.transform.scale(load_image("options_assets/empty.png"), (330, 20)), (555, 335))

        base_x_part_fps = 555  # 880
        num_parts_fps = int((FPS - 20) / 1.5)
        for _ in range(num_parts_fps):
            screen.blit(pygame.transform.scale(load_image("options_assets/bar_part.png"), (5, 20)), (base_x_part_fps,
                                                                                                     335))
            base_x_part_fps += 5

        fps_label = min_font.render(str(FPS), False, (80, 255, 70))
        screen.blit(fps_label, (555 + int((base_x_part_fps - 580) / 2), 330))

        # __________________________________________________-FPS-_________________________________________________

        # ______________________________________________-MUSIC-_____________________________________________

        music_label_name = base_font.render("Music", False, (0, 0, 255))
        screen.blit(music_label_name, (390, 377))
        screen.blit(pygame.transform.scale(load_image("options_assets/bar.png"), (400, 30)), (520, 395))
        screen.blit(pygame.transform.scale(load_image("options_assets/empty.png"), (330, 20)), (555, 400))

        base_x_part_music = 555  # 880
        num_parts_music = int((Music_Value) / 1.5)
        for _ in range(num_parts_music):
            screen.blit(pygame.transform.scale(load_image("options_assets/bar_part_3.png"), (5, 20)),
                        (base_x_part_music,
                         400))
            base_x_part_music += 5

        music_label = min_font.render(str(Music_Value), False, (87, 171, 255))
        screen.blit(music_label, (555 + int((base_x_part_music - 580) / 2), 395))

        # ______________________________________________-MUSIC-_____________________________________________

        # ______________________________________________-Save Changes-_____________________________________________

        Save_label_name = base_font.render("Save Changes", False, (255, 200, 82))
        screen.blit(Save_label_name, (520, 480))
        if save_flag:
            transparent_save = pygame.Surface((200, 30))
            transparent_save.set_alpha(80)
            transparent_save.fill((80, 255, 70))
            Save_label_name = min_font.render("Changes recorded", False, (255, 255, 255))
            screen.blit(Save_label_name, (540, 540))
            screen.blit(transparent_save, (527, 540))

        # ______________________________________________-Save Changes-_____________________________________________

        # _________________________________________________-BACK-____________________________________________

        Save_label_name = base_font.render("<<< Back", False, (255, 50, 50))
        screen.blit(Save_label_name, (300, 550))

        # _________________________________________________-BACK-____________________________________________

        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
        # print(clock.get_fps())
