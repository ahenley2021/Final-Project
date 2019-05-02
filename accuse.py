import pygame
from pygame.locals import *

class Accuse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 345
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 55, 20)
