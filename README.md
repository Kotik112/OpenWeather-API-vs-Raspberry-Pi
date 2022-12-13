![azure-complete](https://user-images.githubusercontent.com/88910492/207046391-0d5e708d-b7c0-4ed6-8b46-4af925823c76.png)

# Azure cloud architecture for gather weather data from IoT and API
The goal of this project is to use a Raspberry Pi with a Sense HAT attached to it to collect temperature, humidity, and air pressure data from the environment. This data will be sent to Azure IoT Hub and processed by Azure Stream Analytics. In addition to the data from the Raspberry Pi, the project will also gather weather data from the OpenWeather API and compare it to the data collected by the Raspberry Pi.

The project will involve setting up a Raspberry Pi with a Sense HAT, configuring it to send data to the IoT Hub, creating an Azure Stream Analytics job to parse the data and store it in Azure, and setting up the necessary tables and collections in CosmosDB to store the data. The project will also involve obtaining an API key from OpenWeather and using it to retrieve weather data for the location of the Raspberry Pi.

Once the project is set up, we will be able to monitor the data as it is collected and stored in Azure. We can then use this data to compare the weather data from the OpenWeather API with the data collected by the Raspberry Pi. This will allow us to gain insights about the environment and the accuracy of the weather data.

**NOTE**: This project has more detailed documentation for [azure-api-function](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/tree/master/azure-api-function) and [raspberry-pi-script](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/tree/master/raspberry-pi-script) respectively.

## Table of Contents:
- [Hardware Setup](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#hardware-setup)
- [Prerequisites](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#prerequisites)
- [Getting started](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#getting-started)
- [Result / Output](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#result--output)
- [Scalability](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#scalability)
- [Security concerns](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#security-concerns-and-improvements)
- [License](https://github.com/Kotik112/OpenWeather-API-vs-Raspberry-Pi/edit/master/README.md#license)

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
```
/* Query output for Azure Stream Analytics) */
/* Save temperature and date to sensor_data_db (NoSQL) */
SELECT
    dt as 'datetime',
    temperature,
    humidity,
    pressure
INTO
    [sensor-data-input]
FROM
    [iothub-output]
WHERE
    temperature is not null

/* Save everything (including meta data) to Blob storage */
SELECT
    *
INTO
    [blob-input]
FROM
    [iothub-output]
```
- Set up the necessary tables and collections in CosmosDB to store the data.
- Monitor the data as it is sent to and stored in Azure.

## Result / Output:
![powerbi](https://user-images.githubusercontent.com/88910492/207239087-dd5ce9dc-2206-490a-866b-80d3a0c1cdc0.png)
Many different types of visualizations can be made out of the data from the two cosmosDB databses. I simply decided to visualize a side by side graph view of the data from each individual database. More than two databases and multiple tables can be imported in this way to aggregate and visualize datasets.


## Scalability:
- The project uses Azure Storage (Cold path) to store the processed data for further analysis and reporting. This allows the system to scale up or down the storage capacity as needed to handle the data volume.
- The project uses Azure Stream Analytics to process the data in real-time, performing tasks such as aggregation, filtering, and triggering alerts. This allows you to scale up or down the number of stream analytics jobs as needed to handle the data volume.

## Security concerns and improvements:
#### Certificates over Primary Connection Strings
1. In this project I use `Primary Connection String` to connect the IoT device (Raspberry Pi) to the Azure IoT hub. This method of authenticating devices is meant for legacy hardware that do not support certificates. It is recommended to use certificates over connection strings for the following reasons:
- Connecting to an IoT device through a certificate rather than a primary connection string can provide a number of security benefits. First, using a certificate allows for mutual authentication between the device and the IoT hub, meaning that both the device and the hub can verify each other's identity. This can help to prevent man-in-the-middle attacks, where an attacker intercepts communication between the device and the hub and tries to impersonate one of the two parties.

- Another benefit of using certificates is that they can be easily revoked if they are lost or stolen. This is especially important in the case of IoT devices, which may be deployed in remote or inaccessible locations. With a primary connection string, revoking access can be more difficult, as it typically involves changing the connection string on both the device and the IoT hub.


2. Encrypt your data: Encrypting your data both in transit and at rest can help to protect it from being accessed by unauthorized parties.
- This is particularly useful if the data being sent is sensitive.

## Issues:
I had issues with the senseHAT's temperature sensor reading way too high temperatures. It shows the room temperature, sometimes as high as 38 C. This is obviously faulty readings. Due to a lack of a secondary sensor I had to make do with what I had. My theory is that the senseHAT sits so close to the Raspberry Pi's processor that it contributes to the high temperature readings.

## License
This project is licensed under the MIT License.
