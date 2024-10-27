import pygame

FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("green")

        pygame.draw.circle(
            screen,
            "magenta",
            pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2),
            40,
        )

        pygame.display.flip()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
