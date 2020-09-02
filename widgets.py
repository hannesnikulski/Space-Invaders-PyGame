import pygame

from pygame.locals import MOUSEBUTTONUP
from typing import Callable, Tuple


class Button:
    def __init__(self, x: int, y: int, w: int, h: int, text: str, func: Callable) -> None:
        self.x = x
        self.y = y
        self.height = h
        self.width = w

        self.text = text
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.func = func

    def event(self, event: pygame.event.EventType) -> None:
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and self.is_in(pygame.mouse.get_pos()):
                self.click()

    def update(self) -> None:
        if self.is_in(pygame.mouse.get_pos()):
            self.text_color = (255, 0, 0)

        elif self.text_color == (255, 0, 0):
            self.text_color = (255, 255, 255)

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height), 2)

        textsurface = self.font.render(self.text, False, self.text_color)
        text_rect = textsurface.get_rect(center=(self.x, self.y))
        screen.blit(textsurface, text_rect)

    def is_in(self, pos: Tuple[int, int]) -> bool:
        x, y = pos
        return self.x < x + self.width // 2 < self.x + self.width and self.y < y + self.height // 2 < self.y + self.height

    def click(self) -> None:
        self.func()


class Text:
    def __init__(self, x, y, text, color):
        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.surface = self.font.render(text, False, color)
        self.rect = self.surface.get_rect(center=(x, y))

    def event(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.surface, self.rect)
