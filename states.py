import pygame

from player import Player
from enemy import Enemy
from widgets import Button

from pygame.locals import K_p, KEYDOWN


class GameStateManager:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.play = PlayState(self.width, self.height, self)
        self.pause = PauseState(self.width, self.height, self)
        self.game_over = GameOverState(self.width, self.height, self)
        self.menu = MenuState(self.width, self.height, self)

        self.active = self.menu

        self.close = False


class PlayState:
    def __init__(self, w: int, h: int, gsm: GameStateManager) -> None:
        self.width = w
        self.height = h

        self.gsm = gsm

        self.font = pygame.font.SysFont('Source Code Pro', 24)

        self.player = Player(self.width // 2, self.height * 0.8, self.width)
        self.enemy = Enemy(self.width, self.height)
        
    def event(self, event: pygame.event.EventType) -> None:
        if event.type == KEYDOWN:
            if event.key == K_p:
                self.pause()

        self.player.event(event)
        self.enemy.event(event)

    def update(self) -> None:
        if self.enemy.is_hit(self.player.bullets):
            self.player.score += 10

        for invader in self.enemy.invaders:
            if self.player.is_hit(invader.bullets):
                if self.player.lives == 0:
                    self.game_over()

                break

        self.player.update()
        self.enemy.update()

    def render(self, screen: pygame.Surface) -> None:
        self.player.render(screen)
        self.enemy.render(screen)

        textsurface = self.font.render(f'Score: {self.player.score}, Lives: {self.player.lives}', False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))

    def pause(self) -> None:
        self.gsm.active = self.gsm.pause

    def game_over(self) -> None:
        self.gsm.active = self.gsm.game_over


class PauseState:
    def __init__(self, w: int, h: int, gsm: GameStateManager) -> None:
        self.width = w
        self.height = h

        self.gsm = gsm

        self.font = pygame.font.SysFont('Source Code Pro', 50)

        self.widgets = [
            Button(self.width // 2, self.height // 2, 250, 75, 'Resume', self.resume),
            Button(self.width // 2, self.height // 2 + 100, 250, 75, 'Menu', self.menu)
        ]

    def event(self, event: pygame.event.EventType) -> None:
        for widget in self.widgets:
            widget.event(event)

    def update(self) -> None:
        for widget in self.widgets:
            widget.update()

    def render(self, screen: pygame.Surface) -> None:
        for widget in self.widgets:
            widget.render(screen)

        textsurface = self.font.render('Pause', False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(self.width // 2, self.height // 3))
        screen.blit(textsurface, text_rect)

    def resume(self) -> None:
        self.gsm.active = self.gsm.play

    def menu(self) -> None:
        self.gsm.active = self.gsm.menu


class MenuState:
    def __init__(self, w, h, gsm):
        self.width = w
        self.height = h

        self.gsm = gsm

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
        self.gsm.play = PlayState(self.width, self.height, self.gsm)
        self.gsm.active = self.gsm.play

    def close(self):
        self.gsm.close = True


class GameOverState:
    def __init__(self, w, h, gsm):
        self.width = w
        self.height = h

        self.gsm = gsm

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
        self.gsm.active = self.gsm.menu
