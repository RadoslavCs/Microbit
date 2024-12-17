from microbit import *
from os import *

class ESP8266_IoT:
    def __init__(self, tx_pin=pin8, rx_pin=pin12, baudrate=115200):
        # Initialize UART with given parameters
        uart.init(baudrate=baudrate, tx=tx_pin, rx=rx_pin)

    # Send the AT command
    def send_at_command(self, command):
        uart.write("{}\r\n".format(command))
        sleep(100)
        response_bytes = uart.read()  # uart.readline()
        if response_bytes is None:
            return "No response"
        response_str = response_bytes.decode("utf-8").strip()
        return response_str

    # Sends an AT command to connect to Wi-Fi with the given SSID and password
    # returns response.
    def connect_wifi(self, ssid, pw):
        at_response = self.send_at_command('AT+CWJAP="{}","{}"'.format(ssid, pw))
        sleep(1000)
        return at_response

    # Sends an AT command to establish a TCP connection to api.thingspeak.com
    # returns the response
    def connect_thingspeak(self):
        at_response = self.send_at_command('AT+CIPSTART="TCP","api.thingspeak.com",80')
        sleep(1000)
        return at_response

    # Uploads the given value to ThingSpeak and returns the response
    def upload_data_thingspeak(self, value):
        self.connect_thingspeak()
        strData = "GET https://api.thingspeak.com/update?api_key=SHOHONPIT460Q0ZH&field1={}".format(value)
        self.send_at_command("AT+CIPSEND={}".format(len(strData) + 2))
        sleep(300)
        at_response = self.send_at_command(strData)
        return at_response

