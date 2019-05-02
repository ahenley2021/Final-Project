import pygame, sys, random
from pygame.locals import *

from gardener import Character
from room import Room
from accuse import Accuse

pygame.init()

FPS = 10

rooms = pygame.sprite.Group()

gardener = Character()
tLeft = Room(10, 0)
tMid = Room(100, 0)
tRight = Room(245, 0)

rTop = Room(296, 65)
rBottom = Room(335, 200)

bRight = Room(150, 265)
bLeft = Room(0, 230)

lLeft = Room(0, 80)
