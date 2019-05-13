import pygame
from pygame.locals import *

CHARACTER = pygame.image.load('resources/character.png')

ground = 290

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 250
        self.y = 370
        self.image = CHARACTER
        self.rect = pygame.Rect(self.x, self.y, 35, 25)
        self.num_moves = 0

    def up(self):
        self.rect.y -= 10
        self.num_moves += 1

    def down(self):
        self.rect.y += 10
        self.num_moves += 1

    def right(self):
        self.rect.x += 10
        self.num_moves += 1

    def left(self):
        self.rect.x -= 10
        self.num_moves += 1
