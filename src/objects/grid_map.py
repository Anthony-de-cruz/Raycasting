from constants import COLOURS
from objects import game_object
import pygame


class GridMap(game_object.GameObject):
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
        image = pygame.Surface((self.tile_height * x_tiles, self.tile_height * y_tiles))

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

    def render(self):

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

    def update(self):

        self.render()
