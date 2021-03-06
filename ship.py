import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('ship2.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.center2 -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.center2 += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.centery = self.center2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
