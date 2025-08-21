from src.etl.extract import extract_data
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
        logging.info(f"Dados brutos: {weather_data}")
