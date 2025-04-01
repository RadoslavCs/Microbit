# Microbit

DESCRIPTION OF THE DEVELOPED SOFTWARE

The created library and its classes enable easy integration and processing of data from sensors connected to the IoT:bit board with a micro:bit microcontroller. 
The library provides methods for reading data from a wide range of sensors, processing it, and subsequently sending it to the ThingSpeak cloud platform using the ESP8266 Wi-Fi module. 
It offers an interface that allows programmers to easily retrieve measured values without the need for manual sensor parameter configuration or signal processing. 
Each sensor has its own class that encapsulates its functionality, ensuring modularity and code clarity. Each module of the library represents software support for individual hardware components, 
covering everything from sensor data processing to cloud transmission.

Overview of Components, Modules, Classes, and Functionalities of the Developed System:

Micro:bit contains the main module main.py, which includes the Main class. 
This module ensures the integration of all connected devices and the processing of sensor data. It serves as the central control element of the entire system.

IoT:bit utilizes the modules iotbit.py and rtc1307.py, which contain the classes ESP8266_IoT and RTC1307. 
It enables Wi-Fi connectivity via the ESP8266 module, allows data transmission to a cloud platform, and manages time measurement using the RTC1307 module.

OLED Display uses the module oled.py with the OLED1306 class. 
It displays textual and simple graphical information, enabling the visualization of measured sensor values.

Soil Moisture Sensor is implemented in the module soilhumidity.py with the SoilHumidity class. 
This sensor measures soil moisture levels and provides essential data for irrigation systems.

Water Level Sensor is handled by the module waterlevel.py with the WaterLevel class. 
It monitors water level height, which is useful for tank monitoring and irrigation systems.

Dust Sensor is managed by the module dustlevel.py and the DustLevel class. 
It measures the concentration of dust particles in the air, which is important for air quality monitoring and pollution detection.

Sonar:bit uses the module sonar.py with the SonarBit class. 
This ultrasonic sensor measures distance and is mainly used in robotics and automated obstacle detection systems.

BME280 Sensor is implemented in the module bme280.py with the BME280 class. 
It provides accurate measurements of temperature, humidity, and air pressure and is used in applications focused on environmental monitoring.

Motion Sensor (PIR) works with the module pir.py and the PIR class. 
It detects movement in its surroundings and is often used in security systems or automated lighting.

Noise Sensor utilizes the module noise.py with the NoiseLevel class. 
It measures noise levels in the environment, allowing for sound pollution monitoring.

UV Radiation Sensor uses the module uvlevel.py with the UV class. 
This sensor measures ultraviolet radiation intensity, which is essential for monitoring sunlight exposure and protection against harmful UV rays.