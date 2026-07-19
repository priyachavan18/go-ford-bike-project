import streamlit as st

from components.sidebar import sidebar_filters
from components.theme import apply_theme
from components.insights import show_business_insights
from utils.loader import load_data

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide",
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("💡 Business Insights")

st.markdown(
    """
Transform operational data into actionable business decisions.
"""
)

st.divider()

show_business_insights(df)