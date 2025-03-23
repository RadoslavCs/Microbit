let uvLight  = 0
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("O2 Internet na doma E9FC", "D7160C37712D")
if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Happy)
} else {
    basic.showIcon(IconNames.Happy)
}
basic.forever(function () {
    while (true) {
        if (RTC_DS1307.getTime(RTC_DS1307.TimeType.SECOND) % 15 == 0) {
            OLED.init(128, 64)
            OLED.clear()
            uvLight = Environment.UVLevel(AnalogPin.P1)
            ESP8266_IoT.connectThingSpeak()
            ESP8266_IoT.setData(
            "SHOHONPIT460Q0ZH",
                uvLight
            )
            ESP8266_IoT.uploadData()
            OLED.writeStringNewLine("UV Level: " + uvLight + ".")
        }
    }
})
