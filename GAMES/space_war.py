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
windows_size = (640, 480)
screen_surface = pygame.display.set_mode(windows_size, 0, 32)
pygame.display.set_caption("Space War")



#2.0 Import or Load Image
img_background = 'imge_background.png'
img_spaceship = 'imge_spaceship1.png'
background = pygame.image.load(img_background).convert()
spaceship = pygame.image.load(img_spaceship).convert_alpha()
background_cord = background.get_rect()
spaceship_rect = spaceship.get_rect(midbottom =(320, 480))
#x_ship, y_ship = (background_cord.midbottom[0], (background_cord.bottom - spaceship.get_height()))
x_ship, y_ship = spaceship_rect[0], spaceship_rect[1]
#print(ship_init)
#print(spaceship_rect)

#2.1 DEFINE COLOR RGB (Red Green Blue)
WHITE = (255,255,255)
BLUE_LIGTH = (185, 240, 240)
RED = (255, 0, 0)
GREEN = (0,255,0)
MARRON = (145, 35, 30)
BLUE = (0,0,255)
YELLOW = (255, 255,0)
BLACK = (0, 0, 0)


#2.2 DEFINE SPEED & CLOCK (FPS)
pix_speed = 10

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


        #==> CAPTURE DYNAMIC MOVEMENT
            if event.key == K_LEFT:
                x_ship -= pix_speed

            if event.key == K_RIGHT:
                x_ship += pix_speed

            if event.key == K_UP:
                y_ship -= pix_speed

            if event.key == K_DOWN:
                y_ship += pix_speed

        #=> Define Obj1 or SHIP BoardLimit
            if x_ship <= 0:
                x_ship = 0

            elif x_ship >= (background.get_width() - spaceship.get_width()):
                x_ship = (background.get_width() - spaceship.get_width())


            if y_ship >= (background_cord.bottom - spaceship.get_height()):
                y_ship = (background_cord.bottom - spaceship.get_height())

            elif y_ship <= 0:
                  y_ship = 0





    #==> UPDATE OBJECT (Movement, Collision, outofBoard, Score,...)


    # ====> DISPLAY THE SURFACE | WHILE you have a BaKGround Using BLIT Method
    #screen_surface.fill(BLUE_LIGTH)
    screen_surface.blit(background, (0, 0))
    screen_surface.blit(spaceship, (x_ship, y_ship))


    #===> DRAW ON SURFACE (can be Built-ins or Image)
    #pygame.draw.line(screen_surface, RED, (20, 40), (200,300), 5)
    #pygame.draw.rect(screen_surface, MARRON, pygame.Rect(200, 30, 200, 100), 3)




    #=====> UPDATE THE SURFACE
    pygame.display.update()











