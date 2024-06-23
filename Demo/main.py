from setting import *
from pypes import Pype

class Main:
    def __init__(self):
        # modules
        self.pype = Pype()

        # general
        pygame.init()

        # create clock obj
        self.clock = pygame.time.Clock()

        # screen
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Flappy-Bird')

        # font intit
        pygame.font.init()
        self.font = pygame.font.Font(None, 40)
        self.counter_font = pygame.font.Font(None, 30)

        # Game start Font surface
        self.startText_surface = self.font.render("Press 'SHIFT' to Start...",True,DARK_ORANGE)
        self.text_rect = self.startText_surface.get_rect(center=(WIDTH/2,HEIGHT/2))

        # point counter text surface
        self.counter_surface = self.counter_font.render(f'{self.pype.pointCounter}',True,BLACK)
        self.counter_rect = self.counter_surface.get_rect(topright=(WIDTH-PADDING,PADDING))

        # Player death Font surface
        self.endText_surface = self.font.render("YOU DIED",True,RED)

##--------------------------------------GAME LOOP--------------------------------------------------

    def run(self):
        gameStart = False
        death = False

        pl_vel_y = 0
        y = PL_Y

        while True:
            self.counter_surface = self.counter_font.render(f'{self.pype.pointCounter}',True,BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # stores keys pressed
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    print('--- Game Start ---')
                    gameStart = True

                if keys[pygame.K_SPACE] and gameStart:
                    pl_vel_y = FLAP_FORCE

            if gameStart:
                # Apply gravity
                pl_vel_y += GRAVITY
               # Update bird position
                y += pl_vel_y

                # Check for collisions with the ground
                if y + PLAYER_H > HEIGHT:
                    y = HEIGHT - PLAYER_H
                    pl_vel_y = 0
                    # ending game play
                    death = True
                    gameStart = False

                elif y < 0:
                    y = 1

            ## display ##
            self.window.fill(LIGHT_BLUE)

            if not gameStart and not death:
                self.window.blit(self.startText_surface,self.text_rect)
            elif not gameStart and death:
                self.window.blit(self.endText_surface,self.text_rect)
                pygame.draw.rect(self.window, ORANGE_RED, (PL_X, y, PLAYER_W,PLAYER_H))

            if gameStart: # drawing pipes
                collition = self.pype.get_pypes(self.window,y)
                if collition:
                    death = True
                    gameStart = False

            # Player (Bird rect)
            pygame.draw.rect(self.window, YELLOW, (PL_X, y, PLAYER_W,PLAYER_W))

            # Point Counter
            self.window.blit(self.counter_surface,self.counter_rect)

            # Update the display
            pygame.display.update()
            self.clock.tick(60)
            pygame.time.delay(50)

if __name__ == '__main__':
    main = Main()
    main.run()