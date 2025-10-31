import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

def load_to_db_and_parquet(df: pd.DataFrame, skip_db: bool = False):
    """
    Svaing data
    """
    os.makedirs("data/processed", exist_ok=True)

    parquet_path = "data/processed/clean_data.parquet"
    df.to_parquet(parquet_path, index=False)
    print(f"Saved data to {parquet_path}")

    if skip_db:
        print("Database upload skipped (use --no-db to enable this mode)")
        return

    # Connecting to the database
    load_dotenv()
    host = os.getenv("PGHOST")
    port = os.getenv("PGPORT", "5432")
    db = os.getenv("PGDATABASE")
    user = os.getenv("PGUSER")
    password = os.getenv("PGPASSWORD")

    if not all([host, db, user, password]):
        print("Missing DB credentials in .env. Skipping database upload.")
        return

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # ID
    df_100 = df.head(100).reset_index(drop=True)
    df_100.insert(0, "id", df_100.index + 1)

    # Loading into PostgreSQL
    table_name = "bondarenko"
    df_100.to_sql(
        table_name,
        engine,
        schema="public",
        index=False,
        if_exists="replace"
    )
    
    print(f"Loaded {len(df_100)} rows into table '{table_name}' in PostgreSQL")

