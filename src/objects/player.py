import math

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

        self.movement_speed = 5
        self.angle = 0
        self.rotation_speed = 5

    def move(self, forward, sideways) -> None:

        """Calculate and apply movement."""

        # Calculate the x and y components of the movement, multiply by movement speed
        # multiplier and directional modifer
        if forward != 0:
            self.rect.x -= (
                math.sin(math.radians(self.angle)) * self.movement_speed * forward
            )
            self.rect.y -= (
                math.cos(math.radians(self.angle)) * self.movement_speed * forward
            )
        if sideways != 0:
            self.rect.x += (
                math.cos(math.radians(self.angle)) * self.movement_speed * sideways
            )
            self.rect.y -= (
                math.sin(math.radians(self.angle)) * self.movement_speed * sideways
            )

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
