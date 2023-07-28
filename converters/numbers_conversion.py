class NumbersConversion(object):
    def __init__(self, amt1_str, unit1, unit2) -> None:
        try:
            self.amt1 = str(amt1_str)
            if self.amt1 == "":
                self.amt1 = "invalid_amt1"
        except ValueError:
            self.amt1 = "invalid_amt1"

        self.unit1 = unit1
        self.unit2 = unit2

    def convert(self):
        if self.amt1 == "invalid_amt1":
            return self.amt1

        if self.unit1 == "decimal":
            return self.convert_decimal(self.amt1)
        if self.unit1 == "binary":
            return self.convert_decimal(self.convert_binary_to_decimal(self.amt1))
        if self.unit1 == "hex":
            return self.convert_decimal(self.convert_hex_to_decimal(self.amt1))
        if self.unit1 == "roman":
            return self.convert_decimal(self.convert_roman_to_decimal(self.amt1))

        return "invalid_unit1"

    def convert_decimal(self, amt1_decimal):
        try:
            amt1_decimal = int(amt1_decimal)
        except ValueError:
            return amt1_decimal

        if self.unit2 == "decimal":
            return amt1_decimal
        if self.unit2 == "binary":
            return self.convert_decimal_to_binary(amt1_decimal)
        if self.unit2 == "hex":
            return self.convert_decimal_to_hex(amt1_decimal)
        if self.unit2 == "roman":
            return self.convert_decimal_to_roman(amt1_decimal)

        return "invalid_unit2"

    def convert_binary_to_decimal(self, amt1_binary):
        return int(amt1_binary, 2)

    def convert_hex_to_decimal(self, amt1_hex):
        return int(amt1_hex, 16)

    def convert_decimal_to_binary(self, amt1_decimal):
        return bin(amt1_decimal)

    def convert_decimal_to_hex(self, amt1_decimal):
        return hex(amt1_decimal)

    def convert_decimal_to_roman(self, amt1_decimal):
        if not isinstance(amt1_decimal, int) or not 0 < amt1_decimal < 4000:
            return "invalid amt1"

        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        amt1_roman = ""
        for value, symbol in roman_numerals.items():
            while amt1_decimal >= value:
                amt1_roman += symbol
                amt1_decimal -= value

        return amt1_roman

    def convert_roman_to_decimal(self, roman):
        symbol_value = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        segs = {
            "I": 0,
            "IV": 0,
            "V": 0,
            "IX": 0,
            "X": 0,
            "XL": 0,
            "L": 0,
            "XC": 0,
            "C": 0,
            "CD": 0,
            "D": 0,
            "CM": 0,
            "M": 0,
        }

        order = []

        for i in range(len(roman)):
            if i != 0 and roman[i - 1] + roman[i] in segs:
                segs[roman[i - 1] + roman[i]] += 1
                if len(order[-1]) == 2:
                    return "invalid_amt1"
                segs[roman[i - 1]] -= 1
                order = order[:-1]
                order.append(roman[i - 1] + roman[i])
            elif roman[i] in segs:
                segs[roman[i]] += 1
                order.append(roman[i])
            else:
                return "invalid_amt1"

        if (
            segs["I"] > 3
            or segs["IV"] > 1
            or segs["V"] > 1
            or segs["IX"] > 1
            or segs["X"] > 3
            or segs["XL"] > 1
            or segs["L"] > 1
            or segs["XC"] > 1
            or segs["C"] > 3
            or segs["CD"] > 1
            or segs["D"] > 1
            or segs["CM"] > 1
            or segs["M"] > 3
        ):
            return "invalid_amt1"

        if (
            (segs["I"] > 0 and segs["IV"] > 0)
            or (segs["I"] > 0 and segs["IX"] > 0)
            or (segs["IV"] > 0 and segs["V"] > 0)
            or (segs["IV"] > 0 and segs["IX"] > 0)
            or (segs["V"] > 0 and segs["IX"] > 0)
            or (segs["X"] > 0 and segs["XL"] > 0)
            or (segs["X"] > 0 and segs["XC"] > 0)
            or (segs["XL"] > 0 and segs["L"] > 0)
            or (segs["XL"] > 0 and segs["XC"] > 0)
            or (segs["L"] > 0 and segs["XC"] > 0)
            or (segs["C"] > 0 and segs["CD"] > 0)
            or (segs["C"] > 0 and segs["CM"] > 0)
            or (segs["CD"] > 0 and segs["D"] > 0)
            or (segs["CD"] > 0 and segs["CM"] > 0)
            or (segs["D"] > 0 and segs["CM"] > 0)
        ):
            return "invalid_amt1"

        segs_value = [symbol_value[i] for i in order]
        for i in range(len(segs_value) - 1):
            if segs_value[i] < segs_value[i + 1]:
                return "invalid_amt1"

        return sum(segs_value)
