This github project describes the Device code for a Raspberry Pi using senseHAT. The code gathers the sensor data from the senseHAT and sends them to the Azure IoT Hub using MQTT. The data is then stored to a cosmosDB NoSQL database where it can be used to visualize the data. 

# Table of Contents
- [Overview](https://github.com/Kotik112/D2C-demo/new/master?readme=1#raspberry-pi-and-sensehat-data-monitoring)
- [Hardware Used](https://github.com/Kotik112/D2C-demo/new/master?readme=1#hardware-used)
- [Python script](https://github.com/Kotik112/D2C-demo/new/master?readme=1#python-script)
- [Running the script](https://github.com/Kotik112/D2C-demo/new/master?readme=1#running-the-script)

# Raspberry Pi and SenseHat Data Monitoring
This project uses a Raspberry Pi and a SenseHat to monitor temperature, humidity, and pressure data. The data is then sent to an Azure IoT Hub at a regular interval.

## Hardware Used
![image](https://user-images.githubusercontent.com/88910492/206953219-2890d18d-fc53-4403-8906-6c0f54e26dce.png)

- `Raspberry Pi`: A series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation to promote teaching of basic computer science in schools and in developing countries.
- `SenseHat`: An add-on board for the Raspberry Pi, featuring an 8x8 RGB LED matrix, a five-button joystick and a variety of sensors, including an accelerometer, gyroscope and magnetometer.

## Python Script
The `sense-hat-script.py` script does the following:

#### Import the required modules: 
```
import sense_hat
import azure.iot.device.aio
import time
```
- Define an `INTERVAL` constant, which determines how often the data is sent to the IoT Hub (in seconds). In this project I had it set to 180 seconds.
- Define a `SenseHatManager` class, which provides methods to retrieve the temperature, humidity, and pressure data from the SenseHat.
- Define a `MessagingClient` class, which uses the SenseHatManager to get the data and then sends it to the IoT Hub using the azure.iot.device.aio module.
- Define the main function, which creates an instance of the MessagingClient and then runs it in an asynchronous loop, sending the data to the IoT Hub at the specified interval.

## Running the Script
To run the script, you need to have `Python 3` installed on your Raspberry Pi, along with the sense_hat and azure-iot-device modules. You also need to have an Azure IoT Hub set up and have the connection string for your device.

Once you have all of these, you can run the script by using the following command:

## Copy code
```
python3 sense-hat-script.py
```
- The script will run indefinitely, sending the data to the IoT Hub at the specified interval. You can stop the script by pressing CTRL+C.
- The script can also be [run as a script](https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f) on Raspberry Pi's linux operating system.
