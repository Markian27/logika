import sys
import pygame
from pygame import *
from random import *

pygame.init()

"""створення вікна програми"""
window_width = 700
window_height = 700
window = pygame.display.set_mode((window_width, window_height))  # Вікно програми
background = image.load('background.png')
background = transform.scale(background, (window_width, window_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Maze")
# icon = pygame.image.load(None)
# pygame.display.set_icon(icon)

"""Звуки"""
musics = ['gameMusic.mp3', "button_click.mp3"]
mixer.init()
mixer.music.set_volume(0.05)


# Не Змінні
BACK = (48, 55, 99)
FPS = 60
# Змінні
GameState = 'menu'

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, size):
        super().__init__()
        self.image = transform.scale(image.load(img), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

"""Спрайти"""
# Кнопки
mazeTxt = GameSprite('maze.png', 215, 115, (270, 115))
btnStart = GameSprite('start.png', 265, 270, (170, 73))
btnExit = GameSprite('exit.png', 265, 358, (170, 73))
btnLeftArrow = GameSprite('LeftArrow.png', 3, 5, (80, 40))
btnOne = GameSprite('one.png', 125, 125, (100, 100))
# Персонажі





while True:
    window.blit(background, (0, 0))
    if GameState == 'menu':
        mazeTxt.draw()
        btnStart.draw()
        btnExit.draw()
    if GameState == 'SelectLevel':
        btnOne.draw()
        btnLeftArrow.draw()
    if GameState == 'level1':
        btnLeftArrow.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            if GameState == 'menu':
                if btnStart.rect.collidepoint(event.pos):
                    GameState = 'SelectLevel'
                    mixer.music.load(musics[1])
                    mixer.music.play()
                if btnExit.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            if GameState == 'SelectLevel':
                if btnOne.rect.collidepoint(event.pos):
                    GameState = 'level1'
                    mixer.music.load(musics[1])
                    mixer.music.play()
            if btnLeftArrow.rect.collidepoint(event.pos):
                GameState = 'menu'
                mixer.music.load(musics[1])
                mixer.music.play()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)
