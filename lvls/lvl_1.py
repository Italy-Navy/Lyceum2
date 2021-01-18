import json

from mobs.Doctor import *
from lvls.blocks import *
from hero.hero import *
from mobs.Low_level_mob import *
from mobs.Plant import *
from mobs.NPC_Worm import *
from hero.hero_hp import *
from fps_measurement import *
import option_menu as options
from mobs.Sprout import *

# Объявляем переменные
WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"
PLATFORM_WIDTH = 20
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = "#FFFFFF"


def load_level(filename):
    filename = "data/maps/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_bg(name, colorkey=None):
    fullname = os.path.join(("%s/../../data/assets/" % __file__), name)
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


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move([self.state.topleft[0], self.state.topleft[1]])

    def apply_new(self, target):
        return target.move([self.state.topleft[0], self.state.topleft[1]])

    def update(self, target):
        self.state = self.camera_func(self.state, Rect(target.rect.x, target.rect.y, target.rect.w, target.rect.h))


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы
    return Rect(l, t, w, h)


def battle_music():
    # __________________________________-DOWNLOAD OPTIONS-________________________________
    json_file_object_music = open("options.json", "r")
    json_dict_music = json.load(json_file_object_music)
    json_file_object_music.close()
    # __________________________________-DOWNLOAD OPTIONS-________________________________
    value = json_dict_music["music_value"] - int(json_dict_music["music_value"] / 2)
    if randint(1, 1) == 1:
        pygame.mixer.music.load('%s/../../data/music/battle.mp3' % __file__)
    pygame.mixer.music.set_volume(value)
    pygame.mixer.music.play(-1)


def save_game(x_hero, y_hero, hero_hp, json_dict):
    save_dict = dict()
    save_dict["x_hero"] = x_hero
    save_dict["y_hero"] = y_hero
    save_dict["hp_hero"] = hero_hp
    json_dict["Save"] = save_dict
    with open('options.json', 'w') as outfile:
        json.dump(json_dict, outfile)


def DrawLvl(x_hero_input=150, y_hero_input=500, now_hero_hp=250):
    # __________________________________-DOWNLOAD OPTIONS-________________________________

    json_file_object = open("options.json", "r")
    json_dict = json.load(json_file_object)
    FPS = json_dict['FPS']

    # __________________________________-DOWNLOAD OPTIONS-________________________________

    pygame.init()  # Инициация PyGame, обязательная строчка

    battle_music()
    save_flag = False
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Dungeon adventure")  # Пишем в шапку
    background = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    background.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    hero = Player(x_hero_input, y_hero_input, now_hero_hp)  # создаем героя по (x,y) координатам
    doctor_mob1 = Doctor(1880, 670)
    doctor_mob2 = Doctor(3350, 430)

    low_level_mob1 = LowLevelMob(900, 670)
    low_level_mob2 = LowLevelMob(1800, 530)
    low_level_mob3 = LowLevelMob(1500, 670)
    low_level_mob4 = LowLevelMob(2820, 530)
    low_level_mob5 = LowLevelMob(3180, 652)
    low_level_mob6 = LowLevelMob(3500, 652)
    low_level_mob7 = LowLevelMob(4700, 530)

    plant_mob1 = Plant(1420, 500)
    plant_mob2 = Plant(1960, 450)
    plant_mob3 = Plant(3650, 530)
    plant_mob4 = Plant(4410, 570)

    npc_worm = Worm(5350, 670)

    hero_hp = health_bar(50, 70)
    fps_label = fps_measure(1200, 70)

    sprout_mob1 = Sprout(2020, 540)
    sprout_mob2 = Sprout(2990, 430)
    sprout_mob3 = Sprout(2660, 650)

    left = right = False  # по умолчанию - стоим
    attack = up = ability = False
    global_pause = use_pause = green_label = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    clock = pygame.time.Clock()
    x = y = 0
    level = load_level("lvl1.txt")
    for row in level:  # вся строка
        for char in row:  # каждый символ
            if char == "p":
                platform = PlatformLvl1(x - 15, y)
                entities.add(platform)
                platforms.append(platform)
            if char == "e":
                earth = EarthLvl1(x - 15, y)
                entities.add(earth)
                platforms.append(earth)
            if char == "~":
                extra_earth = ExtraEarthLvl1(x - 15, y)
                entities.add(extra_earth)
                platforms.append(extra_earth)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    mob_entities = pygame.sprite.Group()  # Все объекты
    plant_entities = pygame.sprite.Group()
    sprout_entities = pygame.sprite.Group()

    # entities.add(doctor_mob1)
    # entities.add(doctor_mob2)
    mob_entities.add(low_level_mob1)
    mob_entities.add(low_level_mob2)
    mob_entities.add(low_level_mob3)
    mob_entities.add(low_level_mob4)
    mob_entities.add(low_level_mob5)
    mob_entities.add(low_level_mob6)
    mob_entities.add(low_level_mob7)

    plant_entities.add(plant_mob1)
    plant_entities.add(plant_mob2)
    plant_entities.add(plant_mob3)
    plant_entities.add(plant_mob4)
    entities.add(npc_worm)
    entities.add(hero_hp)
    # entities.add(fps_label)
    sprout_entities.add(sprout_mob1)
    sprout_entities.add(sprout_mob2)
    sprout_entities.add(sprout_mob3)

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    bg_castle = pygame.transform.scale(load_bg("background_images/bg_tree_2.png"), (1280, 720))

    camera = Camera(camera_configure, total_level_width, total_level_height)

    transparent_pause = pygame.Surface((1280, 720))
    transparent_pause.set_alpha(150)
    transparent_pause.fill((50, 50, 50))

    transparent_pause_all = pygame.Surface((1280, 720))
    transparent_pause_all.set_alpha(255)
    transparent_pause_all.fill((50, 50, 50))

    transparent_surface = pygame.Surface((1280, 720))
    transparent_surface.set_alpha(50)
    transparent_surface.fill((50, 50, 50))

    pause_menu = 1

    main_font = pygame.font.SysFont('Comic Sans MS', 130)
    label_font = pygame.font.SysFont('Comic Sans MS', 50)

    pause_label = main_font.render('Pause', False, (255, 255, 255))

    running = True
    while running:  # Основной цикл программы
        clock.tick(FPS)
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                running = False
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    right = True
                if event.key == K_a:
                    left = True
                if event.key == K_w:
                    up = True
                if event.key == K_i:
                    attack = True
                if event.key == K_p:
                    ability = True
                if event.key == K_ESCAPE:
                    if not global_pause:
                        global_pause = True
                    else:
                        global_pause = False
                        use_pause = False
                if global_pause:
                    if event.key == K_DOWN:
                        pause_menu += 1
                        if green_label:
                            green_label = False
                    if event.key == K_UP:
                        pause_menu -= 1
                        if green_label:
                            green_label = False
                    if event.key == K_RETURN:
                        if pause_menu == 1:
                            global_pause = False
                            use_pause = False
                        if pause_menu == 2:
                            save_flag = True
                        if pause_menu == 3:
                            options.launch_menu()
                            screen.blit(transparent_pause_all, (0, 0))
                            screen.blit(pause_label, (475, 50))
                        if pause_menu == 4:
                            running = False

            elif event.type == KEYUP:
                if event.key == K_d:
                    right = False
                if event.key == K_a:
                    left = False
                if event.key == K_w:
                    up = False
                if event.key == K_i:
                    attack = False
                if event.key == K_p:
                    ability = False

            if pause_menu > 4:
                pause_menu = 4
            if pause_menu < 1:
                pause_menu = 1

        if global_pause:
            if not use_pause:
                screen.blit(transparent_pause, (0, 0))
                screen.blit(pause_label, (475, 50))
                use_pause = True
            if pause_menu == 1:
                continue_label = label_font.render('Continue', False, (170, 170, 170))
                save_label = label_font.render('Save the game', False, (255, 255, 255))
                options_label = label_font.render('Options', False, (255, 255, 255))
                exit_label = label_font.render('Back to menu', False, (255, 255, 255))
            if pause_menu == 2:
                if green_label:
                    save_label = label_font.render('Save the game', False, (80, 255, 80))
                else:
                    save_label = label_font.render('Save the game', False, (170, 170, 170))
                continue_label = label_font.render('Continue', False, (255, 255, 255))
                options_label = label_font.render('Options', False, (255, 255, 255))
                exit_label = label_font.render('Back to menu', False, (255, 255, 255))
            if pause_menu == 3:
                continue_label = label_font.render('Continue', False, (255, 255, 255))
                save_label = label_font.render('Save the game', False, (255, 255, 255))
                options_label = label_font.render('Options', False, (170, 170, 170))
                exit_label = label_font.render('Back to menu', False, (255, 255, 255))
            if pause_menu == 4:
                continue_label = label_font.render('Continue', False, (255, 255, 255))
                save_label = label_font.render('Save the game', False, (255, 255, 255))
                options_label = label_font.render('Options', False, (255, 255, 255))
                exit_label = label_font.render('Back to menu', False, (170, 170, 170))
            screen.blit(continue_label, (540, 300))
            screen.blit(save_label, (475, 370))
            screen.blit(options_label, (547, 440))
            screen.blit(exit_label, (493, 510))

        else:
            screen.blit(bg_castle, (0, 0))
            screen.blit(transparent_surface, (0, 0))
            x_hero, x_origin, y_hero = hero.get_x_y()
            # print(x_hero, y_hero)
            hero.update(x_origin, y_hero, left, right, up, attack, ability, platforms)  # передвижение
            camera.update(hero)  # центризируем камеру относительно персонажа

            doctor_mob1.doctor_behavior(x_hero, y_hero, platforms)
            doctor_mob2.doctor_behavior(x_hero, y_hero, platforms)

            # _____________________________________-DAMAGE CALCULATING-_______________________________

            hero_damage, damage_delta = hero.make_damage()

            if doctor_mob1.state():
                hero.give_damage(doctor_mob1.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                doctor_mob1.dam_hero(hero_damage, x_hero, damage_delta)

            if doctor_mob2.state():
                hero.give_damage(doctor_mob2.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                doctor_mob2.dam_hero(hero_damage, x_hero, damage_delta)

            if plant_mob1.state():
                hero.give_damage(plant_mob1.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                plant_mob1.dam_hero(hero_damage, x_hero, damage_delta)

            if plant_mob2.state():
                hero.give_damage(plant_mob2.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                plant_mob2.dam_hero(hero_damage, x_hero, damage_delta)

            if plant_mob3.state():
                hero.give_damage(plant_mob3.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                plant_mob3.dam_hero(hero_damage, x_hero, damage_delta)

            if plant_mob4.state():
                hero.give_damage(plant_mob4.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                plant_mob4.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob1.state():
                hero.give_damage(low_level_mob1.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob1.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob2.state():
                hero.give_damage(low_level_mob2.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob2.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob3.state():
                hero.give_damage(low_level_mob3.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob3.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob4.state():
                hero.give_damage(low_level_mob4.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob4.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob5.state():
                hero.give_damage(low_level_mob5.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob5.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob6.state():
                hero.give_damage(low_level_mob6.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob6.dam_hero(hero_damage, x_hero, damage_delta)

            if low_level_mob7.state():
                hero.give_damage(low_level_mob7.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                low_level_mob7.dam_hero(hero_damage, x_hero, damage_delta)

            if sprout_mob1.state():
                hero.give_damage(sprout_mob1.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                sprout_mob1.dam_hero(hero_damage, x_hero, damage_delta)

            if sprout_mob2.state():
                hero.give_damage(sprout_mob2.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                sprout_mob2.dam_hero(hero_damage, x_hero, damage_delta)

            if sprout_mob3.state():
                hero.give_damage(sprout_mob3.get_tick_damage())
                now_hero_hp, max_hero_hp = hero.get_hp()
                hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

                sprout_mob3.dam_hero(hero_damage, x_hero, damage_delta)

            # _____________________________________-DAMAGE CALCULATING-_______________________________

            low_level_mob1.low_level_mob_behavior(x_hero, y_hero, platforms)
            low_level_mob2.low_level_mob_behavior(x_hero, y_hero, platforms)
            low_level_mob3.low_level_mob_behavior(x_hero, y_hero, platforms)
            low_level_mob4.low_level_mob_behavior(x_hero, y_hero, platforms)
            low_level_mob5.low_level_mob_behavior(x_hero, y_hero, platforms)
            low_level_mob6.low_level_mob_behavior(x_hero, y_hero, platforms)
            low_level_mob7.low_level_mob_behavior(x_hero, y_hero, platforms)

            plant_mob1.plant_behavior(x_hero, y_hero, platforms)
            plant_mob2.plant_behavior(x_hero, y_hero, platforms)
            plant_mob3.plant_behavior(x_hero, y_hero, platforms)
            plant_mob4.plant_behavior(x_hero, y_hero, platforms)

            npc_worm.worm_behavior(x_hero, y_hero, platforms)

            sprout_mob1.sprout_behavior(x_hero, y_hero, platforms)
            sprout_mob2.sprout_behavior(x_hero, y_hero, platforms)
            sprout_mob3.sprout_behavior(x_hero, y_hero, platforms)

            fps_label.update_fps(int(clock.get_fps()), camera.state.x)

            for element in entities:
                screen.blit(element.image, camera.apply(element))
            screen.blit(hero_hp.image, camera.apply(hero_hp))

            screen.blit(fps_label.image, camera.apply(fps_label))

            screen.blit(doctor_mob1.image, camera.apply_new(
                Rect(doctor_mob1.rect.x, doctor_mob1.rect.y + 15, doctor_mob1.rect.w, doctor_mob1.rect.h)))
            screen.blit(doctor_mob2.image, camera.apply_new(
                Rect(doctor_mob2.rect.x, doctor_mob2.rect.y + 15, doctor_mob2.rect.w, doctor_mob2.rect.h)))

            for element in mob_entities:
                screen.blit(element.image,
                            camera.apply_new(Rect(element.rect.x, element.rect.y + 25, element.rect.w, element.rect.h)))

            for element in plant_entities:
                screen.blit(element.image,
                            camera.apply_new(Rect(element.rect.x, element.rect.y + 8, element.rect.w, element.rect.h)))

            for element in sprout_entities:
                screen.blit(element.image,
                            camera.apply_new(Rect(element.rect.x, element.rect.y + 20, element.rect.w, element.rect.h)))

            screen.blit(pygame.transform.scale(hero.image, (120, 64)), camera.apply(hero))
            # screen.blit(pygame.transform.scale2x(hero.image), camera.apply(hero))
            # screen.blit(hero.image, camera.apply(hero))

        if hero.flag_to_stop():
            running = False
            pygame.mixer.music.stop()

        if save_flag:
            save_game(x_origin, y_hero, now_hero_hp, json_dict)
            green_label = True
            save_flag = False

        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
