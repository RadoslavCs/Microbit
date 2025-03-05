"""Základný popis
    Senzor vlhkosti pôdy, vracia hodnotu v percentách (0-100 %).
    Args: RJ_pin (pin): Pripojený port
    Vráti: Percento obsahu vody
  """
class SoilHumidity:
    def __init__(self, pin):
        self.__pin = pin

    def get_soilhumidity(self):
        __value = self.__pin.read_analog()
        # Úprava vzorca na zaistenie správnej škály hodnôt od 0 do 100 %
        value = ((__value - 0) * (100 - 0)) / (1023 - 0)
        return value
