import sys
import pygame

from pygame.locals import QUIT
from states import GameStateManager


class Game:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.gsm = GameStateManager(self.width, self.height)

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.BACKGROUND = (0, 0, 0)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.close()

            self.gsm.active.event(event)

    def update(self):
        if self.gsm.close:
            self.close()

        self.gsm.active.update()


    def render(self, screen):
        self.gsm.active.render(screen)

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
    pygame.display.set_caption("Space invaders")
    pygame.display.set_icon(pygame.image.load('img/icon.png'))

    game = Game(1280, 720)
    game.run()
