## The pype logic ##
from setting import *

class Pype:
    def __init__(self):
        # Pypes
        self.bottomPipes = []
        self.topPipes = []

    def initPypes(self): # inits the  first pypes on the game starting
        H = random.randint(PYPE_GAP,HEIGHT)
        self.topPipes.append({
            'x' : PYPE_X,
            'y' : 0,
            'height' : H
        })
        self.bottomPipes.append({
            'x' : PYPE_X,
            'y' : self.topPipes[0]['height'] + PYPE_GAP,
            'height' :  HEIGHT - self.topPipes[0]['height'] + PYPE_GAP
        })

    def get_pypes(self,window):
        # Add initial objects
        if len(self.topPipes) == 0 and len(self.bottomPipes) == 0:
            self.initPypes()

        # for amount of pypes in top pypes - which is the same in the bottom pypes list
        # this should let the pair of pypes be drawn at the same time and not the all the top/bottom pypes first or second
        for num in range(len(self.topPipes)):
            top = self.topPipes[num] # top part of pype pair
            bottom = self.bottomPipes[num] # bottom part of pype pair

            if top['x'] == WIDTH - PYPE_W*4: # Adding a new pype obj to list of pype parts when the leading pype reaches point 'x'
                H = random.randint(PYPE_GAP,HEIGHT)
                self.topPipes.append({
                    'x' : PYPE_X,
                    'y' : 0,
                    'height' : H
                })
            if bottom['x'] == WIDTH - PYPE_W*4: # Adding a new pype obj to list of pype parts when the leading pype reaches point 'x'
                self.bottomPipes.append({
                    'x' : PYPE_X,
                    'y' : self.topPipes[num]['height'] + PYPE_GAP,
                    'height' : HEIGHT - self.topPipes[num]['height'] + PYPE_GAP
                })

            print(f'{num} TOP : \n > "Height" { top["height"] }\n > "y" { top["y"] }')
            print(f'{num} Bottom : \n > "Height" { bottom["height"] }\n > "y" { bottom["y"] }')

            # Update pype velocity
            top['x'] -= PYPE_VEL
            bottom['x'] -= PYPE_VEL

            # Drawing pypes
            self.draw_pypes_pairs(window,top,bottom)

    def draw_pypes_pairs(self,window,top,bottom):
        pygame.draw.rect(window, GREEN, (top['x'], top['y'] , PYPE_W , top['height']))
        pygame.draw.rect(window, GREEN, (bottom['x'], bottom['y'] , PYPE_W , bottom['height']))