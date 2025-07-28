import requests

def extract_data():

  # Latitude e Longitude de curitiba
  url = "https://api.open-meteo.com/v1/forecast?latitude=25.25&longitude=49.16&hourly=temperature_2m"

  headers = {"accept": "application/json"}

  response = requests.get(url, headers=headers)
  data = response.json()
  
  baseHourWeather = data["hourly"]["time"][-1]
  tempeatureOnBaseHour = data["hourly"]["temperature_2m"][-1]


  print(baseHourWeather)
  print(tempeatureOnBaseHour)
extract_data()
