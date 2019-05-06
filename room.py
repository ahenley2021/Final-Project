import pygame
from pygame.locals import *

class Room(pygame.sprite.Sprite):
    def __init__(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        super().__init__()
        self.x = topLeftX
        self.y = topLeftY
        self.rect = pygame.Rect(self.x, self.y, bottomRightX, bottomRightY)
