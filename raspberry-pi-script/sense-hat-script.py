# Written by: Arman Iqbal
# Date: 2022-12-12
# Class: Cloud architecture, IoT21 Nackademin


# README:
# This script uses the Sense HAT to gather data from the Sense HAT's sensors and send it to the IoT Hub.
# The data is sent to the IoT Hub as a JSON object containing the temperature, humidity and pressure.

# sense HAT documentation: https://pythonhosted.org/sense-hat/api/
from sense_hat import SenseHat
# IoTHubDeviceClient documentation: https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device.iothubdeviceclient?view=azure-python
from azure.iot.device.aio import IoTHubDeviceClient
# env_secrets contains the connection string to the IoT Hub. Create one according to the github README.
import env_secrets
import asyncio
import time

# Define INTERVAL (in seconds) to the time between each message sent to the IoT Hub
INTERVAL = 180


class SenseHatManager:
    def __init__(self):
        self.sense = SenseHat()

    def get_temperature(self):
        return self.sense.get_temperature()

    def get_humidity(self):
        return self.sense.get_humidity()

    def get_pressure(self):
        return self.sense.get_pressure()

    def get_all(self):
        return {
            "temperature": self.get_temperature(),
            "humidity": self.get_humidity(),
            "pressure": self.get_pressure(),
            "dt": int(time.time())
        }


class MessagingClient:
    def __init__(self):
        self.sense_hat_manager = SenseHatManager()
        # Retrieves the IoT Hub connection string from the environment variables. See env_secrets.py
        self.CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
        self.client = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING)
        asyncio.run(self.client.connect(mqtt_pipeline=True))

    async def send_message(self, message):
        await self.client.send_message(message)

    async def run_temperature(self):
        while True:
            data = self.sense_hat_manager.get_temperature()
            print(f"Sending: {data}")
            await self.send_message(f"{{\"temperature\": {data}}}")
            await asyncio.sleep(INTERVAL)

    async def run_all(self):
        while True:
            data = self.sense_hat_manager.get_all()
            print(f"Sending: {data}")
            await self.send_message(f"{{\"temperature\": {data['temperature']}, \"humidity\": {data['humidity']}, \"pressure\": {data['pressure']}, \"dt\": {data['dt']}}}")
            await asyncio.sleep(INTERVAL)


def main():
    # Create an instance of the MessagingClient class
    messaging_client = MessagingClient()

    # Run the MessagingClient class
    asyncio.run(messaging_client.run_all())


if __name__ == "__main__":
    main()


