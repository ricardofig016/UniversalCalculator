class CurrencyConversion(object):
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

        if self.unit1 == "USD(US Dollar)":
            return self.convert_usd()

        if self.unit1 == "EUR(Euro)":
            return self.convert_eur()

        if self.unit1 == "AUD(Australian Dollar)":
            return self.convert_aud()

        if self.unit1 == "CAD(Canadian Dollar)":
            return self.convert_cad()

        if self.unit1 == "CHF(Swiss Franc)":
            return self.convert_chf()

        if self.unit1 == "CNY(Chinese Yuan)":
            return self.convert_cny()

        if self.unit1 == "GBP(British Pound Strerling)":
            return self.convert_gbp()

        if self.unit1 == "INR(Indian Rupee)":
            return self.convert_inr()

        if self.unit1 == "JPY(Japanese Yen)":
            return self.convert_jpy()

        if self.unit1 == "MXN(Mexican Peso)":
            return self.convert_mxp()

        return "invalid_unit1"

    def convert_usd(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 1
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.897085
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 1.473753
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 1.317538
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.865403
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 7.1768
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.778032
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 82.041653
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 140.3118
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 16.820158
        return "invalid_unit2"

    def convert_eur(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 1.1147215704
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 1
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 1.6428242586
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 1.4686880284
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.9646833912
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 8.0001337666
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.8672890529
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 91.453600272
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 156.40859004
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 18.74979294
        return "invalid_unit2"

    def convert_aud(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 0.6785397553
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.6087078364
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 1
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 0.8940019121
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.5872103399
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 4.8697441159
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.5279256429
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 55.668523151
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 95.207134438
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 11.413145894
        return "invalid_unit2"

    def convert_cad(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 0.7589913915
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.6808797925
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 1.1185658402
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 1
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.6568334272
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 5.4471294187
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.5905195903
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 62.268908373
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 106.49544833
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 12.766355126
        return "invalid_unit2"

    def convert_chf(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 1.1555310069
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 1.0366095334
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 1.7029672881
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 1.5224560118
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 1
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 8.2930149306
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.8990401004
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 94.801673902
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 162.13463554
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 19.436214111
        return "invalid_unit2"

    def convert_cny(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 0.1393378665
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.1249979099
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 0.2053495987
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 0.1835829339
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.1205834076
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 1
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.1084093189
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 11.43150889
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 19.550746851
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 2.3436849292
        return "invalid_unit2"

    def convert_gbp(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 1.2852941781
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 1.1530181278
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 1.8942061509
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 1.6934239209
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 1.1122974376
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 9.2242992576
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 1
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 105.44765897
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 180.34193966
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 21.618851153
        return "invalid_unit2"

    def convert_inr(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 0.0121889304
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.0109345066
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 0.0179634728
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 0.016059379
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.010548337
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 0.0874775158
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.0094833779
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 1
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 1.7102507674
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 0.2050197355
        return "invalid_unit2"

    def convert_jpy(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 0.0071269843
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.0063935107
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 0.0105034145
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 0.0093900727
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.0061677136
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 0.0511489411
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.0055450219
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 0.5847095754
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 1
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 0.1198770025
        return "invalid_unit2"

    def convert_mxp(self):
        if self.unit2 == "USD(US Dollar)":
            return self.amt1 * 0.0594524736
        if self.unit2 == "EUR(Euro)":
            return self.amt1 * 0.0533339223
        if self.unit2 == "AUD(Australian Dollar)":
            return self.amt1 * 0.0876182614
        if self.unit2 == "CAD(Canadian Dollar)":
            return self.amt1 * 0.0783308932
        if self.unit2 == "CHF(Swiss Franc)":
            return self.amt1 * 0.051450349
        if self.unit2 == "CNY(Chinese Yuan)":
            return self.amt1 * 0.4266785128
        if self.unit2 == "GBP(British Pound Strerling)":
            return self.amt1 * 0.046255927
        if self.unit2 == "INR(Indian Rupee)":
            return self.amt1 * 4.8775792118
        if self.unit2 == "JPY(Japanese Yen)":
            return self.amt1 * 8.3418835899
        if self.unit2 == "MXN(Mexican Peso)":
            return self.amt1 * 1
        return "invalid_unit2"
