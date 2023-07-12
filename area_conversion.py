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
            return "invalid_amt1"

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
        elif self.unit1 == "ligh year(ly)":
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
        elif self.unit2 == "ligh year(ly)":
            return self.amt1 * 1.057000834e-16

    def convert_kilometer(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1 * 1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":  # mistake here
            return self.amt1

    def convert_decimeter(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_centimeter(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_milimeter(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_micrometer(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_nanometer(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_mile(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_yard(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_foot(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_inch(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1

    def convert_lightyear(self):
        if self.unit2 == "meter(m)":
            return self.amt1
        elif self.unit2 == "kilometer(km)":
            return self.amt1
        elif self.unit2 == "decimeter(dm)":
            return self.amt1
        elif self.unit2 == "centimeter(cm)":
            return self.amt1
        elif self.unit2 == "milimeter(mm)":
            return self.amt1
        elif self.unit2 == "micrometer(μm)":
            return self.amt1
        elif self.unit2 == "nanometer(nm)":
            return self.amt1
        elif self.unit2 == "mile(mi)":
            return self.amt1
        elif self.unit2 == "yard(yd)":
            return self.amt1
        elif self.unit2 == "foot(ft)":
            return self.amt1
        elif self.unit2 == "inch(in)":
            return self.amt1
        elif self.unit2 == "ligh year(ly)":
            return self.amt1
