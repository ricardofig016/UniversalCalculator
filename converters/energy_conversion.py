class EnergyConversion(object):
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

        if self.unit1 == "joule(J)":
            return self.convert_joule()
        if self.unit1 == "kilojoule(kJ)":
            return self.convert_kilojoule()
        if self.unit1 == "watt-hour(Wh)":
            return self.convert_watthour()
        if self.unit1 == "kilowatt-hour(kWh)":
            return self.convert_kilowatthour()
        if self.unit1 == "kilocalorie(kcal)":
            return self.convert_kilocalorie()
        if self.unit1 == "Btu":
            return self.convert_btu()

        return "invalid_unit1"

    def convert_joule(self):
        if self.unit2 == "joule(J)":
            return self.amt1 * 1
        if self.unit2 == "kilojoule(kJ)":
            return self.amt1 * 0.001
        if self.unit2 == "watt-hour(Wh)":
            return self.amt1 * 0.0002777778
        if self.unit2 == "kilowatt-hour(kWh)":
            return self.amt1 * 2.777777777e-7
        if self.unit2 == "kilocalorie(kcal)":
            return self.amt1 * 0.0002388459
        if self.unit2 == "Btu":
            return self.amt1 * 0.0009478171
        return "invalid_unit2"

    def convert_kilojoule(self):
        if self.unit2 == "joule(J)":
            return self.amt1 * 1000
        if self.unit2 == "kilojoule(kJ)":
            return self.amt1 * 1
        if self.unit2 == "watt-hour(Wh)":
            return self.amt1 * 0.2777777778
        if self.unit2 == "kilowatt-hour(kWh)":
            return self.amt1 * 0.0002777778
        if self.unit2 == "kilocalorie(kcal)":
            return self.amt1 * 0.2388458966
        if self.unit2 == "Btu":
            return self.amt1 * 0.9478171203
        return "invalid_unit2"

    def convert_watthour(self):
        if self.unit2 == "joule(J)":
            return self.amt1 * 3600
        if self.unit2 == "kilojoule(kJ)":
            return self.amt1 * 3.6
        if self.unit2 == "watt-hour(Wh)":
            return self.amt1 * 1
        if self.unit2 == "kilowatt-hour(kWh)":
            return self.amt1 * 0.001
        if self.unit2 == "kilocalorie(kcal)":
            return self.amt1 * 0.8598452279
        if self.unit2 == "Btu":
            return self.amt1 * 3.4121416331
        return "invalid_unit2"

    def convert_kilowatthour(self):
        if self.unit2 == "joule(J)":
            return self.amt1 * 3600000
        if self.unit2 == "kilojoule(kJ)":
            return self.amt1 * 3600
        if self.unit2 == "watt-hour(Wh)":
            return self.amt1 * 1000
        if self.unit2 == "kilowatt-hour(kWh)":
            return self.amt1 * 1
        if self.unit2 == "kilocalorie(kcal)":
            return self.amt1 * 859.84522786
        if self.unit2 == "Btu":
            return self.amt1 * 3412.1416331
        return "invalid_unit2"

    def convert_kilocalorie(self):
        if self.unit2 == "joule(J)":
            return self.amt1 * 4186.8
        if self.unit2 == "kilojoule(kJ)":
            return self.amt1 * 4.1868
        if self.unit2 == "watt-hour(Wh)":
            return self.amt1 * 1.163
        if self.unit2 == "kilowatt-hour(kWh)":
            return self.amt1 * 0.001163
        if self.unit2 == "kilocalorie(kcal)":
            return self.amt1 * 1
        if self.unit2 == "Btu":
            return self.amt1 * 3.9683207193
        return "invalid_unit2"

    def convert_btu(self):
        if self.unit2 == "joule(J)":
            return self.amt1 * 1055.0558526
        if self.unit2 == "kilojoule(kJ)":
            return self.amt1 * 1.0550558526
        if self.unit2 == "watt-hour(Wh)":
            return self.amt1 * 0.2930710702
        if self.unit2 == "kilowatt-hour(kWh)":
            return self.amt1 * 0.0002930711
        if self.unit2 == "kilocalorie(kcal)":
            return self.amt1 * 0.2519957611
        if self.unit2 == "Btu":
            return self.amt1 * 1
        return "invalid_unit2"
