import pygame


class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 424
        self.screen_height = 720
        self.bg = pygame.image.load('images/bg.png')

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3
