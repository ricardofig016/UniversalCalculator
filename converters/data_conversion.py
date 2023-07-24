class DataConversion(object):
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

        if self.unit1 == "bit(b)":
            return self.convert_bit()

        if self.unit1 == "Byte(B)":
            return self.convert_byte()

        if self.unit1 == "word":
            return self.convert_word()

        if self.unit1 == "block":
            return self.convert_block()

        if self.unit1 == "kiloByte(kB)":
            return self.convert_kilobyte()

        if self.unit1 == "megaByte(MB)":
            return self.convert_megabyte()

        if self.unit1 == "gigaByte(GB)":
            return self.convert_gigabyte()

        if self.unit1 == "teraByte(TB)":
            return self.convert_terabyte()

        if self.unit1 == "petaByte(PB)":
            return self.convert_petabyte()

        return "invalid_unit1"

    def convert_bit(self):
        if self.unit2 == "":
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
