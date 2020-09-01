import pygame

from pygame.locals import MOUSEBUTTONUP


class Button:
    def __init__(self, x, y, w, h, text, func):
        self.x = x
        self.y = y
        self.height = h
        self.width = w

        self.text = text
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.func = func

    def event(self, event):
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and self.is_in(pygame.mouse.get_pos()):
                self.click()

    def update(self):
        if self.is_in(pygame.mouse.get_pos()):
            self.text_color = (255, 0, 0)

        elif self.text_color == (255, 0, 0):
            self.text_color = (255, 255, 255)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height), 2)

        textsurface = self.font.render(self.text, False, self.text_color)
        text_rect = textsurface.get_rect(center=(self.x, self.y))
        screen.blit(textsurface, text_rect)

    def is_in(self, pos):
        x, y = pos
        return self.x < x + self.width // 2 < self.x + self.width and self.y < y + self.height // 2 < self.y + self.height

    def click(self):
        self.func()