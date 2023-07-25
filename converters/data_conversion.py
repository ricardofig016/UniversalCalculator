class DataConversion(object):
    def __init__(self, amt1_str, unit1, unit2) -> None:
        try:
            self.amt1 = float(amt1_str)
        except ValueError:
            self.amt1 = "invalid_amt1"

        self.unit1 = unit1
        self.unit2 = unit2

    def convert(self):
        bit_amt = "invalid_bit_amt"

        if self.amt1 == "invalid_amt1":
            return self.amt1
        elif self.unit1 == "bit(b)":
            bit_amt = self.amt1 * 1
        elif self.unit1 == "Byte(B)":
            bit_amt = self.amt1 * 8
        elif self.unit1 == "word":
            bit_amt = self.amt1 * 16
        elif self.unit1 == "block":
            bit_amt = self.amt1 * 4096
        elif self.unit1 == "kiloByte(kB)":
            bit_amt = self.amt1 * 8192
        elif self.unit1 == "megaByte(MB)":
            bit_amt = self.amt1 * 8388608
        elif self.unit1 == "gigaByte(GB)":
            bit_amt = self.amt1 * 8589934592
        elif self.unit1 == "teraByte(TB)":
            bit_amt = self.amt1 * 8796093022208
        elif self.unit1 == "petaByte(PB)":
            bit_amt = self.amt1 * 9007199254740640

        return self.convert_bit(bit_amt)

    def convert_bit(self, bit_amt):
        if self.unit2 == "bit(b)":
            return bit_amt * 1
        if self.unit2 == "Byte(B)":
            return bit_amt * 0.125
        if self.unit2 == "word":
            return bit_amt * 0.0625
        if self.unit2 == "block":
            return bit_amt * 0.0002441406
        if self.unit2 == "kiloByte(kB)":
            return bit_amt * 0.0001220703
        if self.unit2 == "megaByte(MB)":
            return bit_amt * 1.192092895e-7
        if self.unit2 == "gigaByte(GB)":
            return bit_amt * 1.164153218e-10
        if self.unit2 == "teraByte(TB)":
            return bit_amt * 1.136868377e-13
        if self.unit2 == "petaByte(PB)":
            return bit_amt * 1.110223024e-16
        return "invalid_unit2"
