# conversion formulas based on https://www.unitconverters.net

import pygame, sys
from button import Button
from converters.angle_conversion import AngleConversion
from converters.area_conversion import AreaConversion
from converters.currency_conversion import CurrencyConversion
from converters.data_conversion import DataConversion
from converters.energy_conversion import EnergyConversion
from converters.length_conversion import LengthConversion
from converters.numbers_conversion import NumbersConversion
from converters.temperature_conversion import TemperatureConversion

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
                    # fitness_menu()
                    pass
                if MATH_BUTTON.checkForInput(MOUSE_POS):
                    # math_menu()
                    pass
                if GENERATORS_BUTTON.checkForInput(MOUSE_POS):
                    # generators_menu()
                    pass
                if TIME_BUTTON.checkForInput(MOUSE_POS):
                    # time_menu()
                    pass
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def conversions_menu():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        Y_SPACING = HEIGHT * 0.085
        button_size_multiplier = 0.05
        button_counter = 3

        text = get_font(HEIGHT * 0.1).render("Conversions", True, HEX_BLUE)
        rect = text.get_rect(center=(WIDTH * 0.5, Y_SPACING))
        SCREEN.blit(text, rect)

        ANGLE_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Angle",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        AREA_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Area",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        CURRENCY_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Currency",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        DATA_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Data Storage",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        ENERGY_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Energy",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        LENGTH_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Length",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        NUMBERS_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.25, Y_SPACING * button_counter),
            text_input="Numbers",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        button_counter = 3

        PREFIXES_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Prefixes",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        PRESSURE_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Pressure",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        SPEED_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Speed",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        TEMPERATURE_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Temperature",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        TIME_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Time",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        VOLUME_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Volume",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

        WEIGHT_BUTTON = Button(
            image=None,
            pos=(WIDTH * 0.75, Y_SPACING * button_counter),
            text_input="Weight",
            font=get_font(HEIGHT * button_size_multiplier),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        button_counter += 1

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
            ANGLE_BUTTON,
            AREA_BUTTON,
            CURRENCY_BUTTON,
            DATA_BUTTON,
            ENERGY_BUTTON,
            LENGTH_BUTTON,
            NUMBERS_BUTTON,
            PREFIXES_BUTTON,
            PRESSURE_BUTTON,
            SPEED_BUTTON,
            TEMPERATURE_BUTTON,
            TIME_BUTTON,
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
                if ANGLE_BUTTON.checkForInput(MOUSE_POS):
                    conversions_angle_menu()
                if AREA_BUTTON.checkForInput(MOUSE_POS):
                    conversions_area_menu()
                if CURRENCY_BUTTON.checkForInput(MOUSE_POS):
                    conversions_currency_menu()
                if DATA_BUTTON.checkForInput(MOUSE_POS):
                    conversions_data_menu()
                if ENERGY_BUTTON.checkForInput(MOUSE_POS):
                    conversions_energy_menu()
                if LENGTH_BUTTON.checkForInput(MOUSE_POS):
                    conversions_length_menu()
                if NUMBERS_BUTTON.checkForInput(MOUSE_POS):
                    conversions_numbers_menu()
                if TEMPERATURE_BUTTON.checkForInput(MOUSE_POS):
                    conversions_temperature_menu()
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    main_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def conversions_angle_menu():
    unit1 = "degree(º)"
    unit2 = "radian(π)"
    amt1 = "360"
    c = AngleConversion(amt1, unit1, unit2)
    try:
        amt2 = str(round(c.convert(), 2))
    except TypeError:
        amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Angle
        text = get_font(HEIGHT * 0.1).render("Angle", True, HEX_BLUE)
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
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = AngleConversion(amt1, unit1, unit2)
                try:
                    amt2 = str(round(c.convert(), 2))
                except TypeError:
                    amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_angle_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_angle_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = AngleConversion(amt1, unit1, unit2)
                try:
                    amt2 = str(round(c.convert(), 2))
                except TypeError:
                    amt2 = str(c.convert())

        pygame.display.update()


def conversions_angle_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        DEGREE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="degree(º)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        RADIAN = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="radian(π)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        MINUTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="minute(')",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        SECOND = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="second('')",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        CIRCLE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="circle",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        QUADRANT = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="quadrant",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        for button in [DEGREE, RADIAN, MINUTE, SECOND, CIRCLE, QUADRANT]:
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
                if DEGREE.checkForInput(MOUSE_POS):
                    return "degree(º)"
                if RADIAN.checkForInput(MOUSE_POS):
                    return "radian(π)"
                if MINUTE.checkForInput(MOUSE_POS):
                    return "minute(')"
                if SECOND.checkForInput(MOUSE_POS):
                    return "second('')"
                if CIRCLE.checkForInput(MOUSE_POS):
                    return "circle"
                if QUADRANT.checkForInput(MOUSE_POS):
                    return "quadrant"

        pygame.display.update()


def conversions_area_menu():
    unit1 = "square kilometer(km²)"
    unit2 = "square meter(m²)"
    amt1 = "1"
    c = AreaConversion(amt1, unit1, unit2)
    amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Area
        text = get_font(HEIGHT * 0.1).render("Area", True, HEX_BLUE)
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
                elif event.key == pygame.K_e and len(amt1) != 0 and not "e" in amt1:
                    amt1 += "e"
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = AreaConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_area_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_area_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = AreaConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

        pygame.display.update()


def conversions_area_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        METER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square meter(m²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        KILOMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square kilometer(km²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        CENTIMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square centimeter(cm²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        MILIMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square milimeter(mm²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        MICROMETER = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square micrometer(μm²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        HECTARE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="hectare(ha)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        ACRE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="acre(ac)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        MILE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square mile(mi²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        YARD = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square yard(yd²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        FOOT = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square foot(ft²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        INCH = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="square inch(in²)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.35

        for button in [
            METER,
            KILOMETER,
            CENTIMETER,
            MILIMETER,
            MICROMETER,
            HECTARE,
            ACRE,
            MILE,
            YARD,
            FOOT,
            INCH,
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
                    return "square meter(m²)"
                if KILOMETER.checkForInput(MOUSE_POS):
                    return "square kilometer(km²)"
                if CENTIMETER.checkForInput(MOUSE_POS):
                    return "square centimeter(cm²)"
                if MILIMETER.checkForInput(MOUSE_POS):
                    return "square milimeter(mm²)"
                if MICROMETER.checkForInput(MOUSE_POS):
                    return "square micrometer(μm²)"
                if HECTARE.checkForInput(MOUSE_POS):
                    return "hectare(ha)"
                if ACRE.checkForInput(MOUSE_POS):
                    return "acre(ac)"
                if MILE.checkForInput(MOUSE_POS):
                    return "square mile(mi²)"
                if YARD.checkForInput(MOUSE_POS):
                    return "square yard(yd²)"
                if FOOT.checkForInput(MOUSE_POS):
                    return "square foot(ft²)"
                if INCH.checkForInput(MOUSE_POS):
                    return "square inch(in²)"

        pygame.display.update()


def conversions_currency_menu():
    unit1 = "USD(US Dollar)"
    unit2 = "EUR(Euro)"
    amt1 = "1"
    c = CurrencyConversion(amt1, unit1, unit2)
    amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Currency
        text = get_font(HEIGHT * 0.1).render("Currency", True, HEX_BLUE)
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
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = CurrencyConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_currency_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_currency_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = CurrencyConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

        pygame.display.update()


def conversions_currency_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        USD = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="USD(US Dollar)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        EUR = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="EUR(Euro)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        AUD = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="AUD(Australian Dollar)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        CAD = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="CAD(Canadian Dollar)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        CHF = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="CHF(Swiss Franc)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        CNY = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="CNY(Chinese Yuan)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        GBP = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="GBP(British Pound Strerling)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        INR = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="INR(Indian Rupee)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        JPY = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="JPY(Japanese Yen)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        MXP = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="MXN(Mexican Peso)",
            font=get_font(HEIGHT * 0.025),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        for button in [USD, EUR, AUD, CAD, CHF, CNY, GBP, INR, JPY, MXP]:
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
                if USD.checkForInput(MOUSE_POS):
                    return "USD(US Dollar)"
                if EUR.checkForInput(MOUSE_POS):
                    return "EUR(Euro)"
                if AUD.checkForInput(MOUSE_POS):
                    return "AUD(Australian Dollar)"
                if CAD.checkForInput(MOUSE_POS):
                    return "CAD(Canadian Dollar)"
                if CHF.checkForInput(MOUSE_POS):
                    return "CHF(Swiss Franc)"
                if CNY.checkForInput(MOUSE_POS):
                    return "CNY(Chinese Yuan)"
                if GBP.checkForInput(MOUSE_POS):
                    return "GBP(British Pound Strerling)"
                if INR.checkForInput(MOUSE_POS):
                    return "INR(Indian Rupee)"
                if JPY.checkForInput(MOUSE_POS):
                    return "JPY(Japanese Yen)"
                if MXP.checkForInput(MOUSE_POS):
                    return "MXN(Mexican Peso)"

        pygame.display.update()


def conversions_data_menu():
    unit1 = "Byte(B)"
    unit2 = "bit(b)"
    amt1 = "1"
    c = DataConversion(amt1, unit1, unit2)
    try:
        amt2 = str(round(c.convert(), 2))
    except TypeError:
        amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Data
        text = get_font(HEIGHT * 0.1).render("Data", True, HEX_BLUE)
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
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = DataConversion(amt1, unit1, unit2)
                try:
                    amt2 = str(round(c.convert(), 2))
                except TypeError:
                    amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_data_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_data_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = DataConversion(amt1, unit1, unit2)
                try:
                    amt2 = str(round(c.convert(), 2))
                except TypeError:
                    amt2 = str(c.convert())

        pygame.display.update()


def conversions_data_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        BIT = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="bit(b)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        BYTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="Byte(B)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        WORD = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="word",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        BLOCK = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="block",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        KILOBYTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="kiloByte(kB)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        MEGABYTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="megaByte(MB)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        GIGABYTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="gigaByte(GB)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        TERABYTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="teraByte(TB)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        PETABYTE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="petaByte(PB)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        for button in [
            BIT,
            BYTE,
            WORD,
            BLOCK,
            KILOBYTE,
            MEGABYTE,
            GIGABYTE,
            TERABYTE,
            PETABYTE,
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
                if BIT.checkForInput(MOUSE_POS):
                    return "bit(b)"
                if BYTE.checkForInput(MOUSE_POS):
                    return "Byte(B)"
                if WORD.checkForInput(MOUSE_POS):
                    return "word"
                if BLOCK.checkForInput(MOUSE_POS):
                    return "block"
                if KILOBYTE.checkForInput(MOUSE_POS):
                    return "kiloByte(kB)"
                if MEGABYTE.checkForInput(MOUSE_POS):
                    return "megaByte(MB)"
                if GIGABYTE.checkForInput(MOUSE_POS):
                    return "gigaByte(GB)"
                if TERABYTE.checkForInput(MOUSE_POS):
                    return "teraByte(TB)"
                if PETABYTE.checkForInput(MOUSE_POS):
                    return "petaByte(PB)"

        pygame.display.update()


def conversions_energy_menu():
    unit1 = "kilocalorie(kcal)"
    unit2 = "kilojoule(kJ)"
    amt1 = "90"
    c = EnergyConversion(amt1, unit1, unit2)
    try:
        amt2 = str(round(c.convert(), 2))
    except TypeError:
        amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Energy
        text = get_font(HEIGHT * 0.1).render("Energy", True, HEX_BLUE)
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
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = EnergyConversion(amt1, unit1, unit2)
                try:
                    amt2 = str(round(c.convert(), 2))
                except TypeError:
                    amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_energy_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_energy_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = EnergyConversion(amt1, unit1, unit2)
                try:
                    amt2 = str(round(c.convert(), 2))
                except TypeError:
                    amt2 = str(c.convert())

        pygame.display.update()


def conversions_energy_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        JOULE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="joule(J)",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        KILOJOULE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="kilojoule(kJ)",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        WATTHOUR = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="watt-hour(Wh)",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        KILOWATTHOUR = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="kilowatt-hour(kWh)",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        KILOCALORIE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="kilocalorie(kcal)",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5
        BTU = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="Btu",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        for button in [JOULE, KILOJOULE, WATTHOUR, KILOWATTHOUR, KILOCALORIE, BTU]:
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
                if JOULE.checkForInput(MOUSE_POS):
                    return "joule(J)"
                if KILOJOULE.checkForInput(MOUSE_POS):
                    return "kilojoule(kJ)"
                if WATTHOUR.checkForInput(MOUSE_POS):
                    return "watt-hour(Wh)"
                if KILOWATTHOUR.checkForInput(MOUSE_POS):
                    return "kilowatt-hour(kWh)"
                if KILOCALORIE.checkForInput(MOUSE_POS):
                    return "kilocalorie(kcal)"
                if BTU.checkForInput(MOUSE_POS):
                    return "Btu"

        pygame.display.update()


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
                elif event.key == pygame.K_e and len(amt1) != 0 and not "e" in amt1:
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


def conversions_numbers_menu():
    unit1 = "decimal"
    unit2 = "roman"
    amt1 = "56"
    c = NumbersConversion(amt1, unit1, unit2)
    amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Numbers
        text = get_font(HEIGHT * 0.1).render("Numbers", True, HEX_BLUE)
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
                if unit1 == "roman":
                    if event.key == pygame.K_i:
                        amt1 += "I"

                    if event.key == pygame.K_v:
                        amt1 += "V"

                    if event.key == pygame.K_x:
                        amt1 += "X"

                    if event.key == pygame.K_l:
                        amt1 += "L"

                    if event.key == pygame.K_c:
                        amt1 += "C"

                    if event.key == pygame.K_d:
                        amt1 += "D"

                    if event.key == pygame.K_m:
                        amt1 += "M"

                elif unit1 == "hex":
                    if event.key == pygame.K_0:
                        amt1 += "0"
                    if event.key == pygame.K_1:
                        amt1 += "1"
                    if event.key == pygame.K_2:
                        amt1 += "2"
                    if event.key == pygame.K_3:
                        amt1 += "3"
                    if event.key == pygame.K_4:
                        amt1 += "4"
                    if event.key == pygame.K_5:
                        amt1 += "5"
                    if event.key == pygame.K_6:
                        amt1 += "6"
                    if event.key == pygame.K_7:
                        amt1 += "7"
                    if event.key == pygame.K_8:
                        amt1 += "8"
                    if event.key == pygame.K_9:
                        amt1 += "9"
                    if event.key == pygame.K_a:
                        amt1 += "A"
                    if event.key == pygame.K_b:
                        amt1 += "B"
                    if event.key == pygame.K_c:
                        amt1 += "C"
                    if event.key == pygame.K_d:
                        amt1 += "D"
                    if event.key == pygame.K_e:
                        amt1 += "E"
                    if event.key == pygame.K_f:
                        amt1 += "F"
                elif unit1 == "decimal":
                    if event.key == pygame.K_0:
                        amt1 += "0"
                    if event.key == pygame.K_1:
                        amt1 += "1"
                    if event.key == pygame.K_2:
                        amt1 += "2"
                    if event.key == pygame.K_3:
                        amt1 += "3"
                    if event.key == pygame.K_4:
                        amt1 += "4"
                    if event.key == pygame.K_5:
                        amt1 += "5"
                    if event.key == pygame.K_6:
                        amt1 += "6"
                    if event.key == pygame.K_7:
                        amt1 += "7"
                    if event.key == pygame.K_8:
                        amt1 += "8"
                    if event.key == pygame.K_9:
                        amt1 += "9"
                elif unit1 == "binary":
                    if event.key == pygame.K_0:
                        amt1 += "0"
                    if event.key == pygame.K_1:
                        amt1 += "1"

                if event.key == pygame.K_ESCAPE:
                    amt1 = ""
                if event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = NumbersConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_numbers_menu_unit_selection(unit1, 0)
                    amt1 = ""
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_numbers_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = NumbersConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

        pygame.display.update()


def conversions_numbers_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        DECIMAL = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="decimal",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        BINARY = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="binary",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        HEX = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="hex",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        ROMAN = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="roman",
            font=get_font(HEIGHT * 0.035),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.5

        for button in [DECIMAL, BINARY, HEX, ROMAN]:
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
                if DECIMAL.checkForInput(MOUSE_POS):
                    return "decimal"
                if BINARY.checkForInput(MOUSE_POS):
                    return "binary"
                if HEX.checkForInput(MOUSE_POS):
                    return "hex"
                if ROMAN.checkForInput(MOUSE_POS):
                    return "roman"

        pygame.display.update()


def conversions_temperature_menu():
    unit1 = "Fahrenheit(°F)"
    unit2 = "Celsius(°C)"
    amt1 = "70"
    c = TemperatureConversion(amt1, unit1, unit2)
    amt2 = str(c.convert())

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1

        # Temperature
        text = get_font(HEIGHT * 0.1).render("Temperature", True, HEX_BLUE)
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
                elif event.key == pygame.K_e and len(amt1) != 0 and not "e" in amt1:
                    amt1 += "e"
                elif event.key == pygame.K_ESCAPE:
                    amt1 = ""
                elif event.key == pygame.K_BACKSPACE:
                    amt1 = amt1[:-1]

                c = TemperatureConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNIT1_BUTTON.checkForInput(MOUSE_POS):
                    unit1 = conversions_temperature_menu_unit_selection(unit1, 0)
                if UNIT2_BUTTON.checkForInput(MOUSE_POS):
                    unit2 = conversions_temperature_menu_unit_selection(unit2, 2)
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    conversions_menu()
                if EXIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                c = TemperatureConversion(amt1, unit1, unit2)
                amt2 = str(c.convert())

        pygame.display.update()


def conversions_temperature_menu_unit_selection(curr_unit, flag):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(HEX_GREY)

        X_SPACING = WIDTH * 0.25
        Y_SPACING = HEIGHT * 0.1
        y_increment = 3.5

        CELSIUS = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="Celsius(°C)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        FAHRENHEIT = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="Fahrenheit(°F)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        KELVIN = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="Kelvin(K)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        RANKINE = Button(
            image=None,
            pos=(WIDTH - X_SPACING, Y_SPACING * (y_increment + flag)),
            text_input="Rankine(°R)",
            font=get_font(HEIGHT * 0.03),
            base_color=HEX_WHITE,
            hovering_color=HEX_BLUE,
        )
        y_increment += 0.4

        for button in [CELSIUS, FAHRENHEIT, KELVIN, RANKINE]:
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
                if CELSIUS.checkForInput(MOUSE_POS):
                    return "Celsius(°C)"
                if FAHRENHEIT.checkForInput(MOUSE_POS):
                    return "Fahrenheit(°F)"
                if KELVIN.checkForInput(MOUSE_POS):
                    return "Kelvin(K)"
                if RANKINE.checkForInput(MOUSE_POS):
                    return "Rankine(°R)"

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
