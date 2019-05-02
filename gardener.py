import pygame
from pygame.locals import *

CHARACTER = pygame.image.load('resources/ufo.png')

ground = 290

class character(pygame.sprite.Sprite):
    def __init__(self,ground):
        super().__init__()
        self.x = 300
        self.y = 370
        self.image = CHARACTER
        self.rect = pygame.Rect(self.x, self.y, 35, 25)

    def up(self):
        self.rect.y -= 10

    def down(self):
        self.rect.y += 10

    def right(self):
        self.rect.x += 10

    def left(self):
        self.rect.x -= 10
