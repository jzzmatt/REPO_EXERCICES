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



