import streamlit as st

from components.sidebar import sidebar_filters
from components.theme import apply_theme
from components.charts import (
    station_map,
    top_station_table,
)
from utils.loader import load_data

st.set_page_config(
    page_title="Geographic Analysis",
    page_icon="🗺️",
    layout="wide",
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("🗺️ Geographic Analysis")

st.markdown(
"""
Explore the spatial distribution of stations and identify
areas with the highest demand.
"""
)

st.divider()

station_map(df)

st.divider()

st.subheader("🏆 Top 20 Stations")

top_station_table(df)