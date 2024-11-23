import pygame

from dataclasses import dataclass, field
from typing import Optional

from .colors import BUTTON_COLOR, TEXT_COLOR


@dataclass
class Button:
    text: str
    width: float
    height: float
    top: float = 0
    left: float = 0
    border_radius: int = 0
    bg_color: pygame.Color = field(default_factory=lambda: BUTTON_COLOR)
    text_color: pygame.Color = field(default_factory=lambda: TEXT_COLOR)
    font_size: Optional[int] = None
    font_path: Optional[str] = None
    text_pad: int = 0
    shadow_size: int = 0
    shadow_strength: float = 0.1

    def __post_init__(self):
        self.pos = (self.top, self.left)
        self.size = (self.width, self.height)

        self.font = pygame.Font(self.font_path)
        self.font_size = self._calculate_font_size()
        self.font.set_point_size(self.font_size)

        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = pygame.Rect(self.pos, self.size)

        self._render()

    def _calculate_font_size(self) -> int:
        padded_width = self.width - self.text_pad * 2
        padded_height = self.height - self.text_pad * 2
        font_size = int(min(padded_width, padded_height))

        self.font.set_point_size(font_size)
        text_width, text_height = self.font.size(self.text)

        while text_width > padded_width or text_height > padded_height:
            font_size = int(font_size * 0.9)
            self.font.set_point_size(font_size)
            text_width, text_height = self.font.size(self.text)

        return font_size

    def _render(self):
        container_rect = self.surface.fill((0, 0, 0, 0))

        height = self.height - self.shadow_size

        shadow_rect = pygame.draw.rect(
            self.surface,
            self.bg_color.lerp(pygame.Color("black"), self.shadow_strength),
            (0, self.shadow_size, self.width, height),
            border_radius=self.border_radius,
        )

        upper_rect = pygame.draw.rect(
            self.surface,
            self.bg_color,
            (0, 0, self.width, height),
            border_radius=self.border_radius,
        )

        text_surface = self.font.render(self.text, True, self.text_color)

        text_rect = text_surface.get_rect(
            center=(self.width // 2, self.height // 2)
        )

        self.surface.blit(text_surface, text_rect)

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        return screen.blit(self.surface, (self.left, self.top))
