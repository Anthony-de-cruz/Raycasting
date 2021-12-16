import os
import sys

from settings import SETTINGS
import pygame


class Game:

    """Main game class"""

    def __init__(self):

        ## Setup window
        self.window_width =  SETTINGS.window_width
        self.window_height = SETTINGS.window_height
        self.window_name = SETTINGS.window_name

        self.window = self.setup_window()

        self.clock = pygame.time.Clock()

    def setup_window(self) -> pygame.surface:

        window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption((self.window_name))
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        return window

    def handle_events(self) -> None:

        self.event_list = pygame.event.get()

        for event in self.event_list:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def main_loop(self) -> None:

        self.running = True

        while self.running:

            self.handle_events()
