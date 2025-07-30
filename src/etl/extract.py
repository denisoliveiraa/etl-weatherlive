import requests
from dotenv import load_dotenv
import os

load_dotenv() 

def extract_data():

  # Latitude e Longitude de curitiba
  api_key = os.getenv('URL_API')
  url = api_key
  headers = {"accept": "application/json"}
  baseHourWeather = None
  baseTemperatureWeather = None

  try: 
    response = requests.get(url, headers=headers)
    data = response.json()
    baseHourWeather = data["hourly"]["time"][-1]
    baseTemperatureWeather = data["hourly"]["temperature_2m"][-1]

  except Exception as error:
    print(f'we have a problem: {error}')

  finally:
    return baseTemperatureWeather, baseHourWeather
    
  
extract_data()
