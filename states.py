import pygame

from player import Player
from enemy import Enemy
from widgets import Button

from pygame.locals import K_p, KEYDOWN


class PlayState:
    def __init__(self, w, h, parent):
        self.width = w
        self.height = h

        self.parent = parent

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.player = Player(self.width // 2, self.height * 0.8, self.width)
        self.enemy = Enemy(self.width, self.height)
        
    def event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_p:
                self.pause()

        self.player.event(event)
        self.enemy.event(event)

    def update(self):
        if self.enemy.is_hit(self.player.bullets):
            self.player.score += 10

        for invader in self.enemy.invaders:
            if self.player.is_hit(invader.bullets):
                if self.player.lives == 0:
                    self.game_over()

                break

        self.player.update()
        self.enemy.update()

    def render(self, screen):
        self.player.render(screen)
        self.enemy.render(screen)

        textsurface = self.font.render(f'Score: {self.player.score}, Lives: {self.player.lives}', False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))

    def pause(self):
        self.parent.active_state = self.parent.pause_state

    def game_over(self):
        self.parent.active_state = self.parent.game_over_state

class PauseState:
    def __init__(self, w, h, parent):
        self.width = w
        self.height = h

        self.parent = parent

        self.font = pygame.font.SysFont('Source Code Pro', 50)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Resume', self.resume),
            Button(self.width // 2, self.height // 2 + 100, 250, 75, 'Menu', self.menu)
        ]

    def event(self, event):
        for widget in self.widgets:
            widget.event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def render(self, screen):
        for widget in self.widgets:
            widget.render(screen)

        textsurface = self.font.render('Pause', False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(self.width // 2, self.height // 3))
        screen.blit(textsurface, text_rect)

    def resume(self):
        self.parent.active_state = self.parent.play_state

    def menu(self):
        self.parent.active_state = self.parent.menu_state


class MenuState:
    def __init__(self, w, h, parent):
        self.width = w
        self.height = h

        self.parent = parent

        self.font = pygame.font.SysFont('Source Code Pro', 50)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Play', self.play),
            Button(self.width // 2, self.height // 2 + 100, 250, 75, 'Quit', self.close)
        ]

    def event(self, event):
        for widget in self.widgets:
            widget.event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def render(self, screen):
        for widget in self.widgets:
            widget.render(screen)

        textsurface = self.font.render('Space Invaders', False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(self.width // 2, self.height // 3))
        screen.blit(textsurface, text_rect)

    def play(self):
        self.parent.play_state = PlayState(self.width, self.height, self.parent)
        self.parent.active_state = self.parent.play_state

    def close(self):
        self.parent.close()


class GameOverState:
    def __init__(self, w, h, parent):
        self.width = w
        self.height = h

        self.parent = parent

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Menu', self.menu)
        ]

    def event(self, event):
        for widget in self.widgets:
            widget.event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def render(self, screen):
        for widget in self.widgets:
            widget.render(screen)

        textsurface = self.font.render('Game Over', False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(self.width // 2, self.height // 3))
        screen.blit(textsurface, text_rect)
 
    def menu(self):
        self.parent.active_state = self.parent.menu_state