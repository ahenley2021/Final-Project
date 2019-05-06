import pygame, sys, random
from pygame.locals import *

from gardener import Character
from room import Room
from accuse import Accuse

pygame.init()

FPS = 10

rooms = pygame.sprite.Group()

gardener = Character()
tLeft = Room(10, 0, 80, 35)
tMid = Room(100, 0, 225, 40)
tRight = Room(245, 0, 310, 25)

rTop = Room(296, 654, 400, 171)
rBottom = Room(335, 200, 400, 250)

bRight = Room(150, 265, 240, 300)
bLeft = Room(0, 230, 70, 300)

left = Room(0, 80, 45, 125)

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Clue")

def read_file():
    f = open('hints.txt')
    f.read()
    f.close()

def accuse_box():
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    Surf = BASICFONT.render(text, 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = 345, 0
    DISPLAYSURF.blit(Surf, Rect)
    display_message("Accuse")
