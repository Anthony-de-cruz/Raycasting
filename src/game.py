import os
import sys

from settings import SETTINGS
from scenes import main_menu
import pygame


class Object:
    pass


class Game:

    """Main game class"""

    def __init__(self):

        ## Setup window
        self.window_width = SETTINGS.window_width
        self.window_height = SETTINGS.window_height
        self.window_name = SETTINGS.window_name

        self.window = self.setup_window()

        ## Clock
        self.clock = pygame.time.Clock()
        self.FPS = SETTINGS.fps

        ## Scenes
        self.scenes = Object()
        self.scenes.focus = pygame.sprite.GroupSingle()
        self.scenes.main_menu = main_menu.MainMenu()

        ## Initial state
        self.scenes.focus.add(self.scenes.main_menu)
        self.running = True

    def setup_window(self) -> pygame.surface:

        window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption((self.window_name))
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        return window

    def handle_events(self) -> None:

        self.event_list = pygame.event.get()

        for event in self.event_list:

            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()

    def main_loop(self) -> None:

        while self.running:

            self.clock.tick(self.FPS)
            self.handle_events()

            self.scenes.focus.update(self.event_list)

            # Should try to find a nicer way to refer to the focused sprite
            focused_sprite = self.scenes.focus.sprites()[0]
            render = focused_sprite.render()
            self.window.blit(render, (0, 0), focused_sprite.rect)

            pygame.display.flip()
