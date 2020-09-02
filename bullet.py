import pygame


class Bullet:
    def __init__(self, x: int, y: int, size: int, speed: int) -> None:
        self.x = x
        self.y = y

        self.speed = speed
        self.size = size

        self.out = False

    def event(self, event: pygame.event.EventType) -> None:
        pass

    def update(self) -> None:
        self.y -= self.speed

        if self.y < -self.size:
            self.out = True

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.size // 2, self.y - self.size, self.size, 2 * self.size))
