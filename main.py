import pygame
from pygame import *
import lvls.lvl_1 as lvl1

WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#999999"
FPS = 60

if __name__ == "__main__":
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Dungeon adventure")  # Пишем в шапку
    background = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    background.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

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
                    lvl1.DrawLvl()

        textsurface = myfont.render('Push Enter To Start Level 1', False, (0, 0, 0))

        screen.blit(textsurface, (450, 300))
        pygame.display.update()  # обновление и вывод всех изменений на экран
        pygame.display.flip()
        # print(clock.get_fps())
