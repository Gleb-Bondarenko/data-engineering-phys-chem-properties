# Data Engineering: Physical and Chemical Properties of Substances

This project implements a full ETL pipeline (Extract → Transform → Load) for a molecular dataset containing physicochemical and structural features of chemical compounds.
The pipeline automates data downloading, cleaning, type conversion, and saving in both Parquet format and a PostgreSQL database.


# Dataset
https://drive.google.com/file/d/1F6wBd8MNkuAKBLcFTcZjLSU9cg6-VRqR/view?usp=sharing

# Dataset Description
The dataset is automatically downloaded from Google Drive on the first run.
It contains ~4,300 molecular records with various physicochemical properties:
* Molecular weight
* Melting & boiling points
* Heats of fusion and vaporization
* Critical temperature and pressure
* Flash point
* LogP (octanol–water partition coefficient)
* Boolean features (```is_alkane```, ```is_ester```, ```is_aromatic```, etc.)

N.B. Since these are physical measurements, extreme values may not always indicate outliers — some reflect true physical phenomena.
However, values violating fundamental physical laws (e.g., temperature < 0 K) are treated as invalid and removed.

# Project Structure
```bash
my_project/
│
├── etl/                       # ETL package
│   ├── __init__.py
│   ├── extract.py             # Data loading and initial validation
│   ├── transform.py           # Cleaning and type conversions
│   ├── validate.py            # Validation logic
│   ├── load.py                # Save to DB and Parquet
│   └── main.py                # CLI entry point
│
├── data/
│   ├── raw/                   # Raw data (.csv)
│   └── processed/             # Processed data (.parquet)
│
├── notebooks/
│   └── EDA.ipynb              # Exploratory Data Analysis notebook
│
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

# ETL Module Overview

| Module         | Purpose                                                                              | Key Functions                              |
| :------------- | :----------------------------------------------------------------------------------- | :----------------------------------------- |
| `extract.py`   | Downloads data from Google Drive, performs basic validation, saves to `data/raw`     | `extract_data()`                           |
| `transform.py` | Cleans and converts column types (numeric, boolean), removes invalid physical values | `transform_data()`                         |
| `validate.py`  | Validates datasets after each stage (NaN checks, physical constraints)               | `validate_raw()`, `validate_transformed()` |
| `load.py`      | Uploads the final dataset to PostgreSQL and saves as Parquet                         | `load_to_db_and_parquet()`                 |
| `main.py`      | CLI interface combining all stages                                                   | `main()`                                   |


# Vizualization and EDA
The research analysis notebook is available at this link: [nbviewer](https://nbviewer.org/gist/Gleb-Bondarenko/bdf2caaa024245f6a660145409612cc1)

EDA features:
* Distributions of physical properties of molecules
* Correlation maps
* Dynamic visualization of dependencies (Plotly Express)
* Graphs in a unified style with the Spectrum palette (Origin-like)


# Install dependencies

**Option 1: using venv**

   1. Create a virtual environment

   ```bash
   python -m venv my_env
   ```
   2. Activate it
   ```bash
   source my_env/bin/activate       # macOS / Linux
   my_env\Scripts\activate          # Windows
   ```

   3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

**Option 2: using Poetry**
   1. Install Poetry if not already installed
   ```bash
   pip install poetry
   ```
   2. Install all dependencies (will create a virtual environment automatically)
   ```bash
   poetry install
   ```

# Run the ETL Pipeline

   Run the full pipeline (with DB upload and Parquet output):
   ```bash
   python -m etl.main
   ```
   Run without database upload (for testing or local development):
   ```bash
   python -m etl.main --no-db
   ```
After execution, you’ll find the results here:
* data/raw/raw_data.csv
* data/processed/clean_data.parquet


# Requirements

```
pandas
numpy
matplotlib
seaborn
plotly
sqlalchemy
python-dotenv
wget
pyarrow
```

# Source
https://www.kaggle.com/datasets/ivanyakovlevg/physical-and-chemical-properties-of-substances
