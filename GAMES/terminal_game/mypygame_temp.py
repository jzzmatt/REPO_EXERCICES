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


#STEP 3 HANDLE EVENT
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


    #===> DRAW SURFACE


    #====> DISPLAY THE SURFACE


    #=====> UPDATE THE SURFACE











