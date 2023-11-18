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
movement = None
muves = [True]

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
# Стіни
l1w1x = GameSprite('Wall.png', 86, 87.5, (5, 527))
l1w2x = GameSprite('Wall.png', 613, 86, (5, 530))
l1w3y = GameSprite('Wall.png', 86, 86, (527, 5))
l1w4y = GameSprite('Wall.png', 86, 614.5, (527, 5))
walls = [l1w1x, l1w2x, l1w3y, l1w4y]
# Персонажі
p1 = GameSprite('Wall.png', 100, 100, (10, 30))

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
        p1.draw()
        for w in walls:
            w.draw()
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
        if GameState == 'level1':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    movement = "right"
                if event.key == pygame.K_a:
                    movement = "left"
                if event.key == pygame.K_s:
                    movement = "down"
                if event.key == pygame.K_w:
                    movement = "up"
    if GameState == 'level1':
        if movement == "right" and muves[-1] != 'right':
            for wall in walls:
                if p1.rect.colliderect(wall.rect):
                    muves.append('right')
                    p1.rect.x -= 2
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'left':
                muves.remove('left')
            p1.rect.x += 1
        if movement == "left" and muves[-1] != 'left':
            for wall in walls:
                if p1.rect.colliderect(wall.rect):
                    muves.append('left')
                    p1.rect.x += 2
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'right':
                muves.remove('right')
            p1.rect.x -= 1
        if movement == "down" and muves[-1] != 'down':
            for wall in walls:
                if p1.rect.colliderect(wall.rect):
                    muves.append('down')
                    p1.rect.y -= 2
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'left':
                muves.remove('left')
            p1.rect.y += 1
        if movement == "up" and muves[-1] != 'up':
            if GameState == "level1":
                for wall in walls:
                    if p1.rect.colliderect(wall.rect):
                        muves.append('up')
                        p1.rect.y += 2
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'left':
                muves.remove('left')
            p1.rect.y -= 1

    pygame.display.update()
    clock.tick(FPS)
