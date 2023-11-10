import pygame
from pygame import *
import sys

screen_width = 700
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))
img = image.load('background.png')
background = transform.scale(img, (700, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Catch_up")
icon = pygame.image.load('sprite1.png')
pygame.display.set_icon(icon)

class Sprite(sprite.Sprite):
    def __init__(self, ing_image, x, y, size):
        super().__init__()

        self.image = transform.scale(image.load(ing_image), size)

        self.x = x
        self.y = y

    def draw(self):
        window.blit(self.image, (self.x, self.y))

speed = 10

sprite2 = Sprite("sprite2.png", 300, 300, (50, 50))
sprite1 = Sprite("sprite1.png", 100, 100, (50, 50))



while True:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keyPrs = key.get_pressed()

    if keyPrs[K_LEFT] and sprite1.x > 5:
        sprite1.x -= speed
    if keyPrs[K_RIGHT] and sprite1.x < 650:
        sprite1.x += speed
    if keyPrs[K_UP] and sprite1.y > 1:
        sprite1.y -= speed
    if keyPrs[K_DOWN] and sprite1.y < 450:
        sprite1.y += speed

    if keyPrs[K_a] and sprite2.x > 5:
        sprite2.x -= speed
    if keyPrs[K_d] and sprite2.x < 650:
        sprite2.x += speed
    if keyPrs[K_w] and sprite2.y > 1:
        sprite2.y -= speed
    if keyPrs[K_s] and sprite2.y < 450:
        sprite2.y += speed

    sprite1.draw()
    sprite2.draw()

    pygame.display.update()
    clock.tick(60)
