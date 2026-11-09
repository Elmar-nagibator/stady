import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя машинка")

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect(center=(400, 500))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 25))
        self.image.fill((220, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 700)
        self.rect.y = random.randint(-500, -50)

    def update(self):
        self.rect.y += 3

        if self.rect.y > 600:
            self.rect.y = -30
            self.rect.x = random.randint(0, 700)


player = Player()
enemies = pygame.sprite.Group()

for i in range(4):
    enemies.add(Enemy())

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    player.update()
    enemies.update()

    screen.fill((60, 60, 60))
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)
