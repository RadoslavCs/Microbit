from oled import *
from iotbit import *
from microbit import *
from rtc1307 import *

api_key = "SHOHONPIT460Q0ZH"
#ssid =  "O2 Internet na doma E9FC"
#pw = "D7160C37712D"
ssid =  "Test"
pw = "12345678"
display = OLED1306()
display.set_clear()
_iotbit = ESP8266_IoT()

response = _iotbit.connect_wifi(ssid, pw)
_rtc = RTC1307()
while True:
    if _rtc.get_value_by_index(5) % 5 == 0:
        upload_response = _iotbit.upload_data_thingspeak(api_key,_rtc.get_value_by_index(5))
        display.set_text(0, 0, "{}".format(upload_response))

#set_time(self, y, m, d, hh, mm, ss)
#_rtc.set_time(2000, 1, 1, 0, 0, 0)  # Nastaví čas na 1.1.2000 00:00:00
#_rtc.set_time(2025, 03, 1, 20, 20, 10)
#_rtc.clear_time()


#while True:
#    display.set_text(0, 0, "{}:{}".format(_rtc.get_value_by_index(4),_rtc.get_value_by_index(5)))
#    sleep(1000)


