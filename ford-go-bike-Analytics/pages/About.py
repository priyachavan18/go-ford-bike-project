import streamlit as st

from components.theme import apply_theme

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
)

apply_theme()

st.title("ℹ️ About This Project")

st.markdown("""
## 🚴 Ford GoBike Analytics Dashboard

### Project Objective
Analyze the Ford GoBike bike-sharing dataset to uncover rider behavior, station performance, and operational insights.

### Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- Folium
- Scikit-learn

### Key Features

- Executive Dashboard
- Customer Analytics
- Station Analytics
- Time Analysis
- Geographic Analysis
- Business Insights

### Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Dashboard Development
- Data Visualization
- Business Intelligence

---

Developed as a portfolio project to demonstrate end-to-end data analytics skills.
""")