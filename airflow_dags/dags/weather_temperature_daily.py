import sys
sys.path.append('/mnt/c/dev/etl-weatherlive')  
from airflow.models import DAG 
from airflow.operators.python import PythonOperator  
from datetime import datetime, timedelta
from src.etl.extract import extract_data
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



default_args = {
    'owner': 'linkedin.com/in/denis-o-barbosa',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='weather_temperature',
    default_args=default_args,
    description='Rotine to get daily changes of temperature',
    schedule=timedelta(days=1),  # runs once a day
    start_date=datetime(2025, 8, 21),
    catchup=False,
    tags=['etl-weather']
) as dag:
    
    def task_extract(base_url):
        try:
            weather_data = extract_data(base_url)
            logging.info(f"data_info: {weather_data}")
        except:
            logging.error("Return ERROR extract")

    t1 = PythonOperator(
        task_id='extract_data',
        python_callable=task_extract
    )
  
    t1 
