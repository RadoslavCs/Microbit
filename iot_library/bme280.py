from microbit import *
import utime
import time
import ustruct


# Definovanie adresy senzora BME280
BME280_I2C_ADDR = 0x76 # Zvyčajne 0x76 alebo 0x77, podľa senzora

"""Základný popis
    Senzor BME280 meria teplotu, vlhkosť a atmosférický tlak
    Vráti:
        temperature – teplota v °C
        humidity – vlhkosť 0-100%
        pressure – tlak v Pa
        altitude – nadmorská výška v metroch (vypočítané na základe tlaku)
"""
class BME280:
    def __init__(self):
        # Nastavenie parametrov zo senzora
        self._T1 = self.__g2r(0x88)
        self._T2 = self.__short(self.__g2r(0x8A))
        self._T3 = self.__short(self.__g2r(0x8C))
        self._P1 = self.__g2r(0x8E)
        self._P2 = self.__short(self.__g2r(0x90))
        self._P3 = self.__short(self.__g2r(0x92))
        self._P4 = self.__short(self.__g2r(0x94))
        self._P5 = self.__short(self.__g2r(0x96))
        self._P6 = self.__short(self.__g2r(0x98))
        self._P7 = self.__short(self.__g2r(0x9A))
        self._P8 = self.__short(self.__g2r(0x9C))
        self._P9 = self.__short(self.__g2r(0x9E))
        self._H1 = self.__gr(0xA1)
        self._H2 = self.__short(self.__g2r(0xE1))
        self._H3 = self.__gr(0xE3)
        a = self.__gr(0xE5)
        self._H4 = (self.__gr(0xE4) << 4) + (a % 16)
        self._H5 = (self.__gr(0xE6) << 4) + (a >> 4)
        self._H6 = self.__gr(0xE7)
        if self._H6 > 127:
            self._H6 -= 256
        # Nastavenie režimu senzora
        self.__sr(0xF2, 0x04)
        self.__sr(0xF4, 0x2F)
        self.__sr(0xF5, 0x0C)
        self.__T = 0
        self.__P = 0
        self._H = 0

    def __short(self, dat):
        if dat > 32767:
            return dat - 65536
        else:
            return dat

    # Nastavenie registru
    def __sr(self, reg, dat):
        i2c.write(BME280_I2C_ADDR, bytearray([reg, dat]))

    # Čítanie jedného registru
    def __gr(self, reg):
        i2c.write(BME280_I2C_ADDR, bytearray([reg]))
        t = i2c.read(BME280_I2C_ADDR, 1)
        return t[0]

    # Čítanie dvoch registrov
    def __g2r(self, reg):
        i2c.write(BME280_I2C_ADDR, bytearray([reg]))
        t = i2c.read(BME280_I2C_ADDR, 2)
        return t[0] + t[1] * 256

    def __get(self):
        # Čítanie surových údajov a ich výpočet
        adc_T = (self.__gr(0xFA) << 12) + (self.__gr(0xFB) << 4) + (self.__gr(0xFC) >> 4)
        var1 = (((adc_T >> 3) - (self._T1 << 1)) * self._T2) >> 11
        var2 = (((((adc_T >> 4) - self._T1) * ((adc_T >> 4) - self._T1)) >> 12) * self._T3) >> 14
        t = var1 + var2
        self.__T = ((t * 5 + 128) >> 8) / 100
        # Výpočet tlaku
        var1 = (t >> 1) - 64000
        var2 = (((var1 >> 2) * (var1 >> 2)) >> 11) * self._P6
        var2 = var2 + ((var1 * self._P5) << 1)
        var2 = (var2 >> 2) + (self._P4 << 16)
        var1 = (((self._P3 * ((var1 >> 2) * (var1 >> 2)) >> 13) >> 3) + (((self._P2) * var1) >> 1)) >> 18
        var1 = ((32768 + var1) * self._P1) >> 15
        if var1 == 0:
            return  # Aby sa predišlo výnimke spôsobenej delením nulou
        adc_P = (self.__gr(0xF7) << 12) + (self.__gr(0xF8) << 4) + (self.__gr(0xF9) >> 4)
        p = ((1048576 - adc_P) - (var2 >> 12)) * 3125
        if p < 0x80000000:
            p = (p << 1) // var1
        else:
            p = (p // var1) * 2
        var1 = (self._P9 * (((p >> 3) * (p >> 3)) >> 13)) >> 12
        var2 = ((p >> 2) * self._P8) >> 13
        self.__P = p + ((var1 + var2 + self._P7) >> 4)
        # Čítanie vlhkosti
        adc_H = (self.__gr(0xFD) << 8) + self.__gr(0xFE)
        var1 = t - 76800
        var2 = (((adc_H << 14) - (self._H4 << 20) - (self._H5 * var1)) + 16384) >> 15
        var1 = var2 * (((((((var1 * self._H6) >> 10) * (((var1 * self._H3) >> 11) + 32768)) >> 10) + 2097152) * self._H2 + 8192) >> 14)
        var2 = var1 - (((((var1 >> 15) * (var1 >> 15)) >> 7) * self._H1) >> 4)
        if var2 < 0:
            var2 = 0
        if var2 > 419430400:
            var2 = 419430400
        self._H = (var2 >> 12) / 1024
        return [self.__T, self.__P, self._H]

    # Získanie teploty v °C
    def get_temperature(self):
        """
        Čítanie teploty v °C
        """
        self.__get()
        return self.__T

    # Získanie vlhkosti v %
    def get_humidity(self):
        """
        Čítanie vlhkosti v %
        """
        self.__get()
        return self._H

    # Získanie tlaku v Pa
    def get_pressure(self):
        """
        Čítanie tlaku v Pa
        """
        self.__get()
        return self.__P


