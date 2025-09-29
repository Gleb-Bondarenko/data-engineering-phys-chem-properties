import os
import pandas as pd
import wget

# 1. Загрузка данных с Google Drive

FILE_ID = "1F6wBd8MNkuAKBLcFTcZjLSU9cg6-VRqR"  # ID файла на Google Drive
FILE_NAME = "raw_data.csv"
FILE_URL = f"https://drive.google.com/uc?id={FILE_ID}"

# Если файла нет - скачиваем
if not os.path.exists(FILE_NAME):
    print("Файл не найден, скачиваю...")
    wget.download(FILE_URL, FILE_NAME)
else:
    print("Файл уже есть, читаю локальную копию.")


raw_data = pd.read_csv(FILE_NAME)  # читаем файл

# 2. Приведение типов
# Приводим столбцы "is_" в Булевый тип
bool_cols = [c for c in raw_data.columns if c.startswith("is_")]
for col in bool_cols:
    raw_data[col] = raw_data[col].map(lambda x: str(x).upper() == "TRUE")
# Числовые столбцы
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
raw_data[num_cols] = raw_data[num_cols].apply(pd.to_numeric, errors="coerce")
# 3. Сохранение в Parquet
raw_data.to_parquet("clean_data.parquet", index=False)

# 4. Проверка
print(raw_data.dtypes.head(15))
print(raw_data.head(5))

print("Готово! Сохранено как clean_data.parquet")
