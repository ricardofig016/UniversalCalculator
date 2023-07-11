import pygame, sys
from button import Button

pygame.init()

HEX_GREY = "#2C3333"
HEX_BLUE = "#A5C9CA"
HEX_WHITE = "#E7F6F2"

WIDTH = 800
HEIGHT = WIDTH * 0.75
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def get_font(size):
    return pygame.font.Font("assets/Roboto-Medium.ttf", int(size))


def main_menu():
    pygame.display.set_caption("Universal Calculator")

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        SPACING = HEIGHT * 0.09

        TEXT = get_font(HEIGHT * 0.1).render("Menu", True, HEX_BLUE)
        RECT = TEXT.get_rect(center=(WIDTH // 2, SPACING))

        CONVERSIONS_BUTTON = Button(
            image=None,
            pos=(WIDTH // 2, SPACING * 3),
            text_input="Conversions",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        FITNESS_BUTTON = Button(
            image=None,
            pos=(WIDTH // 2, SPACING * 4),
            text_input="Fitness",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        MATH_BUTTON = Button(
            image=None,
            pos=(WIDTH // 2, SPACING * 5),
            text_input="Math",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        GENERATORS_BUTTON = Button(
            image=None,
            pos=(WIDTH // 2, SPACING * 6),
            text_input="Generators",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        TIME_BUTTON = Button(
            image=None,
            pos=(WIDTH // 2, SPACING * 7),
            text_input="Time",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        EXIT_BUTTON = Button(
            image=None,
            pos=(WIDTH // 2, HEIGHT - SPACING),
            text_input="Exit",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        SCREEN.blit(TEXT, RECT)

        for button in [
            CONVERSIONS_BUTTON,
            FITNESS_BUTTON,
            MATH_BUTTON,
            GENERATORS_BUTTON,
            TIME_BUTTON,
            EXIT_BUTTON,
        ]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONVERSIONS_BUTTON.checkForInput(MOUSE_POS):
                    conversions()
                if FITNESS_BUTTON.checkForInput(MOUSE_POS):
                    fitness()
                if MATH_BUTTON.checkForInput(MOUSE_POS):
                    math()
                if GENERATORS_BUTTON.checkForInput(MOUSE_POS):
                    generators()
                if TIME_BUTTON.checkForInput(MOUSE_POS):
                    time()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def conversions():
    pass


def fitness():
    pass


def math():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        TEXT = get_font(36).render("Math Calculators", True, HEX_WHITE)
        RECT = TEXT.get_rect(center=(WIDTH // 2, 40))

        SCREEN.blit(TEXT, RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def generators():
    pass


def time():
    pass


main_menu()
