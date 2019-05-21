import pygame
from pygame.locals import *

ROOM_BACKGROUND = pygame.image.load('resources/room_background.png')

#creates class and establishes variables for hitboxes, points, etc
class Room(pygame.sprite.Sprite):
    def __init__(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        super().__init__()
        self.x = topLeftX
        self.y = topLeftY
        self.image = ROOM_BACKGROUND
        self.rect = pygame.Rect(self.x, self.y, bottomRightX, bottomRightY)
