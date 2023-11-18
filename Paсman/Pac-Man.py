import sys
import pygame
from pygame import *
import random
from datetime import datetime
pygame.init()
FPS = 60
"""Звуки"""
sound = ["button_click.mp3", "hit_sound.mp3", "teleport.mp3", 'monster_dead.mp3']
mixer.init()
mixer.music.load(sound[0])
mixer.music.set_volume(0.1)

"""Кольори"""

back = (48, 55, 99)#Фон

RED = (255, 0, 0)
GREEN = (0, 190, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
BLACK = (0, 0, 0)

"""створення вікна програми"""
screen_width = 715
screen_height = 730
screen = pygame.display.set_mode((screen_width, screen_height)) #Вікно програми
clock = pygame.time.Clock()
pygame.display.set_caption("Pac-Man")
icon = pygame.image.load('Monster_red_right.png')
pygame.display.set_icon(icon)
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(screen, frame_color, self.rect, thickness)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Sprite(sprite.Sprite):
    def __init__(self, img, x, y, size):
        super().__init__()

        self.image = transform.scale(image.load(img), size)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

"""Персонажі"""
Pacman = Sprite('Pacman_right.png', 70, 81, (50, 50))
Monster_blue = Sprite("Monster_blue_right.png", 263, 282, (50, 50))
Monster_yellow = Sprite("Monster_yellow_right.png", 326, 282, (50, 50))
Monster_red = Sprite("Monster_red_right.png", 391, 282, (50, 50))
Monster_green = Sprite("Monster_green_right.png", 432, 282, (50, 50))
Monster_pink = Sprite("Monster_pink_right.png", 312, 282, (50, 50))
"""Головне меню"""
button_start = Sprite("Start.png", 220, 250, (275, 119))
button_exit = Sprite("Exit.png", 220, 400, (274, 119))
Pac_man_text = Sprite("Pac-man.png", 150, 30, (425, 166))
button_setting = Sprite("Setting.png", 220, 600, (275, 119))
"""Налаштування"""

control_text = Label(230, 20, 1, 1, back)
control_text.set_text("Керування", 50, WHITE)
control_outline = Area(220, 20, 300, 72, WHITE)

classic = Label(110, 130, 1, 1, back)
classic.set_text("Класичне", 45, WHITE)

arrows = Label(370, 130, 1, 1, back)
arrows.set_text("Стрілками", 45, WHITE)

about_game = Label(295, 500, 1, 1, back)
about_game.set_text("Про гру", 40, WHITE)
about_game_outline = Area(280, 500, 190, 59, WHITE)

classic_outline = Area(100, 120, 250, 80, WHITE)
arrows_outline = Area(360, 120, 260, 80, WHITE)
"""Вибір рівня"""
button_one = Sprite("One.png", 90, 100, (150, 150))
button_two = Sprite("Two.png", 290, 100, (150, 150))
button_three = Sprite("Three.png", 490, 100, (150, 150))
left_arrow = Sprite("Left_arrow.png", 10, 10, (81, 46))

'''Інтерфейс'''

score_text = Label(170, 5, 50, 50, back)
score_text.set_text("Рахунок:", 40, WHITE)

score_text1 = Label(360, 5, 50, 50, back)

game_over_text = Label(175, 300, 50, 50, back)
game_over_text.set_text("Game-Over", 70, RED)

h1 = Sprite('heart.png', 625, 15, (40, 36))
h2 = Sprite('heart.png', 575, 15, (40, 36))
h3 = Sprite("heart.png", 525, 15, (40, 36))

"""1 рівень"""

map_frame_x = Sprite("wall_x.png", 60, 70, (592, 10))
map_frame_y = Sprite("wall_y.png", 60, 70, (10, 600))
map_frame_x1 = Sprite("wall_x.png", 60, 665, (594, 10))
map_frame_y1 = Sprite("wall_y.png", 644, 70, (10, 600))
wall_x = Sprite("wall_x.png", 60, 137, (72, 8))
wall_y = Sprite("wall_y.png", 189, 70, (8, 74))
wall_x1 = Sprite("wall_x.png", 128, 202, (68, 8))
wall_y1 = Sprite("wall_y.png", 254, 141, (8, 70))
wall_x2 = Sprite("wall_x.png", 256, 138, (70, 8))
wall_x5 = Sprite('wall_x.png', 256, 204, (70, 8))
wall_x3 = Sprite("wall_x.png", 382, 138, (138, 8))
wall_y2 = Sprite("wall_y.png", 126, 203, (8, 348))
wall_y3 = Sprite("wall_y.png", 190, 203, (8, 404))
wall_y4 = Sprite("wall_y.png", 126, 608, (8, 63))
wall_x4 = Sprite("wall_x.png", 579, 138, (70, 8))
wall_x6 = Sprite('wall_x.png', 516, 204, (68, 8))
wall_y12 = Sprite('wall_y.png', 579, 207, (8, 71))
wall_y5 = Sprite('wall_y.png', 514, 139, (8, 72))
wall_y6 = Sprite('wall_y.png', 449, 204, (8, 272))
wall_x7 = Sprite('wall_x.png', 256, 336, (198, 8))
wall_y7 = Sprite('wall_y.png', 383, 204, (8, 74))
wall_x8 = Sprite('wall_x.png', 254, 270, (71, 8))
wall_y8 = Sprite('wall_y.png', 254, 339, (8, 72))
wall_x9 = Sprite('wall_x.png', 318, 402, (74, 8))
wall_x10 = Sprite('wall_x.png', 190, 468, (70, 8))
wall_y14 = Sprite('wall_y.png', 254, 469, (8, 74))
wall_y13 = Sprite('wall_y.png', 318, 468, (8, 74))
wall_y9 = Sprite('wall_y.png', 579, 602, (8, 65))
wall_x12 = Sprite('wall_x.png', 580, 600, (65, 8))
wall_y10 = Sprite('wall_y.png', 448, 535, (8, 70))
wall_x13 = Sprite('wall_x.png', 450, 600, (70, 8))
wall_x18 = Sprite('wall_x.png', 382, 534, (71, 8))
wall_x14 = Sprite('wall_x.png', 514, 468, (70, 8))
wall_y11 = Sprite('wall_y.png', 579, 470, (8, 71))
wall_x11 = Sprite('wall_x.png', 514, 534, (70, 8))
wall_x15 = Sprite('wall_y.png', 514, 400, (140, 8))
wall_x16 = Sprite('wall_x.png', 579, 336, (70, 8))
wall_x17 = Sprite('wall_x.png', 452, 270, (70, 8))
wall_x19 = Sprite('wall_x.png', 192, 601, (70, 8))
wall_x20 = Sprite('wall_x.png', 320, 601, (70, 8))
wall_y15 = Sprite('wall_y.png', 318, 603, (8, 68))

Walls = [map_frame_x, map_frame_y, map_frame_x1, map_frame_y1, wall_x, wall_y, wall_x1, wall_y1, wall_x2,
         wall_x3, wall_y2, wall_y3, wall_y4, wall_x4, wall_x5, wall_x6, wall_y5, wall_y6, wall_x7, wall_y7,
         wall_x8, wall_y8, wall_x9, wall_x10, wall_y9, wall_x11, wall_x12, wall_y10, wall_x13, wall_x14, wall_y11,
         wall_x15, wall_x16, wall_x17, wall_y12, wall_y13, wall_x18, wall_x19, wall_y14, wall_x20, wall_y15]

Point = []
Big_point = []

count = 8#1
for j in range(1):
    x = 90
    y = 170
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 8#2
for j in range(1):
    x = 155
    y = 170
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 9#3
for j in range(1):
    x = 219 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 9#4
for j in range(1):
    x = 283 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 9#5
for j in range(1):
    x = 350 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 9#6
for j in range(1):
    x = 414 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 9#7
for j in range(1):
    x = 479 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 9#8
for j in range(1):
    x = 547 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1
count = 8#9
for j in range(1):
    x = 608 + (27.5 * j)
    y = 105 + (55 * j)
    for i in range(count):
        point = Sprite('Money.png', x, y, (10, 10))
        Point.append(point)
        y += 66
    count += 1

point1 = Sprite('Money++.png', 85, 622, (20, 20))
Big_point.append(point1)
point2 = Sprite('Money++.png', 281, 164, (20, 20))
Big_point.append(point2)
point3 = Sprite('Money++.png', 600, 360, (20, 20))
Big_point.append(point3)
point4 = Sprite('Money++.png', 541, 495, (20, 20))
Big_point.append(point4)
point5 = Sprite('Money++.png', 343, 624, (20, 20))
Big_point.append(point5)
point6 = Sprite('Money++.png', 600, 99, (20, 20))
Big_point.append(point6)
point7 = Sprite('Money++.png', 213, 495, (20, 20))
Big_point.append(point7)

"""Змінні"""
move_left = False
move_right = False
move_down = False
move_up = False
pacman = 'normal'

direction_right = ("left", "up", "down")
direction_left = ("right", "up", "down")
direction_down = ("left", "up", "right")
direction_up = ("left", "right", "down")
direction = ('left', "right", "down", "up")
direction_blue = random.choice(direction)
direction_yellow = random.choice(direction)
direction_red = random.choice(direction_right)
direction_green = random.choice(direction_right)
direction_pink = random.choice(direction_right)

movement = None
status = "Menu"
muves = [True]
pacman_xp = 3
score = 0
timer_active = False
yellow = False
red = False
blue = False

while True:
    screen.fill(back)
    if status == "Menu":
        button_start.draw()
        button_exit.draw()
        Pac_man_text.draw()
        button_setting.draw()
    if status == "play":
        button_one.draw()
        button_two.draw()
        button_three.draw()
        left_arrow.draw()
    if status == "setting":
        left_arrow.draw()
        control_text.draw()
        control_outline.outline(WHITE, 8)
        classic.draw()
        arrows.draw()
        classic_outline.outline(WHITE, 6)
        arrows_outline.outline(WHITE, 6)
        about_game.draw()
        about_game_outline.outline(WHITE, 6)
    if status == "level_1":
        for p in Point:
            p.draw()
        for b in Big_point:
            b.draw()
        score_text1.set_text(str(score), 40, WHITE)
        score_text1.draw()
        Monster_blue.draw()
        Monster_red.draw()
        Monster_yellow.draw()
        score_text.draw()
        left_arrow.draw()
        Pacman.draw()
        h3.draw()
        h2.draw()
        h1.draw()
        for w in Walls:
            w.draw()
        if pacman_xp == 0:
            game_over_text.draw()
            movement = None
    if status == "level_2":
        left_arrow.draw()
        score_text.draw()
        score_text1.set_text(str(score), 40, WHITE)
        score_text1.draw()
        h3.draw()
        h2.draw()
        h1.draw()
        Pacman.draw()
    if status == "level_3":
        left_arrow.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if status == "Menu":
                if button_exit.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if button_start.rect.collidepoint(event.pos):
                    status = "play"
                    mixer.music.load(sound[0])
                    mixer.music.play()
                if button_setting.rect.collidepoint(event.pos):
                    status = "setting"
                    mixer.music.load(sound[0])
                    mixer.music.play()
            if status == "play":
                if left_arrow.rect.collidepoint(event.pos):
                    status = "Menu"
                    mixer.music.load(sound[0])
                    mixer.music.play()
                if button_one.rect.collidepoint(event.pos):
                    status = "level_1"
                    mixer.music.load(sound[0])
                    mixer.music.play()
                    Pacman.rect.x = 70
                    Pacman.rect.y = 81
                if button_two.rect.collidepoint(event.pos):
                    status = "level_2"
                    mixer.music.load(sound[0])
                    mixer.music.play()
                if button_three.rect.collidepoint(event.pos):
                    status = "level_3"
                    mixer.music.load(sound[0])
                    mixer.music.play()
            if status == "level_1" or "level_2":
                if left_arrow.rect.collidepoint(event.pos):
                    status = "Menu"
                    mixer.music.load(sound[0])
                    mixer.music.play()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print(Pacman.rect.x, Pacman.rect.y)
            if event.key == pygame.K_d:
                movement = "right"
            if event.key == pygame.K_a:
                movement = "left"
            if event.key == pygame.K_s:
                movement = "down"
            if event.key == pygame.K_w:
                movement = "up"

    """Рух"""
    if status == "level_1" or "level_2" or "level_3":
        """Pac-Man"""
        if movement == "right" and muves[-1] != 'right':
            if status == "level_1":
                for wall in Walls:
                    if Pacman.rect.colliderect(wall.rect):
                        muves.append('right')
                        Pacman.rect.x -= 4
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'left':
                muves.remove('left')
            Pacman.rect.x += 2
            if pacman == 'normal':
                Pacman = Sprite('Pacman_right.png',  Pacman.rect.x,  Pacman.rect.y, (50, 50))
            if pacman == 'super':
                Pacman = Sprite('Pacman_right_super.png',  Pacman.rect.x,  Pacman.rect.y, (50, 50))
        if movement == "left" and muves[-1] != 'left':
            if status == "level_1":
                for wall in Walls:
                    if Pacman.rect.colliderect(wall.rect):
                        muves.append('left')
                        Pacman.rect.x += 4
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'down':
                muves.remove('down')
            Pacman.rect.x -= 2
            if pacman == 'normal':
                Pacman = Sprite("Pacman_left.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            if pacman == 'super':
                Pacman = Sprite("Pacman_left_super.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
        if movement == "down" and muves[-1] != 'down':
            if status == "level_1":
                for wall in Walls:
                    if Pacman.rect.colliderect(wall.rect):
                        muves.append('down')
                        Pacman.rect.y -= 4
            if muves[-1] == 'up':
                muves.remove('up')
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'left':
                muves.remove('left')
            Pacman.rect.y += 2
            if pacman == 'normal':
                Pacman = Sprite("Pacman_down.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            if pacman == 'super':
                Pacman = Sprite("Pacman_down_super.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
        if movement == "up" and muves[-1] != 'up':
            if status == "level_1":
                for wall in Walls:
                    if Pacman.rect.colliderect(wall.rect):
                        muves.append('up')
                        Pacman.rect.y += 4
            if muves[-1] == 'down':
                muves.remove('down')
            if muves[-1] == 'right':
                muves.remove('right')
            if muves[-1] == 'left':
                muves.remove('left')
            Pacman.rect.y -= 2
            if pacman == 'normal':
                Pacman = Sprite("Pacman_up.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            if pacman == 'super':
                Pacman = Sprite("Pacman_up_super.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
        """Monster-blue"""
        if direction_blue == "right":
            Monster_blue = Sprite("Monster_blue_right.png", Monster_blue.rect.x, Monster_blue.rect.y, (50, 50))
            Monster_blue.rect.x += 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_blue.rect.colliderect(wall.rect):
                        Monster_blue.rect.x -= 2
                        direction_blue = random.choice(direction_right)
        if direction_blue == "left":
            Monster_blue = Sprite("Monster_blue_left.png", Monster_blue.rect.x, Monster_blue.rect.y, (50, 50))
            Monster_blue.rect.x -= 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_blue.rect.colliderect(wall.rect):
                        Monster_blue.rect.x += 2
                        direction_blue = random.choice(direction_left)
        if direction_blue == "down":
            Monster_blue = Sprite("Monster_blue_down.png", Monster_blue.rect.x, Monster_blue.rect.y, (50, 50))
            Monster_blue.rect.y += 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_blue.rect.colliderect(wall.rect):
                        Monster_blue.rect.y -= 2
                        direction_blue = random.choice(direction_down)
        if direction_blue == "up":
            Monster_blue = Sprite("Monster_blue_up.png", Monster_blue.rect.x, Monster_blue.rect.y, (50, 50))
            Monster_blue.rect.y -= 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_blue.rect.colliderect(wall.rect):
                        Monster_blue.rect.y += 2
                        direction_blue = random.choice(direction_up)
        """Monster-red"""
        if direction_red == "right":
            Monster_red = Sprite("Monster_red_right.png", Monster_red.rect.x, Monster_red.rect.y, (50, 50))
            Monster_red.rect.x += 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_red.rect.colliderect(wall.rect):
                        Monster_red.rect.x -= 2
                        direction_red = random.choice(direction_right)
        if direction_red == "left":
            Monster_red = Sprite("Monster_red_left.png", Monster_red.rect.x, Monster_red.rect.y, (50, 50))
            Monster_red.rect.x -= 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_red.rect.colliderect(wall.rect):
                        Monster_red.rect.x += 2
                        direction_red = random.choice(direction_left)
        if direction_red == "down":
            Monster_red = Sprite("Monster_red_down.png", Monster_red.rect.x, Monster_red.rect.y, (50, 50))
            Monster_red.rect.y += 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_red.rect.colliderect(wall.rect):
                        Monster_red.rect.y -= 2
                        direction_red = random.choice(direction_down)
        if direction_red == "up":
            Monster_red = Sprite("Monster_red_up.png", Monster_red.rect.x, Monster_red.rect.y, (50, 50))
            Monster_red.rect.y -= 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_red.rect.colliderect(wall.rect):
                        Monster_red.rect.y += 2
                        direction_red = random.choice(direction_up)
        """Monster-yellow"""
        if direction_yellow == "right":
            Monster_yellow = Sprite("Monster_yellow_right.png", Monster_yellow.rect.x, Monster_yellow.rect.y, (50, 50))
            Monster_yellow.rect.x += 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_yellow.rect.colliderect(wall.rect):
                        Monster_yellow.rect.x -= 2
                        direction_yellow = random.choice(direction_right)
        if direction_yellow == "left":
            Monster_yellow = Sprite("Monster_yellow_left.png", Monster_yellow.rect.x, Monster_yellow.rect.y, (50, 50))
            Monster_yellow.rect.x -= 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_yellow.rect.colliderect(wall.rect):
                        Monster_yellow.rect.x += 2
                        direction_yellow = random.choice(direction_left)
        if direction_yellow == "down":
            Monster_yellow = Sprite("Monster_yellow_down.png", Monster_yellow.rect.x, Monster_yellow.rect.y, (50, 50))
            Monster_yellow.rect.y += 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_yellow.rect.colliderect(wall.rect):
                        Monster_yellow.rect.y -= 2
                        direction_yellow = random.choice(direction_down)
        if direction_yellow == "up":
            Monster_yellow = Sprite("Monster_yellow_up.png", Monster_yellow.rect.x, Monster_yellow.rect.y, (50, 50))
            Monster_yellow.rect.y -= 1.5
            if status == "level_1":
                for wall in Walls:
                    if Monster_yellow.rect.colliderect(wall.rect):
                        Monster_yellow.rect.y += 2
                        direction_yellow = random.choice(direction_up)
    if status == "level_2" or "level_3":
        """Monster-green"""
        if direction_green == "right":
            Monster_green = Sprite("Monster_green_right.png", Monster_green.rect.x, Monster_green.rect.y, (50, 50))
            Monster_green.rect.x += 1.5
        if direction_green == "left":
            Monster_green = Sprite("Monster_green_left.png", Monster_green.rect.x, Monster_green.rect.y, (50, 50))
            Monster_green.rect.x -= 1.5
        if direction_green == "down":
            Monster_green = Sprite("Monster_green_down.png", Monster_green.rect.x, Monster_green.rect.y, (50, 50))
            Monster_green.rect.y += 1.5
        if direction_green == "up":
            Monster_green = Sprite("Monster_green_up.png", Monster_green.rect.x, Monster_green.rect.y, (50, 50))
            Monster_green.rect.y -= 1.5
    if status == "level_3":
        """Monster-pink"""
        if direction_pink == "right":
            Monster_pink = Sprite("Monster_pink_right.png", Monster_pink.rect.x, Monster_pink.rect.y, (50, 50))
            Monster_pink.rect.x += 1.5
        if direction_pink == "left":
            Monster_pink = Sprite("Monster_green_left.png", Monster_pink.rect.x, Monster_pink.rect.y, (50, 50))
            Monster_pink.rect.x -= 1.5
        if direction_pink == "down":
            Monster_pink = Sprite("Monster_pink_down.png", Monster_pink.rect.x, Monster_pink.rect.y, (50, 50))
            Monster_pink.rect.y += 1.5
        if direction_pink == "up":
            Monster_pink = Sprite("Monster_pink_up.png", Monster_pink.rect.x, Monster_pink.rect.y, (50, 50))
            Monster_pink.rect.y -= 1.5
    if timer_active != True and status == "level_1" and "level_2" and "level_3":
        if Pacman.rect.colliderect(Monster_red.rect):
            mixer.music.load(sound[1])
            mixer.music.play()
            Pacman.rect.x = 70
            Pacman.rect.y = 81
            pacman_xp -= 1
            if pacman_xp == 2:
                h1 = Sprite("dead.png", 625, 15, (40, 36))
            if pacman_xp == 1:
                h2 = Sprite("dead.png", 575, 15, (40, 36))
            if pacman_xp == 0:
                h3 = Sprite("dead.png", 525, 15, (40, 36))
        if Pacman.rect.colliderect(Monster_yellow.rect):
            mixer.music.load(sound[1])
            mixer.music.play()
            Pacman.rect.x = 70
            Pacman.rect.y = 81
            pacman_xp -= 1
            if pacman_xp == 2:
                h1 = Sprite("dead.png", 625, 15, (40, 36))
            if pacman_xp == 1:
                h2 = Sprite("dead.png", 575, 15, (40, 36))
            if pacman_xp == 0:
                h3 = Sprite("dead.png", 525, 15, (40, 36))
        if Pacman.rect.colliderect(Monster_blue.rect):
            mixer.music.load(sound[1])
            mixer.music.play()
            Pacman.rect.x = 70
            Pacman.rect.y = 81
            pacman_xp -= 1
            if pacman_xp == 2:
                h1 = Sprite("dead.png", 625, 15, (40, 36))
            if pacman_xp == 1:
                h2 = Sprite("dead.png", 575, 15, (40, 36))
            if pacman_xp == 0:
                h3 = Sprite("dead.png", 525, 15, (40, 36))
    if status == "level_2" or "level_3":
        if Pacman.rect.colliderect(Monster_green.rect):
            mixer.music.load(sound[1])
            mixer.music.play()
            Pacman.rect.x = 70
            Pacman.rect.y = 81
            pacman_xp -= 1
            if pacman_xp == 2:
                h1 = Sprite("dead.png", 625, 15, (40, 36))
            if pacman_xp == 1:
                h2 = Sprite("dead.png", 575, 15, (40, 36))
            if pacman_xp == 0:
                h3 = Sprite("dead.png", 525, 15, (40, 36))
    if status == "level_3":
        if Pacman.rect.colliderect(Monster_pink.rect):
            mixer.music.load(sound[1])
            mixer.music.play()
            Pacman.rect.x = 70
            Pacman.rect.y = 81
            pacman_xp -= 1
            if pacman_xp == 2:
                h1 = Sprite("dead.png", 625, 15, (40, 36))
            if pacman_xp == 1:
                h2 = Sprite("dead.png", 575, 15, (40, 36))
            if pacman_xp == 0:
                h3 = Sprite("dead.png", 525, 15, (40, 36))
    for p in Point:
        if Pacman.rect.colliderect(p.rect):
            if pacman == 'normal':
                Pacman = Sprite("Pacman_close.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            if pacman == 'super':
                Pacman = Sprite("Pacman_close_super.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            Point.remove(p)
            score += 1
    for b in Big_point:
        if Pacman.rect.colliderect(b.rect):
            if pacman == 'normal':
                Pacman = Sprite("Pacman_close.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            if pacman == 'super':
                Pacman = Sprite("Pacman_close_super.png", Pacman.rect.x, Pacman.rect.y, (50, 50))
            Big_point.remove(b)
            score += 4
            timer_active = True
            start1 = datetime.now()
            start = int(start1.strftime("%S"))
            pacman = 'super'
    if timer_active:
        now1 = datetime.now()
        now = int(now1.strftime("%S"))
        period_int = now - start
        period = str(now - start)
        if period_int == 9:
            timer_active = False
            yellow = False
            blue = False
            red = False
            pacman = 'normal'
        if period_int <= -1:
            timer_active = False
            yellow = False
            blue = False
            red = False
            pacman = "normal"
        if blue == False:
            if Pacman.rect.colliderect(Monster_blue.rect):
                mixer.music.load(sound[3])
                mixer.music.play()
                score += 50
                monster_blue_x_l1 = 263
                monster_blue_y_l1 = 282
                blue = True
        if red == False:
            if Pacman.rect.colliderect(Monster_red.rect):
                mixer.music.load(sound[3])
                mixer.music.play()
                score += 50
                monster_red_x_l1 = 391
                monster_red_y_l1 = 282
                red = True
        if yellow == False:
            if Pacman.rect.colliderect(Monster_yellow.rect):
                mixer.music.load(sound[3])
                mixer.music.play()
                score += 50
                monster_yellow_x_l1 = 326
                monster_yellow_y_l1 = 282
                yellow = True
    pygame.display.update()
    clock.tick(FPS)