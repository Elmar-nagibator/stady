
import pygame
import sys

pygame.init()

# 1. Создаем окно
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Управление машинкой")

clock = pygame.time.Clock()

# 2. Загружаем картинку
car = pygame.image.load("car1.png").convert_alpha()
car = pygame.transform.scale(car, (120, 70))

x = 340
y = 250
speed = 5

# Игровой цикл
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 3. Управление
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    # Не даем машинке выйти за окно
    x = max(0, min(x, WIDTH - 120))
    y = max(0, min(y, HEIGHT - 70))

    # Рисуем фон
    screen.fill((100, 180, 100))

    # Рисуем дорогу
    pygame.draw.rect(screen, (60, 60, 60), (0, 200, 800, 200))

    # Рисуем машинку
    screen.blit(car, (x, y))

    pygame.display.update()
    clock.tick(60)
