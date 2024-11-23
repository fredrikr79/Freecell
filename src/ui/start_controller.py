import pygame

from .button import Button

from .controller import Controller

from .colors import (
    BACKGROUND_COLOR,
    BLACK_SUIT_COLOR,
    BUTTON_COLOR,
    TEXT_COLOR,
)


class StartController(Controller):
    def handle_event(self, event: pygame.Event):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        screen.fill(BACKGROUND_COLOR)

        # TODO: custom button

        title_font = pygame.Font("resources/dealerplate california.otf", 104)
        title = title_font.render("FREECELL", True, BUTTON_COLOR)

        screen.blit(
            title,
            (
                screen.width / 2 - title.width / 2,
                screen.height / 3 - title.height / 2,
            ),
        )

        width = screen.width / 3
        height = screen.height / 6
        top = screen.height / 3 * 2
        left = screen.width / 2 - width/2
        button = Button(
            "PLAY",
            width, height, top=top, left=left,
            border_radius=12,
            font_path="resources/whitrabt.ttf",
            text_pad=3,
            shadow_size=12,
            shadow_strength=0.05
        )

        button.draw(screen)
