from settings import SETTINGS, COLOURS
import pygame


class Object():
    pass


class RaycastDemo(pygame.sprite.Sprite):

    def __init__(self, *group):

        super().__init__(*group)

        ## Create surface
        # Values may be drawn from settings in future
        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width() 
        self.height = self.image.get_height()

        ## Create sprite groups
        self.group = Object()
        self.group.player = pygame.sprite.Group()
        self.group.map = pygame.sprite.Group()

        ## Load assets


        ## Create objects


    def update(self, event_list) -> None:

        """Method to run every frame and update scene behaviour."""
        
        #//for event in event_list:
        #//    pass

        pass
    

    def render(self) -> pygame.Surface:
        
        """Creates and returns a surface of the scene to be drawn.

        Returns:
            pygame.surface: A surface of the scene frame.
        """

        # Background
        self.image.fill(COLOURS["Dark Grey"])

        # Draw sprite group
        

        return self.image

