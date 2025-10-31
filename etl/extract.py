import os
import pandas as pd
import wget
from pathlib import Path


def extract_data(file_id: str = "1F6wBd8MNkuAKBLcFTcZjLSU9cg6-VRqR",
                 file_name: str = "raw_data.csv") -> pd.DataFrame:
    """
    Downloads CSV from Google Drive, saves to data/raw, returns a DataFrame
    """
    file_url = f"https://drive.google.com/uc?id={file_id}"
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    file_path = raw_dir / file_name

    if not file_path.exists():
        """
        Checking if a file exists locally
        """
        print("File not found, downloading from Google Drive")
        wget.download(file_url, str(file_path))
        print(f"File uploaded to {file_path}")
    else:
        print(f"Using a local copy: {file_path}")

    df = pd.read_csv(file_path)
    print(f"Successfully loaded {len(df)} rows, {len(df.columns)} columns")

    return df