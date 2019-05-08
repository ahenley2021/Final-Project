import pygame, sys, random, time
from pygame.locals import *

from gardener import Character
from room import Room
from accuse import Accuse

pygame.init()

FPS = 10

rooms = pygame.sprite.Group()

accuse = Accuse()
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

hint_time = pygame.time.get_ticks()

num_moves = 0
win = False
game_over = False

def read_file():
    f = open('hints.txt')
    f.read()
    f.close()

def display_message(x, y):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    Surf = BASICFONT.render(text, 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = x, y
    DISPLAYSURF.blit(Surf, Rect)

def accuse_box():
    display_message("Accuse")

def beginning_hints(100, 5):
    if hint_time > 120:
        display_message("Mr. Lavisham was killed on Sunday. It is currently Monday morning.")
        display_message("The suspects are: Alice, the maid; Gustav, the cook; George, the neighbor; or Lord Remington, Mr. Lavisham’s cat.")
        display_message("One of the pans as well as a silver tray have gone missing since the murder.")
        display_message("Both Alice and Gustav were petitioning for higher wages when Mr. Lavisham died.")
        display_message("The cat seems to be wracked with guilt.")
        display_message("The day before he died, Mr. Lavisham cut the branches off the neighbor’s tree because it was leaning over into his property.")

def roll_dice():
    num_dice = random.randint(1, 7)
    if gardener.num_moves == num_dice:
        num_dice = 0

def new_hint(350, 5):
    chosen_hint = random.randint(1, 14)
    f = open("hints.txt", "r")
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if chosen_hint == line:
            display_message(line)

def leave_room(345, 0):
    display_message("Leave")
    if pygame.sprite.spritecollideany(gardener, Rect):
        DISPLAYSURF.blit('resources/background.png')
        gardener.num_moves == 0

def accuse_alice(0, 120):
    display_message("Alice")

def accuse_gustav(90, 120):
    display_message("Gustav")

def accuse_george(175, 120):
    display_message("George")

def accuse_cat(270, 120):
    display_message("Lord Remington")

def question_box(65, 35):
    display_message("Who do you accuse?")

def win(200, 150):
    if win == True:
        display_message("You win!")

def is_collision():
    global game_over
    if pygame.sprite.spritecollideany(gardener, rooms):
        DISPLAYSURF.blit('resources/room_background.png')
        new_hint()
    elif gardener.x >= 400 or gardener.x <= 0 or gardener.y >= 300 or gardener.y <= 0:
        game_over == True

While True:
    if game_over == False:
        read_file()
        beginning_hints()
        DISPLAYSURF.blit('resources/background.png')
    if game_over == True:
        win()
        gardener.kill()
        rooms.kill()
        accuse.kill()
    for even in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_UP:
            gardener.up()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            gardener.down()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            gardener.right()
        elif event.type == KEYDOWN and event.key == K_LEFT:
            gardener.left()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #end it
