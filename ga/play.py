import pygame
import sys
import random

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.speed = 5

    def update(self, width, height):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 25))
        self.image.fill((220, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 700)
        self.rect.y = random.randint(-500, -50)
        self.speed = random.randint(2, 4)

    def update(self, width, height):
        self.rect.y += self.speed

        if self.rect.top > height:
            self.rect.y = -30
            self.rect.x = random.randint(0, 700)


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Моя машинка")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 50)
        self.game_over = False

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        for i in range(4):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not self.game_over:
                self.all_sprites.update(self.width, self.height)

                if pygame.sprite.spritecollide(self.player, self.enemies, False):
                    self.game_over = True

            self.screen.fill((60, 60, 60))
            self.all_sprites.draw(self.screen)

            if self.game_over:
                text = self.font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(text, (280, 250))

            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.run()
