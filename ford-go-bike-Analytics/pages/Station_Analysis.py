import streamlit as st

from components.sidebar import sidebar_filters
from components.theme import apply_theme
from components.charts import top_station_chart
from utils.loader import load_data

st.set_page_config(
    page_title="Station Analysis",
    page_icon="🚉",
    layout="wide"
)

apply_theme()

df = load_data()

df = sidebar_filters(df)

st.title("🚉 Station Analysis")

st.markdown(
"""
Analyze the busiest stations in the Ford GoBike network.
"""
)

st.divider()

top_station_chart(df)

st.divider()

col1, col2 = st.columns(2)

with col1:

    busiest = (
        df["start_station_name"]
        .value_counts()
        .head(15)
    )

    st.subheader("🏆 Top 15 Start Stations")

    st.dataframe(
        busiest,
        use_container_width=True
    )

with col2:

    busiest_end = (
        df["end_station_name"]
        .value_counts()
        .head(15)
    )

    st.subheader("🎯 Top 15 End Stations")

    st.dataframe(
        busiest_end,
        use_container_width=True
    )