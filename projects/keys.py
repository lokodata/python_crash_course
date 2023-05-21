import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = 424
        self.screen_height = 720

        # Set up the screen
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Key Press Example")

        # Set up the font
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)

        self.key_text = None

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.key_text = self.font.render(
                    str(event.key), True, (255, 255, 255))

    def _update_screen(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Blit the key text onto the screen
        if self.key_text:
            self.screen.blit(self.key_text, (10, 10))

        # Update the display
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
