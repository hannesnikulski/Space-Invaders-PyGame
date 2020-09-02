import random
import sys
import pygame

from pygame.locals import QUIT
from states import GameStateManager


class Game:
    """
        Game class for Space Invaders
    """

    def __init__(self, w: int, h: int) -> None:
        self.width = w
        self.height = h

        self.gsm = GameStateManager(self.width, self.height)

        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.BACKGROUND = (0, 0, 0)

    def event(self) -> None:
        """
            Event
        """

        for event in pygame.event.get():
            if event.type == QUIT:
                self.close()

            self.gsm.active.event(event)

    def update(self) -> None:
        """
            Update
        """

        if self.gsm.close:
            self.close()

        self.gsm.active.update()

    def render(self) -> None:
        self.gsm.active.render(self.screen)

    def run(self) -> None:
        """
            Game loop
        """

        while True:
            self.screen.fill(self.BACKGROUND)

            self.event()

            self.update()
            
            self.render()

            pygame.display.flip()
            self.clock.tick(self.FPS)

    def close(self) -> None:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Space invaders")
    pygame.display.set_icon(pygame.image.load('img/icon.png'))

    game = Game(1280, 720)
    game.run()
