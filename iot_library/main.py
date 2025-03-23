#from oled import *
from iotbit import *
#from rtc1307 import *
#from bme280 import *
#from sonar import *
#from uvlevel import *
#from soilhumidity import *
#from waterlevel import *
#from dustlevel import *
#from pir import *
#from noise import *

from microbit import  display, sleep


class Main:
    def __init__(self,api_key = "SHOHONPIT460Q0ZH",ssid =  "O2 Internet na doma E9FC",pw = "D7160C37712D"):
        try:
            self._api_key = api_key
            #self._rtc = RTC1307()
            #self._display = OLED1306()
            #self._display.set_clear()
            self._iotbit = ESP8266_IoT()
            response = self._iotbit.connect_wifi(ssid, pw)
            #Inicializuj triedy senzorov
            #self._bme = BME280()
            #self._soil = SoilHumidity(pin1)
            #self._sonar = SonarBit(pin1)
            #self._uv = UV(pin1)
            #self._noise = NoiseLevel(pin1)
            #self._water = WaterLevel(pin1)
            #self._dust = DustLevel(pin1,pin2)
            #self._pir = PIR(pin6)
        except Exception as e:
            self._display.set_text(0, 0, "{}".format(e))


    # Získa hodnotu zo zoznamu podľa zadaného indexu
    # Rok:    index = 0
    # Mesiac: index = 1
    # Deň:    index = 2
    # Hodina: index = 3
    # Minuta: index = 4
    # Sekunda:index = 5
    # interval = 15 znamena že kazdych 15 sekúnd sa pošlú data
    def send_data(self,interval = 15, index = 5):
        try:
            while True:
                if self._rtc.get_value_by_index(index) % interval == 0:
                    #Testovanie
                    #t = self._bme.get_temperature()
                    #h = self._bme.get_humidity()
                    #p = self._bme.get_pressure()
                    uv = self._uv.get_intensity()
                    upload_response = self._iotbit.upload_data_thingspeak(self._api_key,uv)
                    display.scroll( "UV Light: {} ".format(uv))
                    #self._display.set_text(0, 0, "Temperature: {} °C".format(t))
                    #self._display.set_text(0, 1, "Humidity: {} %".format(h))
                    #self._display.set_text(0, 2, "Pressure: {} Pa".format(p))
                    #self._display.set_text(0, 3, "ThingSpeak: {}".format(upload_response))
                else:
                    display.scroll( "UV Light: {} ".format(self._rtc.get_value_by_index(index)))

        except Exception as e:
            self._display.set_text(0, 0, "{}".format(e))



    def send_data_v1(self):
        while True:
            uv = 567.8907
            upload_response = self._iotbit.upload_data_thingspeak(self._api_key,uv)
            display.scroll( "UV Light: {} ".format(uv))
            sleep(15000)


app = Main()
app.send_data_v1()



