# Pygame шаблон - скелет для нового проекта Pygame

import pygame
import random
from Constants import *
from Player import *

# # Цвета (R, G, B)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
#
# WIDTH = 360  # ширина игрового окна
# HEIGHT = 480  # высота игрового окна
# FPS = 30  # частота кадров в секунду


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50, 50))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:

    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление\Update
    clock.tick(FPS)
    all_sprites.update()

    # Визуализация\Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
