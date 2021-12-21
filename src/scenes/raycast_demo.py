import os

from settings import SETTINGS
from constants import COLOURS
from objects import player
import pygame


class Object:
    pass


class RaycastDemo(pygame.sprite.Sprite):
    def __init__(self, *group):

        super().__init__(*group)

        ## Create surface
        # Values may be drawn from settings in future
        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        ## Create sprite groups
        self.group = Object()
        self.group.player = pygame.sprite.Group()
        self.group.map = pygame.sprite.Group()

        ## Load assets
        # Temporary surface, will load an actual sprite asset in the future
        player_img = pygame.image.load(os.path.join("assets", "Arrow.png"))

        ## Create objects
        # Player
        self.player = player.Player(player_img, 475, 200, self.group.player)
        print(self.player.rect)

    def update(self, event_list) -> None:

        """Method to run every frame and update scene behaviour."""

        keys = pygame.key.get_pressed()

        if True in keys:

            if (
                keys[pygame.K_w]
                or keys[pygame.K_a]
                or keys[pygame.K_s]
                or keys[pygame.K_d]
            ):
                self.group.player.sprites()[0].move(
                    (keys[pygame.K_w] - keys[pygame.K_s]),
                    (keys[pygame.K_d] - keys[pygame.K_a]),
                )

            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.group.player.sprites()[0].rotate(
                    (keys[pygame.K_LEFT] - keys[pygame.K_RIGHT])
                )

        # for event in event_list:

        #    pass

    def render(self) -> pygame.Surface:

        """Creates and returns a surface of the scene to be drawn.

        Returns:
            pygame.surface: A surface of the scene frame.
        """

        # Background
        self.image.fill(COLOURS["Dark Grey"])

        # Draw sprite group
        self.group.player.draw(self.image)

        return self.image
