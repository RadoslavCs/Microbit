ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("O2 Internet na doma E9FC", "D7160C37712D")
if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Happy)
} else {
    basic.showIcon(IconNames.Sad)
}
function getNoiseLevel(pin: AnalogPin): number {
    let level = 0
    let voltage = 0
    let tl = 0
    let h = 0
    let sum_l = 0
    let sum_h = 0
    let noise = 0

    // Priemerná hodnota napätia zo 1000 meraní
    for (let i = 0; i < 1000; i++) {
        level += pins.analogReadPin(pin)
    }
    level = level / 1000

    // Rozdelenie hodnôt na vysoké a nízke
    for (let j = 0; j < 1000; j++) {
        voltage = pins.analogReadPin(pin)
        if (voltage >= level) {
            h++
            sum_h += voltage
        } else {
            tl++
            sum_l += voltage
        }
    }

    sum_h = h == 0 ? level : sum_h / h
    sum_l = tl == 0 ? level : sum_l / tl
    noise = sum_h - sum_l

    // Mapovanie na dB podľa rozsahov
    if (noise <= 4) {
        noise = ((noise - 0) * (50 - 30)) / (4 - 0) + 30
    } else if (noise <= 8) {
        noise = ((noise - 4) * (55 - 50)) / (8 - 4) + 50
    } else if (noise <= 14) {
        noise = ((noise - 9) * (60 - 55)) / (14 - 9) + 55
    } else if (noise <= 32) {
        noise = ((noise - 15) * (70 - 60)) / (32 - 15) + 60
    } else if (noise <= 60) {
        noise = ((noise - 33) * (75 - 70)) / (60 - 33) + 70
    } else if (noise <= 100) {
        noise = ((noise - 61) * (80 - 75)) / (100 - 61) + 75
    } else if (noise <= 150) {
        noise = ((noise - 101) * (85 - 80)) / (150 - 101) + 80
    } else if (noise <= 231) {
        noise = ((noise - 151) * (90 - 85)) / (231 - 150) + 85
    } else {
        noise = ((noise - 231) * (120 - 90)) / (1023 - 231) + 90
    }

    return noise
}
// Nekonečný cyklus na meranie hluku a odoslanie na ThingSpeak
basic.forever(function () {
    if (RTC_DS1307.getTime(RTC_DS1307.TimeType.SECOND) % 15 == 0) {
        // Použitý pin P1 pre čítanie hluku
        let noiseLevel = getNoiseLevel(AnalogPin.P1)
OLED.init(128, 64)
        OLED.clear()
        OLED.writeStringNewLine("Noise Level: " + noiseLevel + " dB")
        ESP8266_IoT.connectThingSpeak()
        ESP8266_IoT.setData(
        "SHOHONPIT460Q0ZH",
        noiseLevel
        )
        ESP8266_IoT.uploadData()
        OLED.writeStringNewLine("Data Uploaded")
    }
})
