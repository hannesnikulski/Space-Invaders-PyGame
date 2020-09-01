import sys
import pygame

from pygame.locals import QUIT
from states import MenuState, PlayState, PauseState, GameOverState


class Game:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.menu_state = MenuState(self.width, self.height, self)
        self.play_state = PlayState(self.width, self.height, self)
        self.pause_state = PauseState(self.width, self.height, self)
        self.game_over_state = GameOverState(self.width, self.height, self)

        self.active_state = self.menu_state

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.BACKGROUND = (0, 0, 0)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.close()

            self.active_state.event(event)

    def update(self):
        self.active_state.update()

    def render(self, screen):
        self.active_state.render(screen)

    def run(self):
        while True:
            self.screen.fill(self.BACKGROUND)

            self.event()

            self.update()
            
            self.render(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    
    game = Game(1280, 720)
    game.run()
