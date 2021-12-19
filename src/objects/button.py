from types import FunctionType

from game_object import GameObject
import pygame


class Button(GameObject):

    """A button object"""

    def __init__(
        self,
        image: pygame.Surface,
        x_pos: int,
        y_pos: int,
        *group: pygame.sprite.Group,
        function: FunctionType = None
    ):

        super().__init__(
            x_pos, y_pos, *group, image=image
        )

        if function is not None:
            self.function = function

    def function(self) -> None:

        """A method to represent the function of a button when pressed."""

        print("Function unassigned")
