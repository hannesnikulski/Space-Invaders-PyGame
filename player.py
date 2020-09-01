import pygame

from bullet import Bullet

from pygame.locals import QUIT, K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, KEYUP


class Player:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

        self.speed = 4
        self.score = 0
        self.lives = 3

        self.img = pygame.image.load('img/ship.png')
        self.size = self.img.get_rect().size

        self.left = False
        self.right = False
        self.space = False

        self.bulletsize = 10
        self.bullets = []

    def event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.left = True

            elif event.key == K_RIGHT:
                self.right = True

            elif event.key == K_SPACE:
                self.space = True

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                self.left = False

            elif event.key == K_RIGHT:
                self.right = False

    def update(self):
        if self.left and self.x > self.size[0] // 2:
            self.x -= self.speed
        
        elif self.right and self.x < self.width - self.size[0] // 2:
            self.x += self.speed
            
        if self.space:
            self.bullets.append(
                Bullet(self.x - self.bulletsize // 2, self.y - self.size[1] // 2, self.bulletsize, 2 * self.speed)
            )
            self.space = False

        for bullet in self.bullets:
            bullet.update()

        self.remove()

    def render(self, screen):
        screen.blit(self.img, (self.x - self.size[0] // 2, self.y - self.size[1] // 2))

        for bullet in self.bullets:
            bullet.render(screen)

    def remove(self):
        self.bullets = [bullet for bullet in self.bullets if not bullet.out]

    def is_hit(self, bullets):
        for bullet in bullets:
            
            if self.y < bullet.y + (bullet.size + self.size[0]) // 2 < self.y + self.size[0] and \
                (self.x < bullet.x + (bullet.size + self.size[0]) // 2 < self.x + self.size[0] or \
                     self.x < bullet.x + (self.size[0] - bullet.size) // 2 < self.x + self.size[0]):

                bullet.out = True
                self.lives -= 1

                return True
