import pygame


class GameObject(pygame.sprite.Sprite):

    """A base game object class that all other game objects will inherit from.
    If the game object is to have no image, enter None and a blank 1x1 image
    will be generated.
    """

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        *group: pygame.sprite.Group,
        image: pygame.Surface = None
    ):

        super().__init__(*group)

        ## Position
        self.x_pos = x_pos
        self.y_pos = y_pos

        ## Dimentions
        # If an image is passed
        if image is not None:
            self.width = image.get_width()
            self.height = image.get_height()

            self.image = image

        # If an image is not passed
        else:
            self.width = 1
            self.height = 1

            self.image = pygame.Surface((self.width, self.height))

        # Create rect
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
