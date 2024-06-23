# Importing dependancies
import pygame
import sys
import math
import random
import random2

# Window
HEIGHT, WIDTH = 600, 900
PADDING = 20

# Counter
COUNTER_W,COUNTER_H = 100, 85

# Bird w/h (120,100)px
PLAYER_W , PLAYER_H = 30, 25
PL_X,PL_Y = WIDTH/10, HEIGHT / 2

GRAVITY = 1.8
FLAP_FORCE = -13

# pipes
PYPE_W =  60
PYPE_VEL = 10
PYPE_X = WIDTH-PADDING*2
PYPE_GAP = 120
PYPE_SPAWN = WIDTH - PYPE_W*5

# Colour
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255,215,0)
GREEN = (0,255,127)
ORANGE_RED = (255,69,0)
DARK_ORANGE = (255,140,0)
LIGHT_BLUE = (0,255,255)