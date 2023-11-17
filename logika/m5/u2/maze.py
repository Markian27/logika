import sys
import pygame
from pygame import *
from random import *

pygame.init()

"""створення вікна програми"""
window_width = 700
window_height = 500
window = pygame.display.set_mode((window_width, window_height))  # Вікно програми
background = image.load('background.jpg')
background = transform.scale(background, (window_width, window_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Maze")
# icon = pygame.image.load(None)
# pygame.display.set_icon(icon)

"""Звуки"""
music = ['jungles.ogg']
mixer.init()
mixer.music.load(music[0])
mixer.music.set_volume(0.1)

BACK = (48, 55, 99)
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, size):
        super().__init__()
        self.image = transform.scale(image.load(img), size)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

monster = GameSprite("cyborg.png", 1, 300, 300, (50, 50))
player = GameSprite("hero.png", 1, 300, 300, (50, 50))
GameState = 'menu'

while True:
    window.blit(background, (0, 0))
    monster.draw()
    player.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)
