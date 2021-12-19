from game_object import GameObject
import pygame

class Player(GameObject):

    def __init__(
        self, 
        image: pygame.Surface, 
        x_pos: int,
        y_pos: int,
        *group: pygame.sprite.Group):

        super().__init__(x_pos, y_pos, *group, image=image)