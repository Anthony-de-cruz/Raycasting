import math

from settings import SETTINGS
from objects import game_object
import pygame


class Player(game_object.GameObject):
    def __init__(
        self, image: pygame.Surface, x_pos: int, y_pos: int, *group: pygame.sprite.Group
    ):

        super().__init__(x_pos, y_pos, *group, image=image)

        # Save original image to preserve quality after transformations
        self.original_image = image
        self.original_rect = self.rect

        self.movement_speed = SETTINGS.movement_speed
        self.angle = 0
        self.rotation_speed = SETTINGS.movement_angle

        # A floating point version of rect components are needed to maintain movement
        # precision. This is due to rects only working with integers
        self.float_rect_x = float(self.rect.x)
        self.float_rect_y = float(self.rect.y)

    def move(self, forward, sideways) -> None:

        """Calculate and apply movement."""

        # Calculate the x and y components of the movement, multiply by movement speed
        # multiplier and directional modifer
        if forward != 0:
            self.float_rect_x -= (
                math.sin(math.radians(self.angle)) * self.movement_speed * forward
            )
            self.float_rect_y -= (
                math.cos(math.radians(self.angle)) * self.movement_speed * forward
            )
        if sideways != 0:
            self.float_rect_x += (
                math.cos(math.radians(self.angle)) * self.movement_speed * sideways
            )
            self.float_rect_y -= (
                math.sin(math.radians(self.angle)) * self.movement_speed * sideways
            )
        
        self.rect.x = int(self.float_rect_x)
        self.rect.y = int(self.float_rect_y)

    def rotate(self, direction) -> None:

        """Calculate and apply changes in angle."""

        # Change angle depending on the direction and speed multiplier
        self.angle += direction * self.rotation_speed

        # Ensure that angle doesn't go above 360 to keep angles sane
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < -360:
            self.angle += 360

        # Create a new image by rotating the original image by new angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        # Create a new rect based on the center of the old rect
        self.rect = self.image.get_rect(center=self.rect.center)
        # Update the floating rect
        self.float_rect_x, self.float_rect_y  = float(self.rect.x), float(self.rect.y)
