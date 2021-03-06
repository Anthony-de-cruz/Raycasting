from settings import SETTINGS
from constants import COLOURS, RAYCAST_DEMO
from objects import button
import pygame


class Object:
    pass


class MainMenu(pygame.sprite.Sprite):

    """Main Menu scene; allows user to choose what to do."""

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
        self.group.text = pygame.sprite.Group()
        self.group.buttons = pygame.sprite.Group()

        ## Load assets
        # Temporary surface, will load an actual sprite asset in the future
        start_btn_img = pygame.Surface((100, 50))
        start_btn_img.fill(COLOURS["White"])
        text = pygame.font.SysFont(None, 52).render("Start", True, COLOURS["Black"])
        start_btn_img.blit(
            text,
            (
                start_btn_img.get_width() // 2 - text.get_width() // 2,
                start_btn_img.get_height() // 2 - text.get_height() // 2,
            ),
        )

        ## Create objects
        # Start button
        def start_function():
            pygame.event.post(pygame.event.Event(RAYCAST_DEMO))

        self.start_button = button.Button(
            start_btn_img,
            self.width // 2 - start_btn_img.get_width() // 2,
            300,
            self.group.buttons,
            function=start_function,
        )

        # Title text
        # Temporary sprite, will be made from a base Game Object class in future
        self.title_text = pygame.sprite.Sprite(self.group.text)
        self.title_text.image = pygame.font.SysFont(None, 150).render(
            "Raycasting Demo", True, COLOURS["White"]
        )
        self.title_text.rect = pygame.Rect(
            self.width // 2 - self.title_text.image.get_width() // 2,
            100,
            self.title_text.image.get_width(),
            self.title_text.image.get_height(),
        )

    def update(self, event_list) -> None:

        """Method to run every frame and update scene behaviour."""

        ## Handle events
        for event in event_list:

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == pygame.BUTTON_LEFT
            ):
                pos = pygame.mouse.get_pos()
                clicked_buttons = [
                    b for b in self.group.buttons if b.rect.collidepoint(pos)
                ]
                print("Clicked at", pos, "on", clicked_buttons)

                for button in clicked_buttons:
                    button.function()

    def render(self) -> pygame.surface:

        """Creates and returns a surface of the scene to be drawn.

        Returns:
            pygame.surface: A surface of the scene frame.
        """

        # Background
        self.image.fill(COLOURS["Dark Grey"])

        # Draw sprite group
        self.group.text.draw(self.image)
        self.group.buttons.draw(self.image)

        return self.image
