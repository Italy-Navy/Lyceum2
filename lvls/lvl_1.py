import json


from mobs.Doctor import *
from environment.blocks import *
from hero.hero import *
from mobs.Low_level_mob import *
from mobs.Plant import *
from mobs.NPC_Worm import *
from mobs.Wizard import *
from mobs.Fireball import *
from hero.hero_hp import *

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


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target, delta):
        self.state = self.camera_func(self.state, attack_camera_left(target.rect, delta))


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы
    return Rect(l, t, w, h)


def attack_camera_left(rectangle, delta):
    s = str(rectangle)
    e = s[6:-2].split(',')
    return Rect(int(e[0]) + delta, int(e[1]), int(e[2]) + delta, int(e[3]))


def DrawLvl():
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

    hero = Player(100, 500)  # создаем героя по (x,y) координатам
    doctor_mob1 = Doctor(350, 500)
    doctor_mob2 = Doctor(550, 500)
    low_level_mob = LowLevelMob(750, 500)
    plant_mob = Plant(250, 400)
    npc_worm = Worm(100, 400)
    wizard_mob = Wizard(110, 400)
    hero_hp = health_bar(50, 30)

    left = right = False  # по умолчанию - стоим
    attack = up = ability = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    clock = pygame.time.Clock()
    x = y = 0
    level = load_level("lvl1.txt")
    for row in level:  # вся строка
        for char in row:  # каждый символ
            if char == "#":
                # создаем блок, заливаем его цветом и рисеум его
                platform = Platform(x, y)
                entities.add(platform)
                platforms.append(platform)
            else:
                empty = Empty(x, y)
                entities.add(empty)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    entities.add(hero)
    entities.add(doctor_mob1)
    entities.add(doctor_mob2)
    entities.add(low_level_mob)
    entities.add(plant_mob)
    entities.add(npc_worm)
    entities.add(wizard_mob)
    entities.add(hero_hp)

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)

    running = True
    use_fireball = True
    while running:  # Основной цикл программы
        clock.tick(FPS)
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                running = False
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

        screen.blit(background, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        x_hero, x_origin, y_hero = hero.get_x_y()
        camera_delta = hero.update(x_origin, y_hero, left, right, up, attack, ability, platforms)  # передвижение
        camera.update(hero, camera_delta)  # центризируем камеру относительно персонажа

        doctor_mob1.doctor_behavior(x_hero, y_hero, platforms)
        doctor_mob2.doctor_behavior(x_hero, y_hero, platforms)

        # _____________________________________-DAMAGE CALCULATING-_______________________________

        hero.give_damage(doctor_mob1.get_tick_damage())
        hero.give_damage(doctor_mob2.get_tick_damage())
        now_hero_hp, max_hero_hp = hero.get_hp()
        hero_hp.update(int(now_hero_hp), int(max_hero_hp), camera.state.x)

        # _____________________________________-DAMAGE CALCULATING-_______________________________

        low_level_mob.low_level_mob_behavior(x_hero, y_hero, platforms)
        plant_mob.plant_behavior(x_hero, y_hero, platforms)
        npc_worm.worm_behavior(x_hero, y_hero, platforms)

        use_fireball = wizard_mob.wizard_behavior(x_hero, y_hero, platforms)

        if use_fireball:
            spawn_x, spawn_y, position_right = wizard_mob.information_for_fireball()
            fireball = Fireball(spawn_x, spawn_y)
            entities.add(fireball)
            fireball.fireball_behavior(spawn_x, spawn_y, platforms, position_right)
            entities.add(fireball)

        for element in entities:
            screen.blit(element.image, camera.apply(element))
        screen.blit(hero_hp.image, camera.apply(hero_hp))

        if hero.flag_to_stop():
            running = False

        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
        # print(clock.get_fps())
