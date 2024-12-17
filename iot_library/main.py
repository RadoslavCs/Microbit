from oled import *
from iotbit import *

display = OLED1306()
display.set_clear()
_iotbit = ESP8266_IoT()

response = _iotbit.connect_wifi("O2 Internet na doma E9FC", "D7160C37712D")

upload_response = _iotbit.upload_data_thingspeak(42)

display.set_text(0, 0, upload_response)
