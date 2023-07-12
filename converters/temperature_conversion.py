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
            return "invalid_amt1"

        if self.unit1 == "Celsius(°C)":
            return self.convert_celsius()
        elif self.unit1 == "Fahrenheit(°F)":
            return self.convert_farenheit()
        elif self.unit1 == "Kelvin(K)":
            return self.convert_kelvin()
        elif self.unit1 == "Rankine(°R)":
            return self.convert_rankine()

        return "invalid_unit1"

    def convert_celsius(self):
        if self.unit2 == "Celsius(°C)":
            return self.amt1
        elif self.unit2 == "Fahrenheit(°F)":
            return self.amt1
        elif self.unit2 == "Kelvin(K)":
            return self.amt1
        elif self.unit2 == "Rankine(°R)":
            return self.amt1
