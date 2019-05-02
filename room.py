import pygame
from pygame.locals import *

class Room(pygame.sprite.Sprite):
    def __init__(self, topLeft, bottomRight):
        super().__init__()
        self.x = topLeft
        self.y = bottomRight
