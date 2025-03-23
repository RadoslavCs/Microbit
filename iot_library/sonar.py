from microbit import *
from time import sleep_us
from machine import time_pulse_us

"""Základný popis
        Meria vzdialenosť pomocou ultrazvukového senzora Sonar:bit
        Argumenty:
        pin_trig (pin): Pin pre Trig signál
        pin_echo (pin): Pin pre Echo signál
        Vráti: Vzdialenosť v centimetroch
"""
class SonarBit:
    def __init__(self, pin_d):
        self.__pin_e = pin_d
        self.__pin_t = pin_d

    #Zmeria vzdialenosť v centimetroch a vráti ju.
    def get_distance(self):
        self.__pin_e.read_digital()
        self.__pin_t.write_digital(1)
        sleep_us(10)
        self.__pin_t.write_digital(0)
        ts = time_pulse_us(self.__pin_e, 1, 25000)

        vzdialenost = ts * 9 / 6 / 58

        return vzdialenost
