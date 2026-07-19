import streamlit as st
import pandas as pd


def show_business_insights(df: pd.DataFrame):
    """
    Display executive KPIs, key findings and business recommendations.
    """

    total_trips = len(df)

    total_bikes = df["bike_id"].nunique()

    total_start_stations = df["start_station_name"].nunique()

    avg_duration = df["trip_minutes"].mean()

    peak_hour = int(df["hour"].mode().iloc[0])

    busiest_station = (
        df["start_station_name"]
        .mode()
        .iloc[0]
    )

    subscriber_pct = (
        (df["user_type"] == "Subscriber").mean()
        * 100
    )

    customer_pct = (
        (df["user_type"] == "Customer").mean()
        * 100
    )

    st.header("📈 Executive Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("🚴 Total Trips", f"{total_trips:,}")
    c2.metric("🚲 Bikes", f"{total_bikes:,}")
    c3.metric("🚉 Stations", f"{total_start_stations:,}")

    c4, c5, c6 = st.columns(3)

    c4.metric("⏱ Avg Trip", f"{avg_duration:.1f} min")
    c5.metric("⏰ Peak Hour", f"{peak_hour}:00")
    c6.metric("👥 Subscribers", f"{subscriber_pct:.1f}%")

    st.divider()

    st.subheader("🔍 Key Findings")

    findings = [

        f"• The dataset contains **{total_trips:,} trips**.",

        f"• The network consists of **{total_start_stations} start stations**.",

        f"• The busiest station is **{busiest_station}**.",

        f"• Peak riding demand occurs around **{peak_hour}:00**.",

        f"• Average ride duration is **{avg_duration:.1f} minutes**.",

        f"• Subscribers account for **{subscriber_pct:.1f}%** of all rides.",

        f"• Customers account for **{customer_pct:.1f}%** of all rides."

    ]

    for item in findings:
        st.markdown(item)

    st.divider()

    st.subheader("💡 Business Recommendations")

    recommendations = [

        (
            "🚴 Increase Bike Availability",
            "Deploy additional bikes at the busiest stations during peak commuting hours."
        ),

        (
            "🛠 Preventive Maintenance",
            "Schedule maintenance during low-demand periods to reduce service disruption."
        ),

        (
            "📈 Convert Casual Riders",
            "Offer discounts and loyalty programs to convert Customers into Subscribers."
        ),

        (
            "🗺 Expand Station Network",
            "Identify underserved areas and evaluate opportunities for new station placement."
        ),

        (
            "📊 Real-Time Rebalancing",
            "Use live trip demand to rebalance bikes across stations throughout the day."
        )

    ]

    for title, desc in recommendations:

        with st.container():

            st.info(f"### {title}\n\n{desc}")