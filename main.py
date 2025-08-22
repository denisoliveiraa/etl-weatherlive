from src.etl.extract import extract_data
from src.etl.transform import transform_weather_data
import logging
from dotenv import load_dotenv
import os



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if __name__ == "__main__":
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    weather_data = extract_data(base_url)
    if weather_data:
        try:
            weather_result = transform_weather_data(weather_data)
            print(weather_result)
            logging.info(f"Temperatura: {weather_result}")
        except:
           logging.error("Weather data not found")
    else: 
        logging.error("Erro to access extract_data")
        
