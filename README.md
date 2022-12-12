![azure-complete](https://user-images.githubusercontent.com/88910492/207046391-0d5e708d-b7c0-4ed6-8b46-4af925823c76.png)

# Azure cloud architecture for gather weather data from IoT and API
The goal of this project is to use a Raspberry Pi with a Sense HAT attached to it to collect temperature, humidity, and air pressure data from the environment. This data will be sent to Azure IoT Hub and processed by Azure Stream Analytics. In addition to the data from the Raspberry Pi, the project will also gather weather data from the OpenWeather API and compare it to the data collected by the Raspberry Pi.

The project will involve setting up a Raspberry Pi with a Sense HAT, configuring it to send data to the IoT Hub, creating an Azure Stream Analytics job to parse the data and store it in Azure, and setting up the necessary tables and collections in CosmosDB to store the data. The project will also involve obtaining an API key from OpenWeather and using it to retrieve weather data for the location of the Raspberry Pi.

Once the project is set up, we will be able to monitor the data as it is collected and stored in Azure. We can then use this data to compare the weather data from the OpenWeather API with the data collected by the Raspberry Pi. This will allow us to gain insights about the environment and the accuracy of the weather data.

## Table of Contents:
- Hardware Setup
- Prerequisites
- Getting started
- License

## Hardware Setup
![image](https://user-images.githubusercontent.com/88910492/207051605-f3dbafa1-f166-432c-afb0-702207988a7b.png)

The hardware setup for this project involves using a `Raspberry Pi` with a `Sense HAT` attached to it. The Sense HAT is a small add-on board that allows the Raspberry Pi to sense the environment, including temperature, humidity, and air pressure.

## Prerequisites
- [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [Sense HAT](https://pythonhosted.org/sense-hat/)
- Azure subscription <img src="https://user-images.githubusercontent.com/88910492/207051831-c6e9d37f-3d1d-4488-80dc-22f5d2428e74.png" width="30">
  - Azure IoT Hub
  - Azure Stream Analytics
  - Azure Blob storage
  - Azure CosmosDB NoSQL x2 (I created 2 databases to replicate a case where data is coming from two independent sources)
  - Azure timerTrigger function (Refer to my [Azure function github](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/tree/master/azure-api-function))
  - PowerBI license to visualize data from the databses. I used the 60 day free trial for my project.
- Valid key to an API that could provide you with local weather conditions. I used [OpenWeatherMap API](https://openweathermap.org/current) for its ease of use and because it offers the data I needed for free.

## Getting Started
- [Set up (Swedish)](https://azure.microsoft.com/sv-se/?&ef_id=CjwKCAiAv9ucBhBXEiwA6N8nYMv_PFgsW9RxByXOQ4F3EqaJOEccaQgXZBBLujLvCmu0UMn0lhZNmxoCXbQQAvD_BwE:G:s&OCID=AIDcmmtops7fz5_SEM_CjwKCAiAv9ucBhBXEiwA6N8nYMv_PFgsW9RxByXOQ4F3EqaJOEccaQgXZBBLujLvCmu0UMn0lhZNmxoCXbQQAvD_BwE:G:s&gclid=CjwKCAiAv9ucBhBXEiwA6N8nYMv_PFgsW9RxByXOQ4F3EqaJOEccaQgXZBBLujLvCmu0UMn0lhZNmxoCXbQQAvD_BwE) your Azure subscription and create an Azure IoT Hub.
- Connect your Raspberry Pi to the IoT Hub and configure it to send temperature, humidity, and air pressure data. Refer to my [github python script](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/tree/master/raspberry-pi-script)
- Create an Azure Stream Analytics job to parse the data from the IoT Hub and send it to both Blob storage and CosmosDB.
- Set up the necessary tables and collections in CosmosDB to store the data.
- Monitor the data as it is sent to and stored in Azure.

# Security concerns and improvements:

## License
This project is licensed under the MIT License.
