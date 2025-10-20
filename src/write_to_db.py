import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Загружаем переменные из .env
load_dotenv()

host = os.getenv("PGHOST")
port = os.getenv("PGPORT", "5432")
db = os.getenv("PGDATABASE")
user = os.getenv("PGUSER")
password = os.getenv("PGPASSWORD")

# Подключаемся к PostgreSQL
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

# Загружаем датасет
df = pd.read_parquet("data/clean_data.parquet")
df_100 = df.head(100)

# Имя таблицы
table_name = "bondarenko"

# Записываем в базу
df_100.to_sql(table_name, engine, schema="public", index=False, if_exists="replace")
