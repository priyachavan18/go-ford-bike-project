import streamlit as st

from components.theme import apply_theme
from components.sidebar import sidebar_filters
from components.charts import (
    top_routes_chart,
    route_distance_chart,
)

from utils.loader import load_data

st.set_page_config(
    page_title="Route Analysis",
    page_icon="🛣️",
    layout="wide",
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("🛣️ Route Analysis")

st.markdown(
"""
Analyze the most popular travel routes and commuting patterns.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    top_routes_chart(df)

with col2:
    route_distance_chart(df)

st.divider()

st.subheader("📋 Top 20 Routes")

routes = (
    df.groupby(
        [
            "start_station_name",
            "end_station_name"
        ]
    )
    .size()
    .reset_index(name="Trips")
    .sort_values(
        "Trips",
        ascending=False
    )
    .head(20)
)

routes["Route"] = (
    routes["start_station_name"]
    + " → "
    + routes["end_station_name"]
)

st.dataframe(
    routes[
        [
            "Route",
            "Trips"
        ]
    ],
    use_container_width=True,
    hide_index=True,
)