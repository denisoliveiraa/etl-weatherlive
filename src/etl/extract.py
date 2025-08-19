import requests
import os
from dotenv import load_dotenv

def extract_data():

  
  load_dotenv()  
  base_url = os.getenv("BASE_URL")

  try: 
    response = requests.get(base_url)
    data = response.json()
    print(data)
    
  except Exception as error:
    print(f'we have a problem: {error}')
    
  
extract_data()
