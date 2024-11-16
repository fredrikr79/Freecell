import pygame

FPS = 60

class App:
    FPS: int
    screen: pygame.Surface
    clock: pygame.Clock
    is_running: bool

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.Clock()
        self.is_running = True
    
    def main_loop(self):
        self.handle_events()
        self.update_view()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update_view(self):
        self.screen.fill("green")

        pygame.draw.circle(
            self.screen,
            "magenta",
            pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2),
            40,
        )

        pygame.display.flip()

        self.clock.tick(FPS)


