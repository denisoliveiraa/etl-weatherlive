import pandas as pd
import logging

def transform_weather_data(weather_details) : #-> dict | None
  temperature = weather_details['properties']['temperature']['value']
  print(temperature)
  try:
    temperature = weather_details['properties']['temperature']['value']
    humidity = weather_details['properties']['relativeHumidity']['value']
    wind_speed = weather_details['properties']['windSpeed']['value']
    wind_dir = weather_details['properties']['windDirection']['value']
    
    
    #data = pd.DataFrame[{"temperature": temperature, "humidity": humidity, "wind_speed": wind_speed, "wind_dir": wind_dir }]
    #logging.log("Transform data success")

    return humidity
  except: 
    logging.error("Transform data Error")

  