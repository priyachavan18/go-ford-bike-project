import streamlit as st
import pandas as pd


def sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates sidebar filters and returns the filtered dataframe.
    """

    st.sidebar.image(
        "https://img.icons8.com/color/96/bicycle.png",
        width=80,
    )

    st.sidebar.title("🚴 Ford GoBike")

    st.sidebar.markdown("---")

    # -------------------------
    # Month Filter
    # -------------------------

    months = sorted(df["month_name"].dropna().unique())

    selected_months = st.sidebar.multiselect(
        "📅 Select Month",
        options=months,
        default=months,
    )

    # -------------------------
    # User Type Filter
    # -------------------------

    user_types = sorted(df["user_type"].dropna().unique())

    selected_user_types = st.sidebar.multiselect(
        "👥 User Type",
        options=user_types,
        default=user_types,
    )

    # -------------------------
    # Gender Filter
    # -------------------------

    genders = sorted(df["member_gender"].dropna().unique())

    selected_genders = st.sidebar.multiselect(
        "🚻 Gender",
        options=genders,
        default=genders,
    )

    # -------------------------
    # Weekday Filter
    # -------------------------

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    selected_weekdays = st.sidebar.multiselect(
        "📆 Weekday",
        options=weekday_order,
        default=weekday_order,
    )

    # -------------------------
    # Hour Slider
    # -------------------------

    hour_range = st.sidebar.slider(
        "⏰ Hour Range",
        min_value=0,
        max_value=23,
        value=(0, 23),
    )

    # -------------------------
    # Apply Filters
    # -------------------------

    filtered_df = df.copy()

    filtered_df = filtered_df[
        filtered_df["month_name"].isin(selected_months)
    ]

    filtered_df = filtered_df[
        filtered_df["user_type"].isin(selected_user_types)
    ]

    filtered_df = filtered_df[
        filtered_df["member_gender"].isin(selected_genders)
    ]

    filtered_df = filtered_df[
        filtered_df["weekday"].isin(selected_weekdays)
    ]

    filtered_df = filtered_df[
        (filtered_df["hour"] >= hour_range[0])
        &
        (filtered_df["hour"] <= hour_range[1])
    ]

    st.sidebar.markdown("---")

    st.sidebar.metric(
        "🚴 Filtered Trips",
        f"{len(filtered_df):,}"
    )

    st.sidebar.metric(
        "🚲 Bikes",
        filtered_df["bike_id"].nunique()
    )

    st.sidebar.metric(
        "🚉 Stations",
        filtered_df["start_station_name"].nunique()
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
### 📊 Dashboard Info

**Dataset:** Ford GoBike 2018

**Records:** 1.86 Million+

**Developer:** Priya Chavan

**Version:** 1.0
"""
    )

    return filtered_df