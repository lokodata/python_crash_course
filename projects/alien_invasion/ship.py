import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, a1_game):
        """Initialize the ship and set its starting position."""
        self.screen = a1_game.screen
        self.settings = a1_game.settings
        self.screen_rect = a1_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

        # # Load a character
        # self.character = pygame.image.load('images/star.png')
        # self.character = pygame.transform.scale(self.character, (50, 50))
        # self.character_rect = self.character.get_rect()

        # # Start each new character at the center of the screen.
        # self.character_rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # """Draw the character at its current location."""
        # self.screen.blit(self.character, self.character_rect)
