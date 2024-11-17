import pygame

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

        font = pygame.Font("resources/typewriter.ttf", 42)
        title = font.render("FREECELL", True, BUTTON_COLOR)

        screen.blit(
            title,
            (
                screen.width / 2 - title.width / 2,
                screen.height / 3 - title.height / 2,
            ),
        )

        button_rect_width = screen.width / 6
        button_rect_height = screen.height / 12
        button_rect = pygame.Rect(
            screen.width / 2 - button_rect_width / 2,
            screen.height / 3 * 2 - button_rect_height / 2,
            button_rect_width,
            button_rect_height,
        )

        pygame.draw.rect(
            screen, BLACK_SUIT_COLOR, button_rect, border_radius=12
        )

        button_text = font.render("PLAY", True, BUTTON_COLOR)

        screen.blit(
            button_text,
            (
                button_rect.x + button_rect.width / 2 - button_text.width / 2,
                button_rect.y
                + button_rect.height / 2
                - button_text.height / 2,
            ),
        )
