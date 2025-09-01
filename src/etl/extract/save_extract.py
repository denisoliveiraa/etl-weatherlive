import json
from pathlib import Path

def save_raw_data(data: dict, filename="data/raw/weather.json"):
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f)