import pygame


class Bullet:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y

        self.speed = speed
        self.size = size

        self.out = False

    def event(self, event):
        pass

    def update(self):
        self.y -= self.speed

        if self.y < -self.size:
            self.out = True

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.size // 2, self.y - self.size, self.size, 2 * self.size))
