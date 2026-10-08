from .config import PROCESSED_DIR
from .extract import extract_weather
from .load import load_weather
from .transform import transform_weather


def run_pipeline() -> None:
    print("=" * 50)
    print("ETL - DADOS METEOROLÓGICOS")
    print("=" * 50)

    raw_file = extract_weather()
    dataframe = transform_weather(raw_file)

    output_file = PROCESSED_DIR / "weather.csv"
    load_weather(dataframe, output_file)

    print()
    print("=" * 50)
    print("Pipeline concluído com sucesso!")
    print("=" * 50)
    print(f"Total de registros: {len(dataframe)}")
    print(f"Arquivo final: {output_file}")


if __name__ == "__main__":
    run_pipeline()
