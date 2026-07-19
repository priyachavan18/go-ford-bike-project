from pathlib import Path

import gdown
import pandas as pd
import streamlit as st

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

DATA_FILE = DATA_DIR / "bike_data.parquet"

FILE_ID = "1vUCmETYV8voUa3leTb12hLKZU37CPzwX"

DOWNLOAD_URL = f"https://drive.google.com/uc?id={FILE_ID}"


# -------------------------------------------------------
# Download Dataset
# -------------------------------------------------------

def download_dataset():

    if DATA_FILE.exists():
        return

    with st.spinner("Downloading dataset... Please wait (first run only)."):

        gdown.download(
            DOWNLOAD_URL,
            str(DATA_FILE),
            quiet=False,
        )


# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

@st.cache_data(show_spinner="Loading Ford GoBike dataset...")
def load_data():

    download_dataset()

    return pd.read_parquet(DATA_FILE)


# -------------------------------------------------------
# Validate Dataset
# -------------------------------------------------------

def validate_dataset(df):

    required_columns = [
        "start_time",
        "end_time",
        "duration_sec",
        "trip_minutes",
        "hour",
        "weekday",
        "month_name",
        "season",
        "user_type",
        "member_gender",
        "age",
        "start_station_name",
        "end_station_name",
        "start_station_latitude",
        "start_station_longitude",
        "end_station_latitude",
        "end_station_longitude",
    ]

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns:\n{missing}"
        )


# -------------------------------------------------------
# Dataset Summary
# -------------------------------------------------------

def dataset_summary(df):

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_mb": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2,
        ),
    }