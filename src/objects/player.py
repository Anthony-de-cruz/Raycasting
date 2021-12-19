from objects import game_object
import pygame

class Player(game_object.GameObject):

    def __init__(
        self, 
        image: pygame.Surface, 
        x_pos: int,
        y_pos: int,
        *group: pygame.sprite.Group):

        super().__init__(x_pos, y_pos, *group, image=image)