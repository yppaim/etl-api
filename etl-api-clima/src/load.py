from pathlib import Path

import pandas as pd


def load_weather(dataframe: pd.DataFrame, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    print("[LOAD] Salvando CSV...")

    dataframe.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(f"[LOAD] Arquivo salvo em {output_file}")
