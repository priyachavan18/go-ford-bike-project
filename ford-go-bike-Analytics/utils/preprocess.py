"""
Ford GoBike Data Preprocessing

This script:
1. Loads all monthly CSV files
2. Validates the dataset
3. Cleans the data
4. Engineers new features
5. Saves a compressed Parquet dataset
"""

from pathlib import Path
import pandas as pd

# ======================================================
# Project Paths
# ======================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

OUTPUT_DIR = PROJECT_ROOT / "data"

OUTPUT_FILE = OUTPUT_DIR / "bike_data.parquet"

# ======================================================
# Expected Columns
# ======================================================

EXPECTED_COLUMNS = [
    "duration_sec",
    "start_time",
    "end_time",
    "start_station_id",
    "start_station_name",
    "start_station_latitude",
    "start_station_longitude",
    "end_station_id",
    "end_station_name",
    "end_station_latitude",
    "end_station_longitude",
    "bike_id",
    "user_type",
    "member_birth_year",
    "member_gender",
    "bike_share_for_all_trip",
]

# ======================================================
# Load Raw CSV Files
# ======================================================

def load_raw_data() -> pd.DataFrame:

    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in:\n{RAW_DATA_DIR}"
        )

    print("=" * 60)
    print(f"Found {len(csv_files)} monthly datasets")
    print("=" * 60)

    dataframes = []

    for file in csv_files:

        print(f"Loading {file.name}")

        df = pd.read_csv(
            file,
            low_memory=False
        )

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        missing = set(EXPECTED_COLUMNS) - set(df.columns)

        if missing:
            raise ValueError(
                f"{file.name} is missing columns:\n{missing}"
            )

        dataframes.append(df)

    df = pd.concat(
        dataframes,
        ignore_index=True
    )

    print("\nDataset Loaded Successfully")
    print(f"Rows    : {len(df):,}")
    print(f"Columns : {len(df.columns)}")

    return df


# ======================================================
# Clean Dataset
# ======================================================

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    print("\nCleaning dataset...")

    df = df.copy()

    df.drop_duplicates(inplace=True)

    df["start_time"] = pd.to_datetime(
        df["start_time"],
        errors="coerce"
    )

    df["end_time"] = pd.to_datetime(
        df["end_time"],
        errors="coerce"
    )

    df.dropna(
        subset=["start_time", "end_time"],
        inplace=True
    )

    df = df[df["duration_sec"] > 0]

    text_columns = [
        "user_type",
        "member_gender",
        "bike_share_for_all_trip",
        "start_station_name",
        "end_station_name",
    ]

    for col in text_columns:

        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
        )

    return df


# ======================================================
# Feature Engineering
# ======================================================

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:

    print("Creating features...")

    df["trip_minutes"] = df["duration_sec"] / 60

    df["trip_hours"] = df["duration_sec"] / 3600

    df["year"] = df["start_time"].dt.year

    df["month"] = df["start_time"].dt.month

    df["month_name"] = df["start_time"].dt.month_name()

    df["weekday"] = df["start_time"].dt.day_name()

    df["hour"] = df["start_time"].dt.hour

    df["quarter"] = df["start_time"].dt.quarter

    df["week"] = (
        df["start_time"]
        .dt.isocalendar()
        .week
        .astype(int)
    )

    df["is_weekend"] = (
        df["start_time"].dt.dayofweek >= 5
    )

    season_map = {
        12: "Winter",
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
    }

    df["season"] = df["month"].map(season_map)

    current_year = int(df["year"].mode()[0])

    df["member_birth_year"] = pd.to_numeric(
        df["member_birth_year"],
        errors="coerce"
    )

    df["age"] = current_year - df["member_birth_year"]

    df = df[
        (df["age"] >= 10)
        &
        (df["age"] <= 90)
    ]

    return df


# ======================================================
# Save Dataset
# ======================================================

def save_dataset(df: pd.DataFrame):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_parquet(
        OUTPUT_FILE,
        index=False,
        compression="snappy"
    )

    print("\nDataset Saved Successfully")
    print(f"Location : {OUTPUT_FILE}")

    size_mb = OUTPUT_FILE.stat().st_size / (1024 * 1024)

    print(f"Size     : {size_mb:.2f} MB")


# ======================================================
# Main
# ======================================================

def main():

    df = load_raw_data()

    df = clean_data(df)

    df = engineer_features(df)

    save_dataset(df)

    print("\nProcessing Complete")
    print(f"Final Shape : {df.shape}")


if __name__ == "__main__":
    main()