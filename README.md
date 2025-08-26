# ETL Weather Temperature Daily

This project performs daily temperature data collection from a public API using an ETL (Extract, Transform, Load) approach orchestrated with Airflow.


## Features

* Collects daily temperature data from a public API.
* Daily pipeline orchestrated with Airflow.
* Local execution for testing via `main.py`.
* Configurable environment variables via `.env`.

## Technologies Used

* Python 3.12
* Airflow (DAG orchestration)
* Requests (API consumption)
* Python-Dotenv (environment variable loading)
* Logging (execution monitoring)

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/denisoliveiraa/etl-weatherlive.git
cd etl-weatherlive
```

### 2. Create and activate the virtual environment

```bash
python -m venv venv
source venv/bin/activate  # WSL/Linux
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with the variable:

```
BASE_URL=https://api.weather.gov/points/39.7456,-97.0892
```

### 5. Run locally

```bash
python main.py
```

### 6. Run via Airflow

* Configure Airflow to point to the `airflow_dags/dags` folder.
* The `weather_temperature` DAG will run automatically once a day.
* Execution logs can be accessed via the Airflow Web UI.

