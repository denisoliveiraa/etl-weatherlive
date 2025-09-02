import json
from pathlib import Path
import logging

def save_raw_data(data: dict, filename="data/raw/weather.json"):
    try:
        Path("data/raw").mkdir(parents=True, exist_ok=True)
        with open(filename, "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(e)
        logging.error(f"Error to save/create the register csv {e}")
