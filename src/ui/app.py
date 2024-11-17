import pygame

from .start_controller import StartController
from .controller import Controller

from .events import SWITCH_CONTROLLER_EVENT


class App:
    FPS: int = 60

    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

    screen: pygame.Surface
    clock: pygame.Clock

    current_controller: Controller

    is_running: bool

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(App.SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.current_controller = StartController()
        self.is_running = True

    def main_loop(self):
        self.handle_events()
        self.update_view()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == SWITCH_CONTROLLER_EVENT:
                self.current_controller = event.new_controller
            else:
                self.current_controller.handle_event(event)

    def update_view(self):
        self.screen.fill("black")

        self.current_controller.update()
        self.current_controller.render(self.screen)

        pygame.display.flip()
        self.clock.tick(App.FPS)
