import sys
import pygame
from pygame import *
import random
from datetime import datetime

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
mixer.music.set_volume(0.1)


# Не Змінні
BACK = (48, 55, 99)
FPS = 60
# Змінні
GameState = 'menu'
movement = None
ballMovement = None
muves = [True]
timerActive1 = False
playerXP = 1
points = []
bigPoints = []

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, size):
        super().__init__()
        self.image = transform.scale(image.load(img), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Label():
    def __init__(self,  x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = BACK

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

"""Спрайти"""
# Кнопки
mazeTxt = GameSprite('maze.png', 215, 115, (270, 115))
btnStart = GameSprite('start.png', 265, 270, (170, 73))
btnExit = GameSprite('exit.png', 265, 358, (170, 73))
btnLeftArrow = GameSprite('LeftArrow.png', 3, 5, (80, 40))
btnOne = GameSprite('one.png', 125, 125, (100, 100))
GameOverText = Label(80, 256, 0, 0)
GameOverText.set_text('Game Over', 100, (150, 0, 0))
VictoryText = Label(140, 256, 0, 0)
VictoryText.set_text('Victory!', 100, (0, 150, 0))
# Стіни
l1w1x = GameSprite('Wall.png', 86, 87.5, (5, 527))
l1w2x = GameSprite('Wall.png', 613, 86, (5, 530))
l1w3y = GameSprite('Wall.png', 86, 86, (527, 5))
l1w4y = GameSprite('Wall.png', 86, 614.5, (530, 5))
l1w5y = GameSprite('Wall.png', 172, 173, (90, 5))
l1w6x = GameSprite('Wall.png', 172, 173, (5, 90))
l1w7y = GameSprite('Wall.png', 349, 89, (5, 177))
l1w8x = GameSprite('Wall.png', 261, 261, (90, 5))
l1w9y = GameSprite('Wall.png', 261, 261, (5, 177))
l1w10x = GameSprite('Wall.png', 86, 349, (90, 5))
l1w11y = GameSprite('Wall.png', 172, 438, (5, 90))
l1w12y = GameSprite('Wall.png', 172, 526, (90, 5))
l1w13y = GameSprite('Wall.png', 261, 526, (5, 90))
l1w14y = GameSprite('Wall.png', 349, 349, (5, 177))
l1w15x = GameSprite('Wall.png', 261, 438, (90, 5))
l1w16x = GameSprite('Wall.png', 437, 174, (90, 5))
l1w17y = GameSprite('Wall.png', 437, 174, (5, 177))
l1w18x = GameSprite('Wall.png', 439, 261, (177, 5))
l1w19x = GameSprite('Wall.png', 438, 438, (90, 5))
l1w20x = GameSprite('Wall.png', 438, 438, (5, 90))
l1w21x = GameSprite('Wall.png', 438, 526, (90, 5))
l1w22y = GameSprite('Wall.png', 524, 351, (5, 90))
walls = [l1w1x, l1w2x, l1w3y, l1w4y, l1w5y, l1w6x, l1w7y, l1w8x, l1w9y, l1w10x, l1w11y,
         l1w12y, l1w13y, l1w15x, l1w14y, l1w18x, l1w16x, l1w17y, l1w21x, l1w20x, l1w22y, l1w19x]
# Персонажі
player = GameSprite('tankUp.png', 100, 100, (60, 60))
ball1 = GameSprite('Wall.png', 100, 100, (3, 3))
mank1 = GameSprite("mankUp.png", 275, 360, (60, 60))
mank2 = GameSprite("mankUp.png", 544, 183, (60, 60))
monster = [mank1, mank2]
gold = GameSprite("gold.png", 458, 196, (50, 50))
smallGold = GameSprite("smallGold.png", 456, 462, (50, 50))


directionRight = ("left", "up", "down")
directionLeft = ("right", "up", "down")
directionDown = ("left", "up", "right")
directionUp = ("left", "right", "down")
direction = ('left', "right", "down", "up")
direction1 = random.choice(direction)
direction2 = random.choice(direction)

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
        if timerActive1 == False:
            ball1.remove()
        else:
            ball1.draw()
        if playerXP == 1:
            gold.draw()
        btnLeftArrow.draw()
        player.draw()
        mank1.draw()
        mank2.draw()
        for w in walls:
            w.draw()
        if player.rect.colliderect(mank1.rect):
            playerXP -= 1
        if player.rect.colliderect(mank2.rect):
            playerXP -= 1
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
            if GameState == 'level1' and mx > 100 and my > 100:
                if movement == 'up':
                    ballMovement = 'up'
                    ball1.rect.x = player.rect.x + 29
                    ball1.rect.y = player.rect.y
                    timerActive1 = True
                    start1 = datetime.now()
                    start = int(start1.strftime("%S"))
                if movement == 'down':
                    ballMovement = 'down'
                    ball1.rect.x = player.rect.x + 29
                    ball1.rect.y = player.rect.y + 57
                    timerActive1 = True
                    start1 = datetime.now()
                    start = int(start1.strftime("%S"))
                if movement == 'right':
                    ballMovement = 'right'
                    ball1.rect.x = player.rect.x + 57
                    ball1.rect.y = player.rect.y + 28
                    timerActive1 = True
                    start1 = datetime.now()
                    start = int(start1.strftime("%S"))
                if movement == 'left':
                    ballMovement = 'left'
                    ball1.rect.x = player.rect.x
                    ball1.rect.y = player.rect.y + 29
                    timerActive1 = True
                    start1 = datetime.now()
                    start = int(start1.strftime("%S"))
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
    if player.rect.colliderect(gold.rect):
        playerXP += 1
        gold.remove()
    for wall in walls:
        if ball1.rect.colliderect(wall.rect):
            timerActive1 = False
    if timerActive1:
        now1 = datetime.now()
        now = int(now1.strftime("%S"))
        period_int = now - start
        period = str(now - start)
        if period_int == 9:
            timerActive1 = False
        if period_int <= -1:
            timerActive1 = False
        if ballMovement == 'right':
            ball1.rect.x += 5
        if ballMovement == 'left':
            ball1.rect.x -= 5
        if ballMovement == 'down':
            ball1.rect.y += 5
        if ballMovement == 'up':
            ball1.rect.y -= 5
    if playerXP <= 0:
        movement = None
        GameOverText.draw()
    if playerXP >= 2:
        VictoryText.draw()
    if GameState == 'level1':
        if movement == "right" and muves[-1] != 'right':
            player = GameSprite('tankRight.png', player.rect.x, player.rect.y, (60, 60))
            for wall in walls:
                if player.rect.colliderect(wall.rect):
                    muves.append('right')
                    player.rect.x -= 4
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'left':
                muves.remove('left')
            player.rect.x += 2
        if movement == "left" and muves[-1] != 'left':
            player = GameSprite('tankLeft.png', player.rect.x, player.rect.y, (60, 60))
            for wall in walls:
                if player.rect.colliderect(wall.rect):
                    muves.append('left')
                    player.rect.x += 4
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'right':
                muves.remove('right')
            player.rect.x -= 2
        if movement == "down" and muves[-1] != 'down':
            player = GameSprite('tankDown.png', player.rect.x, player.rect.y, (60, 60))
            for wall in walls:
                if player.rect.colliderect(wall.rect):
                    muves.append('down')
                    player.rect.y -= 4
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'left':
                muves.remove('left')
            player.rect.y += 2
        if movement == "up" and muves[-1] != 'up':
            player = GameSprite('tankUp.png', player.rect.x, player.rect.y, (60, 60))
            if GameState == "level1":
                for wall in walls:
                    if player.rect.colliderect(wall.rect):
                        muves.append('up')
                        player.rect.y += 4
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'left':
                muves.remove('left')
            player.rect.y -= 2
        if direction1 == "right":
            mank1 = GameSprite('mankRight.png', mank1.rect.x, mank1.rect.y, (60, 60))
            mank1.rect.x += 1
            for wall in walls:
                if mank1.rect.colliderect(wall.rect):
                    direction1 = random.choice(directionRight)
                    mank1.rect.x -= 2
        if direction1 == "left":
            mank1 = GameSprite('mankLeft.png', mank1.rect.x, mank1.rect.y, (60, 60))
            mank1.rect.x -= 1
            for wall in walls:
                if mank1.rect.colliderect(wall.rect):
                    direction1 = random.choice(directionLeft)
                    mank1.rect.x += 2
        if direction1 == "down":
            mank1 = GameSprite('mankDown.png', mank1.rect.x, mank1.rect.y, (60, 60))
            mank1.rect.y += 1
            for wall in walls:
                if mank1.rect.colliderect(wall.rect):
                    direction1 = random.choice(directionDown)
                    mank1.rect.y -= 2
        if direction1 == "up":
            mank1 = GameSprite('mankUp.png', mank1.rect.x, mank1.rect.y, (60, 60))
            mank1.rect.y -= 1
            for wall in walls:
                if mank1.rect.colliderect(wall.rect):
                    direction1 = random.choice(directionUp)
                    mank1.rect.y += 3
        if direction2 == "right":
            mank2 = GameSprite('mankRight.png', mank2.rect.x, mank2.rect.y, (60, 60))
            mank2.rect.x += 1
            for wall in walls:
                if mank2.rect.colliderect(wall.rect):
                    direction2 = random.choice(directionRight)
                    mank2.rect.x -= 2
        if direction2 == "left":
            mank2 = GameSprite('mankLeft.png', mank2.rect.x, mank2.rect.y, (60, 60))
            mank2.rect.x -= 1
            for wall in walls:
                if mank2.rect.colliderect(wall.rect):
                    direction2 = random.choice(directionLeft)
                    mank2.rect.x += 2
        if direction2 == "down":
            mank2 = GameSprite('mankDown.png', mank2.rect.x, mank2.rect.y, (60, 60))
            mank2.rect.y += 1
            for wall in walls:
                if mank2.rect.colliderect(wall.rect):
                    direction2 = random.choice(directionDown)
                    mank2.rect.y -= 2
        if direction2 == "up":
            mank2 = GameSprite('mankUp.png', mank2.rect.x, mank2.rect.y, (60, 60))
            mank2.rect.y -= 1
            for wall in walls:
                if mank2.rect.colliderect(wall.rect):
                    direction2 = random.choice(directionUp)
                    mank2.rect.y += 3
    pygame.display.update()
    clock.tick(FPS)
