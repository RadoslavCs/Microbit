"""Základný popis
    Snímač hladiny vody, vracia hodnotu v percentách od 0 do 100
    Argumenty: RJ_pin (pin): Pripojený port
    Vráti: Hladinu vody v centimetroch na základe percentuálnej hodnoty (value) a predpokladanej výšky nádrže (high)
    """
class WaterLevel:
    def __init__(self, pin):
        self.__pin = pin

    def get_waterlevel(self, high = 4):
        __value = self.__pin.read_analog()
        percent = ((__value - 0) * (100 - 0)) / (700 - 0) + 0
        height_in_cm = (percent / 100) * high  # Predpokladaná výška nádrže v cm
        return height_in_cm
