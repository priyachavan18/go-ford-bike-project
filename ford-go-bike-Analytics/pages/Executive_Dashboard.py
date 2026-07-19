import streamlit as st

from components.sidebar import sidebar_filters
from components.theme import apply_theme
from components.kpi_cards import show_kpis
from components.charts import (
    monthly_trips_chart,
    hourly_demand_chart,
    user_type_chart,
    trip_duration_chart,
    top_station_chart,
)
from utils.loader import load_data

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide",
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("📊 Executive Dashboard")

show_kpis(df)

st.divider()

col1, col2 = st.columns(2)

with col1:
    monthly_trips_chart(df)

with col2:
    hourly_demand_chart(df)

col3, col4 = st.columns(2)

with col3:
    user_type_chart(df)

with col4:
    trip_duration_chart(df)

st.divider()

top_station_chart(df)