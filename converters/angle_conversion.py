class AngleConversion(object):
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

        if self.unit1 == "degree(º)":
            return self.convert_degree()

        if self.unit1 == "radian(π)":
            return self.convert_radian()

        if self.unit1 == "minute(')":
            return self.convert_minute()

        if self.unit1 == "second('')":
            return self.convert_second()

        if self.unit1 == "circle":
            return self.convert_circle()

        if self.unit1 == "quadrant":
            return self.convert_quadrant()

        return "invalid_unit1"

    def convert_degree(self):
        if self.unit2 == "degree(º)":
            return self.amt1 * 1
        if self.unit2 == "radian(π)":
            return self.amt1 * 0.00555555555
        if self.unit2 == "minute(')":
            return self.amt1 * 60
        if self.unit2 == "second('')":
            return self.amt1 * 3600
        if self.unit2 == "circle":
            return self.amt1 * 0.0027777778
        if self.unit2 == "quadrant":
            return self.amt1 * 0.0111111110
        return "invalid_unit2"

    def convert_radian(self):
        if self.unit2 == "degree(º)":
            return self.amt1 * 180
        if self.unit2 == "radian(π)":
            return self.amt1 * 1
        if self.unit2 == "minute(')":
            return self.amt1 * 10800
        if self.unit2 == "second('')":
            return self.amt1 * 648000
        if self.unit2 == "circle":
            return self.amt1 * 0.5
        if self.unit2 == "quadrant":
            return self.amt1 * 2
        return "invalid_unit2"

    def convert_minute(self):
        if self.unit2 == "degree(º)":
            return self.amt1 * 0.0166666667
        if self.unit2 == "radian(π)":
            return self.amt1 * 9.25925898e-5
        if self.unit2 == "minute(')":
            return self.amt1 * 1
        if self.unit2 == "second('')":
            return self.amt1 * 60
        if self.unit2 == "circle":
            return self.amt1 * 0.0000462963
        if self.unit2 == "quadrant":
            return self.amt1 * 0.0001851852
        return "invalid_unit2"

    def convert_second(self):
        if self.unit2 == "degree(º)":
            return self.amt1 * 0.0002777778
        if self.unit2 == "radian(π)":
            return self.amt1 * 1.54319816e-6
        if self.unit2 == "minute(')":
            return self.amt1 * 0.0166666667
        if self.unit2 == "second('')":
            return self.amt1 * 1
        if self.unit2 == "circle":
            return self.amt1 * 7.716049382e-7
        if self.unit2 == "quadrant":
            return self.amt1 * 0.0000030864
        return "invalid_unit2"

    def convert_circle(self):
        if self.unit2 == "degree(º)":
            return self.amt1 * 360
        if self.unit2 == "radian(π)":
            return self.amt1 * 2
        if self.unit2 == "minute(')":
            return self.amt1 * 21600
        if self.unit2 == "second('')":
            return self.amt1 * 1296000
        if self.unit2 == "circle":
            return self.amt1 * 1
        if self.unit2 == "quadrant":
            return self.amt1 * 4
        return "invalid_unit2"

    def convert_quadrant(self):
        if self.unit2 == "degree(º)":
            return self.amt1 * 90
        if self.unit2 == "radian(π)":
            return self.amt1 * 0.5
        if self.unit2 == "minute(')":
            return self.amt1 * 5400
        if self.unit2 == "second('')":
            return self.amt1 * 324000
        if self.unit2 == "circle":
            return self.amt1 * 0.25
        if self.unit2 == "quadrant":
            return self.amt1 * 1
        return "invalid_unit2"
