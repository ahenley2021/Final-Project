import pygame, sys, random, time
from pygame.locals import *

from gardener import Character
from room import Room
from accuse import Accuse

pygame.init()

FPS = 10

rooms = pygame.sprite.Group()
accuse_options = pygame.sprite.Group()

gardener = Character()

tLeft = Room(10, 0, 70, 35)
tMid = Room(100, 0, 125, 40)
tRight = Room(245, 0, 65, 25)

rTop = Room(296, 654, 105, 106)
rBottom = Room(335, 200, 65, 50)

bRight = Room(150, 265, 90, 35)
bLeft = Room(0, 230, 70, 70)

left = Room(0, 80, 45, 45)

alice = Accuse(0, 120, 77, 45)
gustav = Accuse(90, 120, 70, 95)
george = Accuse(175, 120, 65, 95)
cat = Accuse(270, 120, 65, 95)

accuse_box = Accuse(345, 0, 55, 20)

rooms.add(tLeft, tMid, tRight, rTop, rBottom, bLeft, bRight, left)
accuse_options.add(alice, gustav, george, cat)

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Clue")

BACKGROUND = pygame.image.load('resources/background.png')
background_x = 0
background_y = 0

ROOM_BACKROUND = pygame.image.load('resources/room_background.png')
room_background_x = 0
room_background_y = 0

ACCUSE_BACKGROUND = pygame.image.load('resources/accuse_background.png')
accuse_background_x = 0
accuse_background_y = 0

OPENING = pygame.image.load('resources/opening.png')
opening_x = 0
opening_y = 0

time = 0
click_x, click_y = pygame.mouse.get_pos()

num_moves = 0
win = False
game_over = False

def read_file():
    f = open('hints.txt')
    f.read()
    f.close()

def display_message(text, x, y, z):
    BASICFONT = pygame.font.Font('freesansbold.ttf', z)
    Surf = BASICFONT.render(text, 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = x, y
    DISPLAYSURF.blit(Surf, Rect)

def accuse_box():
    display_message("Accuse", 345, 0, 10)
    is_collision()

def beginning_hints():
    if time <= 300:
        DISPLAYSURF.blit(OPENING,(opening_x, opening_y))
        display_message("Mr. Lavisham was killed on Sunday. It is currently Monday morning.", 50, 25, 11)
        display_message("The suspects are: Alice, the maid; Gustav, the cook;", 50, 40, 11)
        display_message("George, the neighbor; or Lord Remington, Mr. Lavisham’s cat.", 50, 50, 11)
        display_message("One of the pans as well as a silver tray have gone missing", 50, 70, 11)
        display_message("since the murder.", 50, 80, 11)
        display_message("Both Alice and Gustav were petitioning for higher wages", 50, 90, 11)
        display_message("when Mr. Lavisham died.", 50, 100, 11)
        display_message("The cat seems to be wracked with guilt.", 50, 120, 11)
        display_message("The day before he died, Mr. Lavisham cut the branches off", 50, 135, 11)
        display_message("the neighbor’s tree because it was leaning over into his property.", 50, 145, 11)
    else:
        DISPLAYSURF.blit(BACKGROUND,(background_x, background_y))
        is_collision()

def roll_dice():
    num_dice = random.randint(1, 7)
    if gardener.num_moves == num_dice:
        num_dice = 0

def new_hint():
    chosen_hint = random.randint(1, 14)
    f = open("hints.txt", "r")
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if chosen_hint == line:
            display_message(line, 150, 150, 11)

def leave_room():
    display_message("Leave", 345, 0, 11)
    """if pygame.sprite.spritecollideany(click, Rect):
        DISPLAYSURF.blit(BACKROUND,(background_x, background_y))
        gardener.num_moves == 0"""

def accuse_alice():
    display_message("Alice", 0, 120, 11)
    is_collision()

def accuse_gustav():
    display_message("Gustav", 90, 120, 11)
    is_collision()

def accuse_george():
    display_message("George", 175, 120, 11)
    is_collision()

def accuse_cat():
    display_message("Lord Remington", 270, 120, 11)
    is_collision()

def question_box():
    display_message("Who do you accuse?", 65, 35, 11)

def win():
    if win == True:
        display_message("You win!")
    elif win == False:
        display_message("You lost.")

def is_collision():
    global game_over
    #print("uwu")
    if time >= 300:

        if pygame.sprite.spritecollideany(gardener, rooms):
            DISPLAYSURF.blit(ROOM_BACKROUND,(room_background_x, room_background_x))
            new_hint()

        else:
            win = False
            leave_room()

    """    elif pygame.sprite.(click, accuse_box):
            DISPLAYSURF.blit(ACCUSE_BACKGROUND,(accuse_background_x, accuse_background_y))
            accuse_alice()
            accuse_gustav()
            accuse_george()
            accuse_cat()

        elif gardener.x >= 400 or gardener.x <= 0 or gardener.y >= 300 or gardener.y <= 0:
            game_over = True

        elif pygame.sprite.spritecollide(click, accuse_options, True):
            if pygame.sprite.spritecollide(click, george, True):
                win = True
                game_over = True
            else:
                win = False
                game_over = False """

while True:
    if game_over == False:
        read_file()
        beginning_hints()
        DISPLAYSURF.blit(gardener.image,(gardener.rect.x, gardener.rect.y))
        #accuse_box()
        #roll_dice()
        #is_collision()
        #DISPLAYSURF.blit(gardener.image,(gardener.rect.x, gardener.rect.y))
        time += 1
    if game_over == True:
        win()
        gardener.kill()
        rooms.kill()
        accuse.kill()
    for event in pygame.event.get():
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
    pygame.display.update()
