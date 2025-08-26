from airflow_dags.dags.weather_temperature_daily import task_extract
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
    try:
        task_extract(base_url)
        logging.info("DAG weather temperature daily ACCESS SUCCESS")
    except:
        logging.error("DAG weather temperature daily ERROR")

        
