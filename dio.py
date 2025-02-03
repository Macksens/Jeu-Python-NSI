import pygame
import random
import numpy as np

pygame.init()

# Dimension de l'ecran et couleur
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

game_speed = 10

# Classe Dino
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 100
        self.is_jumping = False
        self.jump_speed = 15
        self.gravity = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True

        if self.is_jumping:
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed < -15:
                self.is_jumping = False
                self.jump_speed = 15

# Classe Obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 90

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -20:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = SCREEN_HEIGHT - 90

# Creation des sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

dino = Dino()
all_sprites.add(dino)

# Creation des obstacles
for _ in range(3):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

running = True
clock = pygame.time.Clock()

# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.spritecollideany(dino, obstacles):
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
