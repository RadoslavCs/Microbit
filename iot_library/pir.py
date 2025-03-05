"""Základný popis
        Detekcia infračerveného žiarenia z ľudského tela, detekcia pohybu
        Argumenty: RJ_pin (pin): Pripojený port
"""
class PIR:
    def __init__(self, pin):
        self.__pin = pin

    """     Návratová hodnota:
            boolean: Ak je detekované, vráti True, ak nie, vráti False
    """
    def is_detection(self) -> bool:
        if self.__pin.read_digital():
            return True
        else:
            return False


