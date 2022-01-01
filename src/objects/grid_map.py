import os

from constants import COLOURS
from objects.game_object import GameObject
import pygame


class Tile(GameObject):

    """Tile"""

    def __init__(
        self, tile: tuple, x_pos: int, y_pos: int, *group: pygame.sprite.Group
    ):

        super().__init__(x_pos, y_pos, *group, image=tile[0])

        self.collision = tile[1]
        if self.collision:
            self.mask = pygame.mask.from_surface(self.image)


class GridMap(GameObject):

    """Game object to act as the 2D map that rays are cast in."""

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        x_tiles: int,
        y_tiles: int,
        *group: pygame.sprite.Group,
    ):

        ## Create surface
        # Create the surface based on calculated dimentions
        self.tile_width = self.tile_height = int(
            (pygame.display.get_window_size()[0] / 2) / x_tiles
        )
        image = pygame.Surface(
            (self.tile_height * x_tiles, self.tile_height * y_tiles)
        ).convert_alpha()

        super().__init__(x_pos, y_pos, *group, image=image)

        ## Create tile set
        # Create tile group
        self.tiles_group = pygame.sprite.Group()
        self.tiles_collision_group = pygame.sprite.Group()
        # Create tile set (image, collision)
        self.TILE_SET = {
            "Wall": (
                pygame.image.load(os.path.join("assets", "Wall.png")).convert(),
                True,
            ),
            "Floor": (
                pygame.image.load(os.path.join("assets", "Floor.png")).convert(),
                False,
            ),
        }

        ## Generate map data
        # In future this should be read from a file
        self.map_data = dict()
        self.map_data["Dimentions"] = (x_tiles, y_tiles)
        for x in range(x_tiles):
            for y in range(y_tiles):
                self.map_data[f"{x},{y}"] = Tile(
                    self.TILE_SET["Floor"],
                    x * self.tile_width + self.rect.x,
                    y * self.tile_height + self.rect.y,
                    self.tiles_group,
                )

        # Generate map walls -temp-
        for x in range(self.map_data["Dimentions"][0]):
            for y in range(self.map_data["Dimentions"][1]):

                if x == 0:
                    self.map_data[f"{x},{y}"] = Tile(
                        self.TILE_SET["Wall"],
                        x * self.tile_width + self.rect.x,
                        y * self.tile_height + self.rect.y,
                        self.tiles_group,
                        self.tiles_collision_group,
                    )
                if x == self.map_data["Dimentions"][0] - 1:
                    self.map_data[f"{x},{y}"] = Tile(
                        self.TILE_SET["Wall"],
                        x * self.tile_width + self.rect.x,
                        y * self.tile_height + self.rect.y,
                        self.tiles_group,
                        self.tiles_collision_group,
                    )
                if y == 0:
                    self.map_data[f"{x},{y}"] = Tile(
                        self.TILE_SET["Wall"],
                        x * self.tile_width + self.rect.x,
                        y * self.tile_height + self.rect.y,
                        self.tiles_group,
                        self.tiles_collision_group,
                    )
                if y == self.map_data["Dimentions"][1] - 1:
                    self.map_data[f"{x},{y}"] = Tile(
                        self.TILE_SET["Wall"],
                        x * self.tile_width + self.rect.x,
                        y * self.tile_height + self.rect.y,
                        self.tiles_group,
                        self.tiles_collision_group,
                    )
                if y == 5 and x == 5:
                    self.map_data[f"{x},{y}"] = Tile(
                        self.TILE_SET["Wall"],
                        x * self.tile_width + self.rect.x,
                        y * self.tile_height + self.rect.y,
                        self.tiles_group,
                        self.tiles_collision_group,
                    )

        self.render()

    def render(self) -> None:

        """Method to render an image of the map.
        Should only be called when changes are made for performance"""

        self.image.fill((0, 0, 0, 0))

        self.tiles_group.draw(self.image)

    def update(self) -> None:

        """Method to run every frame and update map behaviour."""

        self.tiles_group.update()
        self.render()
