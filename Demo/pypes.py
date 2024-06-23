## The pype logic ##
from setting import *

class Pype:
    def __init__(self):
        # Pypes
        self.pypes = []

        # Collition
        self.died = False

        # points
        self.pointCounter = 0

    def get_pypes(self,window,pl_y):
        if len(self.pypes) == 0:
            self.init_pypes()

        for pype in self.pypes:
            if pype['x'] == PYPE_SPAWN:
                gap_start_Y = random.randrange(0,HEIGHT-PYPE_GAP,PYPE_GAP)
                self.pypes.append({
                    'x' : PYPE_X,
                    'gap' : gap_start_Y
                })

            pype['x'] -= PYPE_VEL
            self.draw_pypes_pairs(window,pype)

            #----- Collition  -----#
            if PL_X == pype['x']:
               self.died = self.collition(pype,pl_y)

        return self.died

    def init_pypes(self):
        gap_start_Y = random.randrange(0,HEIGHT-PYPE_GAP,PYPE_GAP)
        self.pypes.append({
            'x' : PYPE_X,
            'gap' : gap_start_Y
        })

    def draw_pypes_pairs(self,window,pype):
        pygame.draw.rect(window,GREEN,(pype['x'], 0, PYPE_W, HEIGHT)) # drawing pype
        pygame.draw.rect(window,LIGHT_BLUE, (pype['x'], pype['gap'], PYPE_W, PYPE_GAP)) # drawing gap

    def collition(self,pype,pl_y):
        gap_rect = pygame.Rect(pype['x'],pype['gap'],PYPE_W, PYPE_GAP)
        pl_rect = pygame.Rect(PL_X, pl_y, PLAYER_W, PLAYER_H)

        if gap_rect.colliderect(pl_rect):
            self.pointCounter += 1
            print(f'Points : {self.pointCounter}')
            return False
        elif not gap_rect.colliderect(pl_rect):
            return True