import streamlit as st

from components.theme import apply_theme
from components.sidebar import sidebar_filters
from components.charts import (
    top_bikes_chart,
    bike_duration_chart,
    bike_usage_distribution,
)
from utils.loader import load_data

st.set_page_config(
    page_title="Bike Utilization",
    page_icon="🚲",
    layout="wide",
)

apply_theme()

df = load_data()
df = sidebar_filters(df)

st.title("🚲 Bike Utilization")

st.markdown(
"""
Analyze bike usage patterns and identify highly utilized bikes.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    top_bikes_chart(df)

with col2:
    bike_duration_chart(df)

st.divider()

bike_usage_distribution(df)