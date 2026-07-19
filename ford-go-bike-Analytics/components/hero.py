import streamlit as st


def show_hero():

    st.markdown(
        """
<div class="hero">

<h1>🚴 Ford GoBike Analytics Dashboard</h1>

<h4>
Interactive Business Intelligence Platform
</h4>

<br>

Analyze more than

<h2>1.86 Million Bike Trips</h2>

using interactive dashboards,
business insights and
advanced visualizations.

</div>
""",
        unsafe_allow_html=True,
    )