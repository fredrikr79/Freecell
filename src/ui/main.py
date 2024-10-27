from .app import App


def main():
    app = App()

    while app.is_running:
        app.main_loop()


if __name__ == "__main__":
    main()
