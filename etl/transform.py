import pandas as pd
from pathlib import Path


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Casts types, handles Boolean and numeric columns, and preserves parquet
    """
    print("Start of data transformation")

    # Boolean columns
    bool_cols = [c for c in df.columns if c.startswith("is_")]
    for col in bool_cols:
        df[col] = df[col].map(lambda x: str(x).upper() == "TRUE")

    # Numeric columns
    num_cols = [
        "molecular_weight",
        "melting_point_K",
        "boiling_point_K",
        "heat_of_fusion",
        "heat_of_vaporization",
        "critical_temperature",
        "critical_pressure",
        "flash_point",
        "logP",
    ]
    df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")

    # Preserving parquet
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    parquet_path = processed_dir / "clean_data.parquet"
    df.to_parquet(parquet_path, index=False)

    print(f"Transformation complete. File saved: {parquet_path}")
    print(df.dtypes.head(10))

    return df

