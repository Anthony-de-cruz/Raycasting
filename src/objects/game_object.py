import pygame


class GameObject(pygame.sprite.Sprite):

    """A base game object class that all other game objects will inherit from."""

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        *groups: pygame.sprite.Group,
        width: int = 1,
        height: int = 1
    ):

        super().__init__(*groups)

        ## Position
        self.x_pos = x_pos
        self.y_pos = y_pos

        ## Dimentions
        self.width = width
        self.height = height

        ## Surface and rect
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(
            x_pos, y_pos, self.image.get_width(), self.image.get_height()
        )
