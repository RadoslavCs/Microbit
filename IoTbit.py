from microbit import *
from os import *

ssid = "O2 Internet na doma E9FC"
pw = "D7160C37712D"

uart.init(baudrate=115200, tx=pin8, rx=pin12)

# Send the AT command
def send_at_command(command):
    uart.write("{}\r\n".format(command))
    sleep(100)
    response_bytes = uart.read()  # uart.readline()
    if response_bytes is None:
        return "No response"
    response_str = response_bytes.decode("utf-8").strip()
    return response_str

send_at_command('AT+CWJAP="{}","{}"'.format(ssid, pw))
sleep(1000)

at_response = send_at_command('AT+CIPSTART="TCP","api.thingspeak.com",80')
sleep(1000)

strData = "GET https://api.thingspeak.com/update?api_key=SHOHONPIT460Q0ZH&field1=95"
send_at_command("AT+CIPSEND={}".format(len(strData)+2))
sleep(300)
at_response = send_at_command(strData)
sleep(300)
display.show("{}".format(at_response))

