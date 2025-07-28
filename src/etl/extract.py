import requests

def extract_data():

  # Latitude e Longitude de curitiba
  url = "https://api.open-meteo.com/v1/forecast?latitude=22.25&longitude=49.16&hourly=temperature_2m"
  headers = {"accept": "application/json"}
  baseHourWeather = None
  baseTemperatureWeather = None

  try: 
    response = requests.get(url, headers=headers)
    data = response.json()
    baseHourWeather = data["hourly"]["time"][-1]
    baseTemperatureWeather = data["hourly"]["temperature_2m"][-1]
    print(baseHourWeather)
    print(baseTemperatureWeather)
    
  except Exception as error:
    print(f'we have a problem: {error}')
    
  
extract_data()
