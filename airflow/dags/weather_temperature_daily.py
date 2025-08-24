from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.etl import extract_data, transform
from dotenv import load_dotenv
import os


default_args = {
    'owner': 'meu_usuario',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define o DAG
with DAG(
    'weather_temperature',
    default_args=default_args,
    description='Rotine to get daily changes of temperature',
    schedule_interval=timedelta(days=1),  # executa uma vez por dia
    start_date=datetime(2025, 8, 21),
    catchup=False,
    tags=['etl-weather']
) as dag:
    
    def task_extract(**kwargs):
        base_url = os.getenv("BASE_URL")
        data = extract_data(base_url)
        kwargs['ti'].xcom_push(key='data', value=data)  

    t1 = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True
    )
    #Transform Task

    def task_transform(**kwargs):
        ti = kwargs['ti']
        data = ti.xcom_pull(key='data', task_ids='data_extract_form')  
        df = transform(data)
        print(df.head()) 
        return df
    
    t2 = PythonOperator(
        task_id='data_transform',
        python_callable=transform,
        provide_context=True
    )
  
    t1 >> t2  
