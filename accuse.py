import pygame
from pygame.locals import *

ACCUSE_BACKGROUND = pygame.image.load('resources/accuse_background.png')

#creates class for accusing screen
class Accuse(pygame.sprite.Sprite):
    def __init__(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        super().__init__()
        self.x = topLeftX
        self.y = topLeftY
        self.image = ACCUSE_BACKGROUND
        self.rect = pygame.Rect(self.x, self.y, bottomRightX, bottomRightY)
