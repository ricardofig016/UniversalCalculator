import pygame, sys
from button import Button
from length_conversion import LengthConversion

pygame.init()

HEX_GREY = "#2C3333"
HEX_BLUE = "#A5C9CA"
HEX_WHITE = "#E7F6F2"

WIDTH = 860
HEIGHT = WIDTH * 0.7
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def get_font(size):
    return pygame.font.Font("assets/Roboto-Medium.ttf", int(size))


def main_menu():
    pygame.display.set_caption("Universal Calculator")

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        Y_SPACING = HEIGHT * 0.1

        TEXT = get_font(HEIGHT * 0.1).render("Menu", True, HEX_BLUE)
        RECT = TEXT.get_rect(center=(WIDTH * 0.5, Y_SPACING))
        SCREEN.blit(TEXT, RECT)

        CONVERSIONS_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 3),
            text_input="Conversions",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        FITNESS_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 4),
            text_input="Fitness",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        MATH_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 5),
            text_input="Math",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        GENERATORS_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 6),
            text_input="Generators",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        TIME_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 7),
            text_input="Time",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        BACK_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.4, HEIGHT - Y_SPACING),
            text_input="Back",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        EXIT_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.6, HEIGHT - Y_SPACING),
            text_input="Exit",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        for button in [
            CONVERSIONS_BUTTON,
            FITNESS_BUTTON,
            MATH_BUTTON,
            GENERATORS_BUTTON,
            TIME_BUTTON,
            BACK_BUTTON,
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
                    conversions_menu()
                if FITNESS_BUTTON.checkForInput(MOUSE_POS):
                    fitness_menu()
                if MATH_BUTTON.checkForInput(MOUSE_POS):
                    math_menu()
                if GENERATORS_BUTTON.checkForInput(MOUSE_POS):
                    generators_menu()
                if TIME_BUTTON.checkForInput(MOUSE_POS):
                    time_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def conversions_menu():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        Y_SPACING = HEIGHT * 0.1

        TEXT = get_font(HEIGHT * 0.1).render("Conversions", True, HEX_BLUE)
        RECT = TEXT.get_rect(center=(WIDTH * 0.5, Y_SPACING))
        SCREEN.blit(TEXT, RECT)

        AREA_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 3),
            text_input="Area",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        LENGTH_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 4),
            text_input="Length",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        TEMPERATURE_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 5),
            text_input="Temperature",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        VOLUME_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 6),
            text_input="Volume",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        WEIGHT_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.5, Y_SPACING * 7),
            text_input="Weight",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        BACK_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.4, HEIGHT - Y_SPACING),
            text_input="Back",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        EXIT_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.6, HEIGHT - Y_SPACING),
            text_input="Exit",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        for button in [
            AREA_BUTTON,
            LENGTH_BUTTON,
            TEMPERATURE_BUTTON,
            VOLUME_BUTTON,
            WEIGHT_BUTTON,
            BACK_BUTTON,
            EXIT_BUTTON,
        ]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AREA_BUTTON.checkForInput(MOUSE_POS):
                    conversions_area_menu()
                if LENGTH_BUTTON.checkForInput(MOUSE_POS):
                    conversions_length_menu()
                if TEMPERATURE_BUTTON.checkForInput(MOUSE_POS):
                    conversions_temperature_menu()
                if VOLUME_BUTTON.checkForInput(MOUSE_POS):
                    conversions_volume_menu()
                if WEIGHT_BUTTON.checkForInput(MOUSE_POS):
                    conversions_weight_menu()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    main_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def conversions_area_menu():
    pass


def conversions_length_menu():
    unit1 = "kilometer(km)"
    unit2 = "meter(m)"
    amt1 = "1"
    c = LengthConversion(amt1, unit1, unit2)
    amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Length
        text = get_font(HEIGHT * 0.1).render("Length", True, HEX_BLUE)
        rect = text.get_rect(center=(WIDTH * 0.5, Y_SPACING))
        SCREEN.blit(text, rect)

        # amt1
        text = get_font(HEIGHT * 0.04).render(amt1, True, HEX_WHITE)
        rect = text.get_rect(center=(WIDTH // 2 - X_SPACING, Y_SPACING * 3))
        SCREEN.blit(text, rect)

        # =
        text = get_font(HEIGHT * 0.04).render("=", True, HEX_WHITE)
        rect = text.get_rect(center=(WIDTH * 0.5, Y_SPACING * 4))
        SCREEN.blit(text, rect)

        # amt2
        text = get_font(HEIGHT * 0.04).render(amt2, True, HEX_WHITE)
        rect = text.get_rect(center=(WIDTH // 2 - X_SPACING, Y_SPACING * 5))
        SCREEN.blit(text, rect)

        UNIT1_BUTTON = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * 3),
            text_input=unit1,
            font=get_font(HEIGHT * 0.04),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        UNIT2_BUTTON = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * 5),
            text_input=unit2,
            font=get_font(HEIGHT * 0.04),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        BACK_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.4, HEIGHT - Y_SPACING),
            text_input="Back",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        EXIT_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.6, HEIGHT - Y_SPACING),
            text_input="Exit",
            font=get_font(HEIGHT * 0.05),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )

        for button in [
            UNIT1_BUTTON,
            UNIT2_BUTTON,
            BACK_BUTTON,
            EXIT_BUTTON,
        ]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    amt1 += "0"
                elif event.key == pygame.K_1:
                    amt1 += "1"
                elif event.key == pygame.K_2:
                    amt1 += "2"
                elif event.key == pygame.K_3:
                    amt1 += "3"
                elif event.key == pygame.K_4:
                    amt1 += "4"
                elif event.key == pygame.K_5:
                    amt1 += "5"
                elif event.key == pygame.K_6:
                    amt1 += "6"
                elif event.key == pygame.K_7:
                    amt1 += "7"
                elif event.key == pygame.K_8:
                    amt1 += "8"
                elif event.key == pygame.K_9:
                    amt1 += "9"
                elif event.key == pygame.K_PERIOD or event.key == pygame.K_COMMA:
                    amt1 += "."
                elif event.key == pygame.K_PLUS and (len(amt1) == 0 or amt1[-1] == "e"):
                    amt1 += "+"
                elif event.key == pygame.K_MINUS and (
                    len(amt1) == 0 or amt1[-1] == "e"
                ):
                    amt1 += "-"
                elif event.key == pygame.K_e and len(amt1) != 0:
                    amt1 += "e"
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = LengthConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_length_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_length_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = LengthConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

        pygame.display.update()


def conversions_length_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        METER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="meter(m)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        KILOMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="kilometer(km)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        DECIMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="decimeter(dm)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        CENTIMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="centimeter(cm)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        MILIMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="milimeter(mm)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        MICROMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="micrometer(μm)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        NANOMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="nanometer(nm)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        MILE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="mile(mi)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        YARD = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="yard(yd)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        FOOT = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="foot(ft)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        INCH = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="inch(in)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        LIGH_YEAR = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="light year(ly)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        for button in [
            METER,
            KILOMETER,
            DECIMETER,
            CENTIMETER,
            MILIMETER,
            MICROMETER,
            NANOMETER,
            MILE,
            YARD,
            FOOT,
            INCH,
            LIGH_YEAR,
        ]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return curr_unit

            if event.type == pygame.MOUSEBUTTONDOWN:
                if METER.checkForInput(MOUSE_POS):
                    return "meter(m)"
                if KILOMETER.checkForInput(MOUSE_POS):
                    return "kilometer(km)"
                if DECIMETER.checkForInput(MOUSE_POS):
                    return "decimeter(dm)"
                if CENTIMETER.checkForInput(MOUSE_POS):
                    return "centimeter(cm)"
                if MILIMETER.checkForInput(MOUSE_POS):
                    return "milimeter(mm)"
                if MICROMETER.checkForInput(MOUSE_POS):
                    return "micrometer(μm)"
                if NANOMETER.checkForInput(MOUSE_POS):
                    return "nanometer(nm)"
                if MILE.checkForInput(MOUSE_POS):
                    return "mile(mi)"
                if YARD.checkForInput(MOUSE_POS):
                    return "yard(yd)"
                if FOOT.checkForInput(MOUSE_POS):
                    return "foot(ft)"
                if INCH.checkForInput(MOUSE_POS):
                    return "inch(in)"
                if LIGH_YEAR.checkForInput(MOUSE_POS):
                    return "light year(ly)"

        pygame.display.update()


def conversions_temperature_menu():
    pass


def conversions_volume_menu():
    pass


def conversions_weight_menu():
    pass


def fitness_menu():
    pass


def math_menu():
    pass


def generators_menu():
    pass


def time_menu():
    pass


main_menu()
