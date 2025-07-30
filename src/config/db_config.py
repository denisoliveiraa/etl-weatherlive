from dotenv import load_dotenv
import os
import psycopg2

load_dotenv() 


host = os.getenv('DB_HOST')      
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
port = os.getenv('URL_API')            

def connection():
  try:
      conn = psycopg2.connect(
          host=host,
          dbname=dbname,
          user=user,
          password=password,
          port=port
      )
      print("Conexão bem-sucedida!")
      return conn

  except Exception as e:
      print("Erro na conexão:", e)