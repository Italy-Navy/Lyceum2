# Импортируем библиотеку pygame
import pygame
from pygame import *

# Объявляем переменные
WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон

    while 1:  # Основной цикл программы
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                print(1)
                raise SystemExit("QUIT")
            if event.type == QUIT:
                raise SystemExit("QUIT")
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    print('2')
    main()
