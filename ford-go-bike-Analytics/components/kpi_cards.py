import streamlit as st
import pandas as pd


def show_kpis(df: pd.DataFrame):

    total_trips = len(df)

    total_bikes = df["bike_id"].nunique()

    total_start_stations = df["start_station_name"].nunique()

    avg_trip = df["trip_minutes"].mean()

    members = (df["user_type"] == "Subscriber").sum()

    customers = (df["user_type"] == "Customer").sum()

    peak_hour = (
        df["hour"]
        .value_counts()
        .idxmax()
    )

    avg_daily = (
        df.groupby(
            df["start_time"].dt.date
        )
        .size()
        .mean()
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        card("🚴", "Total Trips", f"{total_trips:,}")

    with c2:

        card("🚲", "Total Bikes", f"{total_bikes:,}")

    with c3:

        card("🚉", "Stations", f"{total_start_stations:,}")

    with c4:

        card("⏱", "Avg Trip", f"{avg_trip:.1f} min")

    c5, c6, c7, c8 = st.columns(4)

    with c5:

        card("👥", "Subscribers", f"{members:,}")

    with c6:

        card("🙋", "Customers", f"{customers:,}")

    with c7:

        card("⏰", "Peak Hour", f"{peak_hour}:00")

    with c8:

        card("📈", "Avg Daily Trips", f"{avg_daily:,.0f}")


def card(icon, label, value):

    st.markdown(
        f"""
<div class="kpi-card">

<div style="font-size:45px">{icon}</div>

<div class="kpi-value">{value}</div>

<div class="kpi-label">

{label}

</div>

</div>
""",
        unsafe_allow_html=True,
    )