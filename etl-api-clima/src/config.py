import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

LATITUDE = float(os.getenv("LATITUDE", "-28.2925"))
LONGITUDE = float(os.getenv("LONGITUDE", "-53.5027"))
TIMEZONE = os.getenv("TIMEZONE", "America/Sao_Paulo")
FORECAST_DAYS = int(os.getenv("FORECAST_DAYS", "7"))

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

API_URL = "https://api.open-meteo.com/v1/forecast"
