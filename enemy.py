import random
import pygame

from bullet import Bullet
from typing import List


class Enemy:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.speed = 1

        self.invaders = []
        self.add()

    def event(self, event: pygame.event.EventType) -> None:
        pass

    def update(self) -> None:
        for invader in self.invaders:
            invader.update(self.speed)
        
        for invader in self.invaders:
            if  0 >= invader.x - invader.size[0] // 2 or invader.x + invader.size[0] // 2 >= self.width:
                self.speed *= -1

                for invader in self.invaders:
                    invader.y += invader.size[1]

                break

        self.remove()

    def render(self, screen: pygame.Surface) -> None:
        for invader in self.invaders:
            invader.render(screen)

    def add(self) -> None:
        for i in range(1, 10):
            for j in range(1, 3):
                self.invaders.append(
                    Invader(i * self.width // 10, j * self.height // 10)
                )

    def remove(self) -> None:
        self.invaders = [invader for invader in self.invaders if not invader.out]

    def is_hit(self, bullets: List[int]) -> bool:
        for bullet in bullets:
            for invader in self.invaders:
                if invader.y < bullet.y - bullet.size + invader.size[1] // 2 < invader.y + invader.size[1] and \
                    (invader.x < bullet.x + (invader.size[0] - bullet.size) // 2 < invader.x + invader.size[0] or \
                        invader.x < bullet.x + (invader.size[0] + bullet.size) // 2 < invader.x + invader.size[0]):
                    
                    bullet.out = True
                    invader.out = True

                    return True

class Invader:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

        self.img = pygame.image.load('img/invader.png')
        self.size = self.img.get_rect().size

        self.out = False

        self.bulletsize = 10
        self.bullets = []

    def event(self, event: pygame.event.EventType) -> None:
        pass

    def update(self, speed: pygame.Surface) -> None:
        self.x += speed

        r = random.random()

        if r < 0.005:
            self.bullets.append(
                Bullet(self.x, self.y, self.bulletsize, -10)
            )

        for bullet in self.bullets:
            bullet.update()

        self.remove()

    def render(self, screen: pygame.Surface) -> None:
        for bullet in self.bullets:
            bullet.render(screen)

        screen.blit(self.img, (self.x - self.size[0] // 2, self.y - self.size[1] // 2))

    def remove(self) -> None:
        self.bullets = [bullet for bullet in self.bullets if not bullet.out]
