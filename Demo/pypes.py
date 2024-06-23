## The pype logic ##
from setting import *

class Pype:
    def __init__(self):
        # Pypes
        self.pypes = []

    def get_pypes(self,window):
        if len(self.pypes) == 0:
            self.init_pypes()

        for pype in self.pypes:
            if pype['x'] == PYPE_SPAWN:
                gap_start_Y = random.randint(0,HEIGHT-PYPE_GAP)
                self.pypes.append({
                    'x' : PYPE_X,
                    'gap' : gap_start_Y
                })
            pype['x'] -= PYPE_VEL
            self.draw_pypes_pairs(window,pype)

    def init_pypes(self):
        gap_start_Y = random.randint(0,HEIGHT-PYPE_GAP)
        self.pypes.append({
            'x' : PYPE_X,
            'gap' : gap_start_Y
        })






    def draw_pypes_pairs(self,window,pype):
        pygame.draw.rect(window,GREEN,(pype['x'], 0, PYPE_W, HEIGHT)) # drawing pype
        pygame.draw.rect(window,RED, (pype['x'], pype['gap'], PYPE_W, PYPE_GAP)) # drawing gap
        # pygame.draw.rect(window, GREEN, (top['x'], top['y'] , PYPE_W , HEIGHT))
        # pygame.draw.rect(window, GREEN, (bottom['x'], bottom['y'] , PYPE_W , HEIGHT))