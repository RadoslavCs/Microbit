from microbit import i2c
from microbit import *

RTC_ADDR = 0x68

class RTC1307:
    def __init__(self):
        self.address = RTC_ADDR

    def bcd2bin(self, v):
        return v - 6 * (v >> 4)

    def bin2bcd(self, v):
        return v + 6 * (v // 10)

    def get_time(self):
        i2c.write(self.address, b'\x00')
        value = i2c.read(self.address, 7)
        ss = self.bcd2bin(value[0] & 0x7F)
        mm = self.bcd2bin(value[1])
        hh = self.bcd2bin(value[2])
        d = self.bcd2bin(value[4])
        m = self.bcd2bin(value[5])
        y = self.bcd2bin(value[6]) + 2000
        return [y, m, d, hh, mm, ss]

    def set_time(self, y, m, d, hh, mm, ss):
        value = []
        value.append(self.bin2bcd(ss))
        value.append(self.bin2bcd(mm))
        value.append(self.bin2bcd(hh))
        value.append(self.bin2bcd(0))  # Deň v týždni (nepoužíva sa)
        value.append(self.bin2bcd(d))
        value.append(self.bin2bcd(m))
        value.append(self.bin2bcd(y % 100))  # Uloží len posledné dve číslice roku
        i2c.write(self.address, b'\x00' + bytearray(value))

    # Nastavíme všetky hodnoty na nulu (resetovanie času)
    def clear_time(self):
        value = [0, 0, 0, 0, 0, 0, 0]  # Nulovanie sekúnd, minút, hodín, dňa, mesiaca, roka
        i2c.write(self.address, b'\x00' + bytearray(value))

    # Získa hodnotu zo zoznamu podľa zadaného indexu
    # Rok:    index = 0
    # Mesiac: index = 1
    # Deň:    index = 2
    # Hodina: index = 3
    # Minuta: index = 4
    # Sekunda:index = 5
    def get_value_by_index(self, index):
        time_values = self.get_time()
        if 0 <= index < len(time_values):
            return time_values[index]
        else:
            return None  # Ak je index mimo rozsah
