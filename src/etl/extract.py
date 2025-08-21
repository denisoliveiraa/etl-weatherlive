import requests
import os
from dotenv import load_dotenv
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_data():
  load_dotenv()  
  base_url = os.getenv("BASE_URL")
  logging.info("Tentativa de busca na API")
  try: 
    
    response = requests.get(base_url)
    data = response.json()
    logging.info("Tentativa concluída com sucesso")
    print(data)
    
  except Exception as error:
    logging.error(f"Erro HTTP: {error}")
    
  
extract_data()
