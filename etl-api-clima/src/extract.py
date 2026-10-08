import json
from datetime import datetime, timezone
from pathlib import Path

import requests

from .config import (
    API_URL,
    FORECAST_DAYS,
    LATITUDE,
    LONGITUDE,
    RAW_DIR,
    TIMEZONE,
)


def extract_weather() -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "wind_speed_10m,"
            "weather_code"
        ),
        "forecast_days": FORECAST_DAYS,
        "timezone": TIMEZONE,
    }

    print("[EXTRACT] Consultando Open-Meteo...")

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()

    payload = response.json()

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_file = RAW_DIR / f"weather_{timestamp}.json"

    output_file.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("[EXTRACT] Dados recebidos com sucesso.")
    print(f"[EXTRACT] Arquivo bruto salvo em {output_file}")

    return output_file
