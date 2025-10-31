import pandas as pd


def validate_load_input(df: pd.DataFrame) -> None:
    """
    Checks that the dataframe is not empty and contains key fields
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty - there is nothing to load")
    required_cols = ["molecular_weight", "logP"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"The DataFrame is missing required columns: {missing}")
    print("Input validation passed")


def validate_db_connection(host, port, db, user, password) -> None:
    """
    Checks that all connection parameters are present
    """
    missing = [
        name
        for name, value in {
            "PGHOST": host,
            "PGPORT": port,
            "PGDATABASE": db,
            "PGUSER": user,
            "PGPASSWORD": password,
        }.items()
        if not value
    ]
    if missing:
        raise EnvironmentError(f"Missing variables in .env: {missing}")
    print("Connection parameters were checked successfully")