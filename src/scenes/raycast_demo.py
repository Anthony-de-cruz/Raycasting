import os

from settings import SETTINGS
from constants import COLOURS
from objects import player, grid_map
import pygame


class Object:
    pass


class RaycastDemo(pygame.sprite.Sprite):
    def __init__(self, *group: pygame.sprite.Group):

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
        # Player sprite
        player_img = pygame.image.load(os.path.join("assets", "Arrow.png"))

        ## Create objects
        # Map
        self.map = grid_map.GridMap(0, 0, 10, 10, self.group.map)
        # Player
        self.player = player.Player(player_img, 475, 200, self.group.player)

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

    def render(self) -> pygame.Surface:

        """Creates and returns a surface of the scene to be drawn.

        Returns:
            pygame.surface: A surface of the scene frame.
        """

        # Update objects
        self.group.map.update()

        # Background
        self.image.fill(COLOURS["Dark Grey"])

        # Draw sprite group
        self.group.map.draw(self.image)
        self.group.player.draw(self.image)

        return self.image
