class AreaConversion(object):
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

        if self.unit1 == "square meter(m²)":
            return self.convert_meter()
        elif self.unit1 == "square kilometer(km²)":
            return self.convert_kilometer()
        elif self.unit1 == "square centimeter(cm²)":
            return self.convert_centimeter()
        elif self.unit1 == "square milimeter(mm²)":
            return self.convert_milimeter()
        elif self.unit1 == "square micrometer(μm²)":
            return self.convert_micrometer()
        elif self.unit1 == "hectare(ha)":
            return self.convert_hectare()
        elif self.unit1 == "acre(ac)":
            return self.convert_acre()
        elif self.unit1 == "square mile(mi²)":
            return self.convert_mile()
        elif self.unit1 == "square yard(yd²)":
            return self.convert_yard()
        elif self.unit1 == "square foot(ft²)":
            return self.convert_foot()
        elif self.unit1 == "square inch(in²)":
            return self.convert_inch()

        return "invalid_unit1"

    def convert_meter(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 1
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 0.000001
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 10000
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 1000000
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 1000000000000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 0.0001
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 0.0002471054
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 3.861021585e-7
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 1.1959900463
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 10.763910417
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 1550.0031
        return "invalid_unit2"

    def convert_kilometer(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 1000000
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 1
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 10000000000
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 1000000000000
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 1000000000000000000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 100
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 247.10538147
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 0.3861021585
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 1195990.0463
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 10763910.417
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 1550003100
        return "invalid_unit2"

    def convert_centimeter(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 0.0001
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 1.0e-10
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 1
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 100
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 100000000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 1.0e-8
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 2.471053814e-8
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 3.861021585e-11
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 0.000119599
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 0.001076391
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 0.15500031
        return "invalid_unit2"

    def convert_milimeter(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 0.000001
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 1.0e-12
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 0.01
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 1
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 1000000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 1.0e-10
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 2.471053814e-10
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 3.861021585e-13
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 0.000001196
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 0.0000107639
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 0.0015500031
        return "invalid_unit2"

    def convert_micrometer(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 1.0e-12
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 1.0e-18
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 1.0e-8
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 0.000001
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 1
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 1.0e-16
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 2.471053814e-16
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 3.861021585e-19
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 1.195990046e-12
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 1.076391041e-11
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 1.5500031e-9
        return "invalid_unit2"

    def convert_hectare(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 10000
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 0.01
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 100000000
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 10000000000
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 10000000000000000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 1
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 2.4710538147
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 0.0038610216
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 11959.900463
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 107639.10417
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 15500031
        return "invalid_unit2"

    def convert_acre(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 4046.8564224
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 0.0040468564
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 40468564.224
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 4046856422.4
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 4046856422399924
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 0.4046856422
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 1
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 0.0015625
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 4840
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 43560
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 6272640
        return "invalid_unit2"

    def convert_mile(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 2589988.1103
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 2.5899881103
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 25899881103
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 2589988110336
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 2589988110335972400
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 258.99881103
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 640
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 1
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 3097600
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 27878400
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 4014489600
        return "invalid_unit2"

    def convert_yard(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 0.83612736
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 8.361273599e-7
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 8361.2736
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 836127.36
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 836127360000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 0.0000836127
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 0.0002066116
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 3.228305785e-7
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 1
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 9
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 1296
        return "invalid_unit2"

    def convert_foot(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 0.09290304
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 9.290303999e-8
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 929.0304
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 92903.04
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 92903040000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 0.0000092903
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 0.0000229568
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 3.587006427e-8
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 0.1111111111
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 1
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 144
        return "invalid_unit2"

    def convert_inch(self):
        if self.unit2 == "square meter(m²)":
            return self.amt1 * 0.00064516
        elif self.unit2 == "square kilometer(km²)":
            return self.amt1 * 6.4516e-10
        elif self.unit2 == "square centimeter(cm²)":
            return self.amt1 * 6.4516
        elif self.unit2 == "square milimeter(mm²)":
            return self.amt1 * 645.16
        elif self.unit2 == "square micrometer(μm²)":
            return self.amt1 * 645160000
        elif self.unit2 == "hectare(ha)":
            return self.amt1 * 6.4516e-8
        elif self.unit2 == "acre(ac)":
            return self.amt1 * 1.594225079e-7
        elif self.unit2 == "square mile(mi²)":
            return self.amt1 * 2.490976686e-10
        elif self.unit2 == "square yard(yd²)":
            return self.amt1 * 0.0007716049
        elif self.unit2 == "square foot(ft²)":
            return self.amt1 * 0.0069444444
        elif self.unit2 == "square inch(in²)":
            return self.amt1 * 1
        return "invalid_unit2"
