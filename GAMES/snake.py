import pygame
import sys
import random
import time

check_errors = pygame.init()  # initialize the Class pygame
# as init() method will check the funcionality and return a tuple of eg (4, 0), 0 for mention no issue

if check_errors[1] > 0:
  print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
  sys.exit(-1) # return standard error exit

else:
  print("(+) Pygame successfully initialized!")



#Setup a  Surface or Board | x,y | row , columns | width, height
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game!')  #Define the Windows Title


#Setup a Colors in RGB format
#define red Color, by default color = 0
red = pygame.Color(255, 0, 0)  #=> gameover
green = pygame.Color(0, 255, 0) #=> Snake
black = pygame.Color(0, 0, 0)  #=> score
white = pygame.Color(255, 255, 255) #=> background
brown = pygame.Color(165, 42, 42)   #=> food



# FPS (Frame Per Second) controller
fpsController = pygame.time.Clock()

snakePos = [100, 50]    #Hold the Coordinate of the Snake, the x and y | the head
snakeBody = [[100, 50],
             [90, 50],
             [80, 50]
             ]    #Display the body of the snake a 2d list | list of list

#get the food location based an a random of x,y

foodPos = [random.randrange(1, 72)* 10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGTH'
changeto = direction


#Game Over fct
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    Gosurf = myFont.render('Game Over!', True, red)
    Gorect = Gosurf.get_rect()
    Gorect.midtop = (360, 15)
    playSurface.blit(Gosurf, Gorect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()  #pygame exit
    sys.exit()     #Console exit



gameOver()

