from oled import *
#from iotbit import *
from microbit import *
#from rtc1307 import *
from sensors import *

api_key = "SHOHONPIT460Q0ZH"
#ssid =  "O2 Internet na doma E9FC"
#pw = "D7160C37712D"
ssid =  "Test"
pw = "12345678"
display = OLED1306()
display.set_clear()
#_iotbit = ESP8266_IoT()

#response = _iotbit.connect_wifi(ssid, pw)
#_rtc = RTC1307()

#DustLevel
d = DustLevel(pin1, pin2)
while True:
    display.set_text(0, 0,"dust level: {} µg/m³".format(d.get_dust()))
    sleep(500)

#WaterLevel
"""
wl = WaterLevel(pin1)
while True:
    display.set_text(0, 0,"wather level: {} cm".format(wl.get_waterlevel()))
"""

#SoilHumidity
"""
sh = SoilHumidity(pin1)
while True:
    display.set_text(0, 0,"Soil humidity : {} %".format(sh.get_soilhumidity()))
"""

#NoiseLevel
"""
n = NoiseLevel(pin1)
while True:
    display.set_text(0, 0,"Noise Level: {}".format(n.get_noise()))
    sleep(200)
"""

#LightSensor
"""
light = LightLevel(pin1)
while True:
    display.set_text(0, 0,"Light intensity: {}".format(light.get_intensity()))
    sleep(500)
"""
#PIR
"""
sensor = PIR(pin1)
while True:
    if sensor.is_detection():
        display.set_clear()
        display.set_text(0, 0,"Pohyb detekovany")
    else:
        display.set_clear()
        display.set_text(0, 0,"Bez pohybu")
"""
#BME280
"""
bme = BME280()
while True:
    temp = bme.get_temperature()
    hum = bme.get_humidity()
    tlak = bme.get_pressure()
    display.set_text(0, 0,"Teplota: {:.2f} °C".format(temp))
    display.set_text(0, 1,"Vlhkost: {:.2f} %".format(hum))
    display.set_text(0, 2,"Tlak: {:.2f} Pa".format(tlak))
    sleep(500)
"""
# Inicializácia senzora na pine P1
"""
sonar = SonarBit(pin1)
while True:
    vzdialenost = sonar.get_distance()
    if vzdialenost > 0:
       display.set_text(0, 0, "{} cm".format(vzdialenost))
    else:
        display.set_text(0, 0, "-")
    sleep(500)
"""

#Posleme data na thingspeak:
"""
while True:
    if _rtc.get_value_by_index(5) % 5 == 0:
        upload_response = _iotbit.upload_data_thingspeak(api_key,_rtc.get_value_by_index(5))
        display.set_text(0, 0, "{}".format(upload_response))

set_time(self, y, m, d, hh, mm, ss)
_rtc.set_time(2000, 1, 1, 0, 0, 0)  # Nastaví čas na 1.1.2000 00:00:00
_rtc.set_time(2025, 03, 1, 20, 20, 10)
_rtc.clear_time()
while True:
    display.set_text(0, 0, "{}:{}".format(_rtc.get_value_by_index(4),_rtc.get_value_by_index(5)))
    sleep(1000)
"""

