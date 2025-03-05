from oled import *
from iotbit import *
#from microbit import *
from rtc1307 import *
from bme280 import *
#from sonar import *
#from uvlevel import *
#from soilhumidity import *
#from waterlevel import *
#from dustlevel import *
#from pir import *

class Main:
    def __init__(self,api_key = "SHOHONPIT460Q0ZH",ssid =  "O2 Internet na doma E9FC",pw = "D7160C37712D"):
        self._api_key = api_key
        #Inicializuj triedy
        self._rtc = RTC1307()
        self._display = OLED1306()
        self._display.set_clear()
        self._iotbit = ESP8266_IoT()
        response = self._iotbit.connect_wifi(ssid, pw)
        self._bme = BME280()


    # Získa hodnotu zo zoznamu podľa zadaného indexu
    # Rok:    index = 0
    # Mesiac: index = 1
    # Deň:    index = 2 --> Deň v týždni (nepoužíva sa)
    # Hodina: index = 3
    # Minuta: index = 4
    # Sekunda:index = 5
    # interval = 5 znamena že kazdych 5 sekúnd sa pošlú data
    def send_data(self,interval = 5, index = 5):
        while True:
            if self._rtc.get_value_by_index(index) % interval == 0:
                #Testovanie
                #Príklad merania teploty, vlhkosti a tlaku
                upload_response = self._iotbit.upload_data_thingspeak(self._api_key,self._bme.get_temperature(),self._bme.get_humidity(),self._bme.get_pressure())
                self._display.set_text(0, 0, "{}".format(upload_response))

app = Main()
app.send_data()
