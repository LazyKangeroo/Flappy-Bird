from setting import *

class Main:
    def __init__(self):
        # general
        pygame.init()

        # create clock obj
        self.clock = pygame.time.Clock()

        # screen
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Flappy-Bird')

        # font intit
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        # Game start Font surface
        self.startText_surface = self.font.render("Press 'SHIFT' to Start...",True,DARK_ORANGE)
        self.text_rect = self.startText_surface.get_rect(center=(WIDTH/2,HEIGHT/2))

        # Player Death Font surface
        self.endText_surface = self.font.render("YOU DIED",True,RED)

        # counter surface
        self.counter_surface = pygame.Surface((COUNTER_W,COUNTER_H))
        self.counter_rect = self.counter_surface.get_rect(topright=(WIDTH - PADDING * 2,PADDING * 2))

    def run(self):
        gameStart = False
        death = False

        pl_vel_y = 0
        y = PL_Y
        while True:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # stores keys pressed
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    print('--- Game Start ---')
                    gameStart = True
                    death = False

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

            ## display ##
            self.window.fill(LIGHT_BLUE)
            self.counter_surface.fill(WHITE)

            # self.window.blit(self.counter_surface,self.counter_rect)
            pygame.draw.rect(self.window, YELLOW, (PL_X, y, PLAYER_W,PLAYER_W))

            if not gameStart and not death:
                self.window.blit(self.startText_surface,self.text_rect)
            elif not gameStart and death:
                self.window.blit(self.endText_surface,self.text_rect)
                pygame.draw.rect(self.window, ORANGE_RED, (PL_X, y, PLAYER_W,PLAYER_W))

            # Update the display
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()