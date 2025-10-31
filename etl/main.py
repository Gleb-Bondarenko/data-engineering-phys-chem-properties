import argparse
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_db_and_parquet


def main():
    parser = argparse.ArgumentParser(description="ETL pipeline: extract → transform → load")
    parser.add_argument(
        "--no-db",
        action="store_true",
        help="Skip database upload (useful for testing)"
    )
    args = parser.parse_args()

    print("Launching the ETL pipeline...")

    # Extraction
    df = extract_data()
    print(f"Extracted {len(df)} rows")

    # Transforming
    df_transformed = transform_data(df)
    print(f"Transformed dataset shape: {df_transformed.shape}")

    # Loading
    load_to_db_and_parquet(df_transformed, skip_db=args.no_db)
    print("Data successfully saved to Parquet and (optionally) to DB")

    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    main()