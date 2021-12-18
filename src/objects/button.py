from types import FunctionType
import pygame

from objects.game_object import GameObject

class Button(GameObject):

    """A button object
    """

    def __init__(self, image: pygame.Surface, x_pos: int, y_pos: int, *groups: pygame.sprite.Group, function=None):

        super().__init__(x_pos, y_pos, *groups, width = image.get_width(), height = image.get_height())
        
        self.image = image

        if function is not None: self.function = function
    
    def function(self) -> None:

        """A method to represent the function of a button when pressed.
        """

        print("wooooo")

