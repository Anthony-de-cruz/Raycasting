from constants import COLOURS
from objects import game_object
import pygame


class GridMap(game_object.GameObject):

    """Game object to act as the 2D map that rays are cast in."""

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        x_tiles: int,
        y_tiles: int,
        *group: pygame.sprite.Group,
    ):

        self.tile_width = self.tile_height = int(
            (pygame.display.get_window_size()[0] / 2) / x_tiles
        )

        # Create the surface based on calculated dimentions
        image = pygame.Surface(
            (self.tile_height * x_tiles, self.tile_height * y_tiles)
        ).convert_alpha()

        super().__init__(x_pos, y_pos, *group, image=image)

        # Generate map data
        self.map_data = dict()
        self.map_data["Dimentions"] = (x_tiles, y_tiles)
        for x in range(x_tiles):
            for y in range(y_tiles):
                self.map_data[f"{x},{y}"] = 0

        # Generate map walls -temp-
        for x in range(self.map_data["Dimentions"][0]):
            for y in range(self.map_data["Dimentions"][1]):

                if x == 0:
                    self.map_data[f"{x},{y}"] = 1
                if x == self.map_data["Dimentions"][0] - 1:
                    self.map_data[f"{x},{y}"] = 1
                if y == 0:
                    self.map_data[f"{x},{y}"] = 1
                if y == self.map_data["Dimentions"][1] - 1:
                    self.map_data[f"{x},{y}"] = 1

    def render(self) -> None:

        """Method to render an image of the map."""

        self.image.fill((0, 0, 0, 0))

        # This method of drawing the tiles with collision, creating the mask and then
        # drawing the rest is wasteful as the number of iterations are doubled
        # todo Need to replace this with a more efficient solution in the future
        # Draw tiles that have collision
        for x in range(self.map_data["Dimentions"][0]):
            for y in range(self.map_data["Dimentions"][1]):

                if self.map_data[f"{x},{y}"] == 1:
                    pygame.draw.rect(
                        self.image,
                        COLOURS["White"],
                        pygame.rect.Rect(
                            x * self.tile_width,
                            y * self.tile_height,
                            self.tile_width,
                            self.tile_height,
                        ),
                    )

        # Create a mask with just the tiles that have collision
        self.mask = pygame.mask.from_surface(self.image)

        # Draw tiles that don't have collision
        for x in range(self.map_data["Dimentions"][0]):
            for y in range(self.map_data["Dimentions"][1]):

                if self.map_data[f"{x},{y}"] == 0:
                    pygame.draw.rect(
                        self.image,
                        (25, 25, 0),
                        pygame.rect.Rect(
                            x * self.tile_width,
                            y * self.tile_height,
                            self.tile_width,
                            self.tile_height,
                        ),
                    )

    def update(self) -> None:

        """Method to run every frame and update map behaviour."""

        self.render()
