from microbit import *
import time

class SonarBit:
    def __init__(self, pin):
        self.pin = pin

"""Zmeria vzdialenosť v centimetroch a vráti ju."""
    def get_distance(self):
        self.pin.write_digital(0)
        time.sleep_us(2)
        self.pin.write_digital(1)
        time.sleep_us(10)
        self.pin.write_digital(0)

        start_time = running_time()
        while self.pin.read_digital() == 0:
            if running_time() - start_time > 100:
                return -1  # Timeout

        start = running_time()
        while self.pin.read_digital() == 1:
            if running_time() - start_time > 100:
                return -1  # Timeout

        duration = running_time() - start  # Čas návratu v milisekundách
        distance = duration * 34 / 2  # Výpočet vzdialenosti (34 cm/ms rýchlosť zvuku)

        return round(distance, 2)  # Zaokrúhlenie

