import utime
"""Základný popis
    Knižnica pre senzor prachu
    Argumenty: RJ_pin (pin): Pripojený port
    Vráti: Hodnotu prachu v µg/m³
"""
class DustLevel:
    def __init__(self, pin_vo, pin_vLED):
        self.__pin_vo = pin_vo
        self.__pin_vLED = pin_vLED

    def get_dust(self):
        __voltage = 0
        __dust = 0
        self.__pin_vLED.write_digital(0)
        utime.sleep_us(160)
        __voltage = self.__pin_vo.read_analog() * 6.5
        utime.sleep_us(100)
        self.__pin_vLED.write_digital(1)
        __voltage = ((__voltage - 0) * 3100) / (1023 - 0) + 0
        __dust = (__voltage - 380) * 5 / 29
        if __dust < 0:
            __dust = 0
        return __dust
