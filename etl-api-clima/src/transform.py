import json
from pathlib import Path

import pandas as pd


def transform_weather(raw_file: Path) -> pd.DataFrame:
    print("[TRANSFORM] Normalizando dados...")

    payload = json.loads(raw_file.read_text(encoding="utf-8"))
    hourly = payload["hourly"]

    dataframe = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_c": hourly["temperature_2m"],
        "humidity_percent": hourly["relative_humidity_2m"],
        "precipitation_mm": hourly["precipitation"],
        "wind_speed_kmh": hourly["wind_speed_10m"],
        "weather_code": hourly["weather_code"],
    })

    dataframe["timestamp"] = pd.to_datetime(
        dataframe["timestamp"],
        errors="coerce",
    )

    numeric_columns = [
        "temperature_c",
        "humidity_percent",
        "precipitation_mm",
        "wind_speed_kmh",
        "weather_code",
    ]

    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(
            dataframe[column],
            errors="coerce",
        )

    dataframe = (
        dataframe
        .dropna(subset=["timestamp"])
        .drop_duplicates(subset=["timestamp"])
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    print(f"[TRANSFORM] {len(dataframe)} registros preparados.")

    return dataframe
