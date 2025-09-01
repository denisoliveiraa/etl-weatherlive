import requests
import logging
from save_extract import save_raw_data


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_data(base_url: str) -> dict | None:
  logging.info("Tentativa de busca na API")
  try: 
    
    # Base URL information
    response = requests.get(base_url)
    data = response.json()
    logging.info("Try to access Base API success")
    obs_url = data["properties"]["observationStations"]

    if not obs_url:
      return None

  except Exception as error:
    logging.error(f"Erro initial Access to URL {error}")
    return None
    
  try: 
    # Stations URL information
    details_url = requests.get(obs_url)
    data_obs = details_url.json()
    observation_station = data_obs["observationStations"][0]
    logging.info("Try to get observation station information success")
    observation_station = observation_station + "/observations/latest"

  except Exception as error:
    logging.error(f"Error to get the station: {error}")
    return None
  
  try: 
    # specifc Station URL information
    station_url = requests.get(observation_station)
    data_weather = station_url.json()
    logging.info("Try to get temperature information success")

  except Exception as error:
    logging.error(f"Error to get the accesss one observation: {error}")
    return None

  try: 
    # saving the information to being consuming by spark
    save_raw_data(data_weather)
    logging.info("Save raw information Sucesss")
    return save_raw_data
  
  except Exception as error:
    logging.error(f"Error to save/create the register csv {error}")
    return None
  

    

