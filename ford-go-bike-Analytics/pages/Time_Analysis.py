import streamlit as st

from components.sidebar import sidebar_filters
from components.theme import apply_theme
from components.charts import (
    hourly_demand_chart,
    weekday_chart,
    monthly_trips_chart,
    weekend_chart,
)
from utils.loader import load_data

st.set_page_config(
    page_title="Time Analysis",
    page_icon="⏰",
    layout="wide",
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("⏰ Time Analysis")

st.markdown(
"""
Analyze demand patterns across hours, weekdays, and months.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    hourly_demand_chart(df)

with col2:
    weekday_chart(df)

st.divider()

col3, col4 = st.columns(2)

with col3:
    monthly_trips_chart(df)

with col4:
    weekend_chart(df)