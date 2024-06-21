# Importing dependancies
import pygame
import sys
import math

# Window
HEIGHT, WIDTH = 500, 800
PADDING = 20

# Counter
COUNTER_W,COUNTER_H = 100, 85

# Bird w/h (120,100)px
PLAYER_W , PLAYER_H = 50, 50
PL_X,PL_Y = PADDING * 4, HEIGHT / 2


GRAVITY = 1
FLAP_FORCE = -10

# Colour
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255,215,0)
GREEN = (0,255,127)
ORANGE_RED = (255,69,0)
DARK_ORANGE = (255,140,0)
LIGHT_BLUE = (0,255,255)