class TemperatureConversion(object):
    def __init__(self, amt1_str, unit1, unit2) -> None:
        try:
            self.amt1 = float(amt1_str)
        except ValueError:
            self.amt1 = "invalid_amt1"

        self.unit1 = unit1
        self.unit2 = unit2

    def convert(self):
        if self.amt1 == "invalid_amt1":
            return self.amt1

        if self.unit1 == "Celsius(°C)":
            if self.amt1 < -273.15:
                return "invalid_amt1"
            return self.convert_celsius()

        elif self.unit1 == "Fahrenheit(°F)":
            if self.amt1 < -459.67:
                return "invalid_amt1"
            return self.convert_fahrenheit()

        elif self.unit1 == "Kelvin(K)":
            if self.amt1 < 0:
                return "invalid_amt1"
            return self.convert_kelvin()

        elif self.unit1 == "Rankine(°R)":
            if self.amt1 < 0:
                return "invalid_amt1"
            return self.convert_rankine()

        return "invalid_unit1"

    def convert_celsius(self):
        if self.unit2 == "Celsius(°C)":
            return self.amt1 * 1
        elif self.unit2 == "Fahrenheit(°F)":
            return self.amt1 * 1.8 + 32
        elif self.unit2 == "Kelvin(K)":
            return self.amt1 + 273.15
        elif self.unit2 == "Rankine(°R)":
            return (self.amt1 + 273.15) * 1.8

    def convert_fahrenheit(self):
        if self.unit2 == "Celsius(°C)":
            return (self.amt1 - 32) * (5 / 9)
        elif self.unit2 == "Fahrenheit(°F)":
            return self.amt1 * 1
        elif self.unit2 == "Kelvin(K)":
            return (self.amt1 - 32) * (5 / 9) + 273.15
        elif self.unit2 == "Rankine(°R)":
            return self.amt1 + 459.67

    def convert_kelvin(self):
        if self.unit2 == "Celsius(°C)":
            return self.amt1 - 273.15
        elif self.unit2 == "Fahrenheit(°F)":
            return (self.amt1 - 273.15) * 1.8 + 32
        elif self.unit2 == "Kelvin(K)":
            return self.amt1 * 1
        elif self.unit2 == "Rankine(°R)":
            return self.amt1 * 1.8

    def convert_rankine(self):
        if self.unit2 == "Celsius(°C)":
            return (self.amt1 - 491.67) * (5 / 9)
        elif self.unit2 == "Fahrenheit(°F)":
            return self.amt1 - 459.67
        elif self.unit2 == "Kelvin(K)":
            return self.amt1 * (5 / 9)
        elif self.unit2 == "Rankine(°R)":
            return self.amt1 * 1
