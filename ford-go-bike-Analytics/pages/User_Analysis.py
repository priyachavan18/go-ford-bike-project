import streamlit as st

from components.sidebar import sidebar_filters
from components.theme import apply_theme
from components.charts import (
    user_type_chart,
    gender_chart,
    age_distribution_chart,
    duration_by_user_chart,
)
from utils.loader import load_data

st.set_page_config(
    page_title="User Analysis",
    page_icon="👥",
    layout="wide",
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("👥 User Analysis")

st.markdown(
"""
Understand rider demographics and usage patterns.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    user_type_chart(df)

with col2:
    gender_chart(df)

st.divider()

col3, col4 = st.columns(2)

with col3:
    age_distribution_chart(df)

with col4:
    duration_by_user_chart(df)