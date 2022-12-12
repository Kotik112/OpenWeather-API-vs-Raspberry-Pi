import datetime
import logging
import requests
import time

import azure.functions as func


def main(mytimer: func.TimerRequest, outdoc: func.Out[func.Document]) -> None:
    
    logging.info("Triggered") 

    # Make an API call to the specified URL
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                                params={
                                    "lat": 59.33,
                                    "lon": 18.06,
                                    "units": "metric",
                                    "appid": "a14e686a66f44fb43c62f3300b8ef2dd"
                                })

        # Extract the data from the response
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        dt = datetime.datetime.fromtimestamp(data["dt"])

        logging.info("Successfully made API call")

        # Write the data to the output binding
        data = {
            "temp": temp,
            "humidity": humidity,
            "pressure": pressure,
            "datetime": time.mktime(dt.timetuple())   
        }
        outdoc.set(func.Document.from_dict(data))
        

        logging.info("Successfully wrote data to output binding")
    except Exception as e:
        logging.info(f"Failed to write data to output binding: {e}")

