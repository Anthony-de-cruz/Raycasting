import pygame

class Button(pygame.sprite.Sprite):

    """A button object
    """

    def __init__(self, image, x_pos, y_pos, *groups):

        super().__init__(*groups)

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = image
        self.rect = pygame.Rect(x_pos, y_pos, image.get_width(), image.get_height())
    
    def function(self):

        """A method to represent the function of a button when pressed.
        """

        pass


