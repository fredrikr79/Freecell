import pygame

from dataclasses import dataclass

@dataclass
class Button:
    text: str
    width: int
    height: int
    top: int = 0
    left: int = 0
    border_radius: int = 0

    def __post_init__(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.pos = (self.top, self.left)

    def blit(self, destination: pygame.Surface):
        destination.blit(self.surface, self.pos)
