#!/usr/bin/env python3
# -*- coding : utf-8 -*-
#---> MODULES IMPORT
import pygame
from pygame.locals import *
from sys import *
from random import *

#STEP 1 INITIALIZATION
check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) had {0} initializing errors, exiting...".format(check_errors[1]))


else:
    print("(+) Pygame Successfully Initialised ")



#STEP 2 DEFINE WINDOWS OR SURFACE SIZE
windows_size = (500, 400)
screen_surface = pygame.display.set_mode(windows_size, 0, 32)
pygame.display.set_caption("Game Template")

#2.1 DEFINE COLOR RGB (Red Green Blue)
WHITE = (255,255,255)
BLUE_LIGTH = (185, 240, 240)
RED = (255, 0, 0)
GREEN = (0,255,0)
MARRON = (145, 35, 30)
BLUE = (0,0,255)
YELLOW = (255, 255,0)
BLACK = (0, 0, 0)


#STEP 3 BODY GAME & HANDLE EVENT
exit_game = False


while not exit_game:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game = True
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit_game = True
                exit()


    #==> UPDATE OBJECT (Movement, Collision, outofBoard, Score,...)


    # ====> DISPLAY THE SURFACE | WHILE you have a BaKGround Use BLIT Method
    screen_surface.fill(BLUE_LIGTH)


    #===> DRAW ON SURFACE (can be Built-ins or Image)
    #pygame.draw.line(screen_surface, RED, (20, 40), (200,300), 5)
    #pygame.draw.rect(screen_surface, MARRON, pygame.Rect(200, 30, 200, 100), 3)





    #=====> UPDATE THE SURFACE
    pygame.display.update()











