class LengthConversion(object):
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

        if self.unit1 == "meter(m)":
            return self.convert_meter()
        elif self.unit1 == "kilometer(km)":
            return self.convert_kilometer()
        elif self.unit1 == "decimeter(dm)":
            return self.convert_decimeter()
        elif self.unit1 == "centimeter(cm)":
            return self.convert_centimeter()
        elif self.unit1 == "milimeter(mm)":
            return self.convert_milimeter()
        elif self.unit1 == "micrometer(μm)":
            return self.convert_micrometer()
        elif self.unit1 == "nanometer(nm)":
            return self.convert_nanometer()
        elif self.unit1 == "mile(mi)":
            return self.convert_mile()
        elif self.unit1 == "yard(yd)":
            return self.convert_yard()
        elif self.unit1 == "foot(ft)":
            return self.convert_foot()
        elif self.unit1 == "inch(in)":
            return self.convert_inch()
        elif self.unit1 == "light year(ly)":
            return self.convert_lightyear()

        return "invalid_unit1"

    def convert_meter(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 1
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.001
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 10
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 100
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 1000
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 1000000
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 1000000000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.0006213712
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 1.0936132983
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 3.280839895
        elif self.unit2 == "inch(in)":
            return self.amt1 * 39.37007874
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-16
        return "invalid_unit2"

    def convert_kilometer(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 1000
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 10000
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 100000
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 1000000
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 1000000000
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 1000000000000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.6213711922
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 1093.6132983
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 3280.839895
        elif self.unit2 == "inch(in)":
            return self.amt1 * 39370.07874
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-13
        return "invalid_unit2"

    def convert_decimeter(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.1
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.0001
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 10
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 100
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 100000
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 100000000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.0000621371
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 0.1093613298
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 0.3280839895
        elif self.unit2 == "inch(in)":
            return self.amt1 * 3.937007874
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-17
        return "invalid_unit2"

    def convert_centimeter(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.01
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.00001
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 0.1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 10
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 10000
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 10000000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.0000062137
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 0.010936133
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 0.032808399
        elif self.unit2 == "inch(in)":
            return self.amt1 * 0.3937007874
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-18
        return "invalid_unit2"

    def convert_milimeter(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.001
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.000001
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 0.01
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 0.1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 1000
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 1000000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 6.213711922e-7
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 0.0010936133
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 0.0032808399
        elif self.unit2 == "inch(in)":
            return self.amt1 * 0.0393700787
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-19
        return "invalid_unit2"

    def convert_micrometer(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.000001
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 1.0e-9
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 0.00001
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 0.0001
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 0.001
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 1000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 6.213711922e-10
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 0.0000010936
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 0.0000032808
        elif self.unit2 == "inch(in)":
            return self.amt1 * 0.0000393701
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-22
        return "invalid_unit2"

    def convert_nanometer(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 9.999999999e-10
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 1.0e-12
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 1.0e-8
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 1.0e-7
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 0.000001
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 0.001
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 1
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 6.213711922e-13
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 1.093613298e-9
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 3.280839895e-9
        elif self.unit2 == "inch(in)":
            return self.amt1 * 3.937007874e-8
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.057000834e-25
        return "invalid_unit2"

    def convert_mile(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 1609.344
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 1.609344
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 16093.44
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 160934.4
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 1609344
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 1609344000
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 1609344000000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 1
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 1760
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 5280
        elif self.unit2 == "inch(in)":
            return self.amt1 * 63360
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1.70107795e-13
        return "invalid_unit2"

    def convert_yard(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.9144
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.0009144
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 9.144
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 91.44
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 914.4
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 914400
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 914400000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.0005681818
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 1
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 3
        elif self.unit2 == "inch(in)":
            return self.amt1 * 36
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 9.665215626e-17
        return "invalid_unit2"

    def convert_foot(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.3048
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.0003048
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 3.048
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 30.48
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 304.8
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 304800
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 304800000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.0001893939
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 0.3333333333
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 1
        elif self.unit2 == "inch(in)":
            return self.amt1 * 12
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 3.221738542e-17
        return "invalid_unit2"

    def convert_inch(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 0.0254
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 0.0000254
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 0.254
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 2.54
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 25.4
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 25400
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 25400000
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 0.0000157828
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 0.0277777778
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 0.0833333333
        elif self.unit2 == "inch(in)":
            return self.amt1 * 1
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 2.684782118e-18
        return "invalid_unit2"

    def convert_lightyear(self):
        if self.unit2 == "meter(m)":
            return self.amt1 * 9460730472580044
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 9460730472580
        elif self.unit2 == "decimeter(dm)":
            return self.amt1 * 94607304725800430
        elif self.unit2 == "centimeter(cm)":
            return self.amt1 * 946073047258004200
        elif self.unit2 == "milimeter(mm)":
            return self.amt1 * 9460730472580043000
        elif self.unit2 == "micrometer(μm)":
            return self.amt1 * 9.460730472e21
        elif self.unit2 == "nanometer(nm)":
            return self.amt1 * 9.460730472e24
        elif self.unit2 == "mile(mi)":
            return self.amt1 * 5878625373183
        elif self.unit2 == "yard(yd)":
            return self.amt1 * 10346380656802248
        elif self.unit2 == "foot(ft)":
            return self.amt1 * 31039141970406748
        elif self.unit2 == "inch(in)":
            return self.amt1 * 372469703644879100
        elif self.unit2 == "light year(ly)":
            return self.amt1 * 1
        return "invalid_unit2"
