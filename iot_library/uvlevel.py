"""Základný popis
    Senzor intenzity ultrafialového žiarenia
    Args: RJ_pin (pin): Pripojovací port
    Vráti: Hodnotu intenzity UV žiarenia v rozsahu 0-15
"""
class UV:
    def __init__(self, pin):
        self.__pin = pin

    def get_intensity(self):
        __value = self.__pin.read_analog()
        value = ((__value - 0) * (15 - 0)) / (625 - 0) + 0
        return value
