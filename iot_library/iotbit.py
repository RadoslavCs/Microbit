from microbit import *
from os import *
import time

class ESP8266_IoT:
    def __init__(self, tx_pin=pin8, rx_pin=pin12, baudrate=115200):
        # Initialize UART with given parameters
        uart.init(baudrate=baudrate, tx=tx_pin, rx=rx_pin)

    # Send the AT command
    def send_at_command(self, command):
        uart.write("{}\r\n".format(command))
        response_bytes = uart.read()  # uart.readline()
        if response_bytes is None:
            return "No response"
        return response_bytes.decode("utf-8").strip()

    # Sends an AT command to connect to Wi-Fi with the given SSID and password
    # returns response.
    def connect_wifi(self, ssid, pw):
        return self.send_at_command('AT+CWJAP="{}","{}"'.format(ssid, pw))

    # Sends an AT command to establish a TCP connection to api.thingspeak.com
    # returns the response
    def connect_thingspeak(self):
        return self.send_at_command('AT+CIPSTART="TCP","api.thingspeak.com",80')

    # Uploads the given values to ThingSpeak and returns the response
    def upload_data_thingspeak(self,api_key, value1=0,value2=0,value3=0,value4=0,value5=0,value6=0,value7=0,value8=0):
        self.connect_thingspeak()
        strData = "GET https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}&field7={}&field8={}".format(api_key,value1,value2,value3,value4,value5,value6,value7,value8)
        at_response = self.send_at_command("AT+CIPSEND={}".format(len(strData) + 2))
        sleep(100)
        at_response = self.send_at_command(strData)
        return at_response


