from settings import SETTINGS, COLOURS
from objects import button
import pygame

class Object: pass

class MainMenu(pygame.sprite.Sprite):

    """Main Menu scene; allows user to choose what to do."""

    def __init__(self, *groups):

        super().__init__(*groups)

        ## Create surface
        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        ## Create sprite groups
        self.groups = Object()
        self.groups.text = pygame.sprite.Group()
        self.groups.buttons = pygame.sprite.Group()

        ## Load assets
        # Temporary surface, will load an actual sprite asset in the future
        start_btn_img = pygame.Surface((100, 50))
        start_btn_img.fill(COLOURS["White"])
        text = pygame.font.SysFont(None, 52).render("Start", True, COLOURS["Black"])
        start_btn_img.blit(text,
            (start_btn_img.get_width() // 2 - text.get_width() // 2, 
            start_btn_img.get_height() // 2 - text.get_height() // 2))

        ## Create objects
        # Start button
        self.start_button = button.Button(start_btn_img,
            self.width // 2 - start_btn_img.get_width() // 2, 300,
            self.groups.buttons)

        # Title text
        # Temporary sprite, will be made from a base Game Object class in future
        self.title_text = pygame.sprite.Sprite(self.groups.text)
        self.title_text.image = pygame.font.SysFont(None, 150).render(
            "Raycasting Demo", True, COLOURS["White"])
        self.title_text.rect = pygame.Rect(
            self.width // 2 - self.title_text.image.get_width() // 2,
            100,
            self.title_text.image.get_width(),
            self.title_text.image.get_height()
        )

    def update(self):
        pass

    def render(self) -> pygame.surface:

        """Creates and returns a surface of the scene to be drawn.

        Returns:
            pygame.surface: A surface of the scene frame.
        """

        self.groups.text.draw(self.image)
        self.groups.buttons.draw(self.image)
        
        return self.image
