import pandas as pd


# -------------------------------------------------------
# Number Formatting
# -------------------------------------------------------

def format_number(value: float) -> str:

    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"

    if value >= 1_000:
        return f"{value/1_000:.1f}K"

    return f"{value:.0f}"


# -------------------------------------------------------
# Percentage Formatting
# -------------------------------------------------------

def format_percentage(value: float) -> str:
    return f"{value:.1f}%"


# -------------------------------------------------------
# Duration Formatting
# -------------------------------------------------------

def minutes_to_hours(minutes: float) -> str:

    hours = minutes / 60

    if hours < 1:
        return f"{minutes:.1f} min"

    return f"{hours:.1f} hrs"


# -------------------------------------------------------
# Top N Helper
# -------------------------------------------------------

def top_n(df: pd.DataFrame, column: str, n: int = 10):

    return (
        df[column]
        .value_counts()
        .head(n)
    )


# -------------------------------------------------------
# Safe Mean
# -------------------------------------------------------

def safe_mean(series):

    if series.empty:
        return 0

    return series.mean()


# -------------------------------------------------------
# Safe Median
# -------------------------------------------------------

def safe_median(series):

    if series.empty:
        return 0

    return series.median()