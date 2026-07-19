import streamlit as st

from components.theme import apply_theme
from components.hero import show_hero
from utils.loader import load_data
from components.kpi_cards import show_kpis
from utils.loader import load_data

st.set_page_config(page_title="Test")

st.title("Ford GoBike Test")

df = load_data()

st.success("Dataset loaded successfully!")

st.write(df.head())

st.set_page_config(
    page_title="Ford GoBike Analytics",
    page_icon="🚴",
    layout="wide",
)

apply_theme()

df = load_data()

show_hero()

st.markdown(
    '<div class="section-title">Executive Overview</div>',
    unsafe_allow_html=True,
)

show_kpis(df)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Project Overview</div>',
    unsafe_allow_html=True,
)

st.markdown("""
### Features

- 📊 Executive KPIs
- 👥 Rider Behaviour
- 🚉 Station Analytics
- 🛣 Route Analysis
- ⏰ Time Analysis
- 🗺 Geographic Analysis
- 🚲 Bike Utilization
- 💡 Business Insights
""")
