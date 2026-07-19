import plotly.express as px
import streamlit as st
import pandas as pd

def monthly_trips_chart(df: pd.DataFrame):

    monthly = (
        df.groupby("month_name")
        .size()
        .reset_index(name="Trips")
    )

    month_order = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    monthly["month_name"] = pd.Categorical(
        monthly["month_name"],
        categories=month_order,
        ordered=True,
    )

    monthly = monthly.sort_values("month_name")

    fig = px.line(
        monthly,
        x="month_name",
        y="Trips",
        markers=True,
        title="Monthly Trips",
    )

    fig.update_layout(
        height=420,
        template="plotly_dark",
        margin=dict(l=20, r=20, t=50, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)

def hourly_demand_chart(df: pd.DataFrame):

     hourly = (
        df.groupby("hour")
        .size()
        .reset_index(name="Trips")
    )

     fig = px.bar(
        hourly,
        x="hour",
        y="Trips",
        title="Trips by Hour",
    )

     fig.update_layout(
        template="plotly_dark",
        height=420,
    )

     st.plotly_chart(fig, use_container_width=True)

def user_type_chart(df: pd.DataFrame):

     users = (
        df["user_type"]
        .value_counts()
        .reset_index()
    )

     users.columns = ["User Type", "Trips"]

     fig = px.pie(
        users,
        names="User Type",
        values="Trips",
        hole=0.6,
        title="User Distribution",
    )

     fig.update_layout(
        template="plotly_dark",
        height=420,
    )

     st.plotly_chart(fig, use_container_width=True)

def trip_duration_chart(df: pd.DataFrame):

     fig = px.histogram(
        df,
        x="trip_minutes",
        nbins=50,
        title="Trip Duration Distribution",
    )

     fig.update_layout(
        template="plotly_dark",
        height=420,
    )

     st.plotly_chart(fig, use_container_width=True)

def top_station_chart(df: pd.DataFrame):

     stations = (
        df["start_station_name"]
        .value_counts()
        .head(10)
        .reset_index()
    )

     stations.columns = ["Station", "Trips"]

     fig = px.bar(
        stations,
        x="Trips",
        y="Station",
        orientation="h",
        title="Top 10 Stations",
    )

     fig.update_layout(
        template="plotly_dark",
        height=500,
        yaxis=dict(categoryorder="total ascending"),
    )

     st.plotly_chart(fig, use_container_width=True)

def user_type_chart(df):

    users = (
        df["user_type"]
        .value_counts()
        .reset_index()
    )

    users.columns = ["User Type", "Trips"]

    fig = px.pie(
        users,
        names="User Type",
        values="Trips",
        hole=0.6,
        title="User Type Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

def gender_chart(df):

    gender = (
        df["member_gender"]
        .dropna()
        .value_counts()
        .reset_index()
    )

    gender.columns = ["Gender", "Trips"]

    fig = px.bar(
        gender,
        x="Gender",
        y="Trips",
        text="Trips",
        title="Gender Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

def age_distribution_chart(df):

    age_df = df[
        (df["age"] > 10) &
        (df["age"] < 90)
    ]

    fig = px.histogram(
        age_df,
        x="age",
        nbins=30,
        title="Age Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

def duration_by_user_chart(df):

    duration = (
        df.groupby("user_type")["trip_minutes"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        duration,
        x="user_type",
        y="trip_minutes",
        text_auto=".1f",
        title="Average Trip Duration"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        xaxis_title="User Type",
        yaxis_title="Minutes"
    )

    st.plotly_chart(fig, use_container_width=True)

def hourly_demand_chart(df):

    hourly = (
        df.groupby("hour")
        .size()
        .reset_index(name="Trips")
    )

    fig = px.line(
        hourly,
        x="hour",
        y="Trips",
        markers=True,
        title="Trips by Hour"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        xaxis_title="Hour of Day",
        yaxis_title="Trips"
    )

    st.plotly_chart(fig, use_container_width=True)

def weekday_chart(df):

    order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    weekday = (
        df.groupby("weekday")
        .size()
        .reset_index(name="Trips")
    )

    weekday["weekday"] = pd.Categorical(
        weekday["weekday"],
        categories=order,
        ordered=True
    )

    weekday = weekday.sort_values("weekday")

    fig = px.bar(
        weekday,
        x="weekday",
        y="Trips",
        text="Trips",
        title="Trips by Weekday"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

def monthly_trips_chart(df):

    order = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    monthly = (
        df.groupby("month_name")
        .size()
        .reset_index(name="Trips")
    )

    monthly["month_name"] = pd.Categorical(
        monthly["month_name"],
        categories=order,
        ordered=True
    )

    monthly = monthly.sort_values("month_name")

    fig = px.area(
        monthly,
        x="month_name",
        y="Trips",
        title="Monthly Trips"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

def weekend_chart(df):

    weekend = (
        df.groupby("is_weekend")
        .size()
        .reset_index(name="Trips")
    )

    weekend["is_weekend"] = weekend["is_weekend"].map({
        False: "Weekday",
        True: "Weekend"
    })

    fig = px.pie(
        weekend,
        names="is_weekend",
        values="Trips",
        hole=0.6,
        title="Weekend vs Weekday Trips"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

import folium
from streamlit_folium import st_folium


def station_map(df):

    stations = (
        df.groupby("start_station_name")
        .agg(
            Latitude=("start_station_latitude", "first"),
            Longitude=("start_station_longitude", "first"),
            Trips=("start_station_name", "count"),
        )
        .reset_index()
    )

    m = folium.Map(
        location=[37.77, -122.42],
        zoom_start=12,
        tiles="CartoDB positron",
    )

    for _, row in stations.iterrows():

        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=max(3, min(row["Trips"] / 1000, 15)),
            popup=f"""
            <b>{row['start_station_name']}</b><br>
            Trips: {row['Trips']:,}
            """,
            color="blue",
            fill=True,
            fill_opacity=0.7,
        ).add_to(m)

    st_folium(
        m,
        width=None,
        height=650,
    )

def top_station_table(df):

    stations = (
        df["start_station_name"]
        .value_counts()
        .head(20)
        .reset_index()
    )

    stations.columns = [
        "Station",
        "Trips"
    ]

    st.dataframe(
        stations,
        use_container_width=True,
        hide_index=True,
    )

def top_routes_chart(df):

    routes = (
        df.groupby(
            [
                "start_station_name",
                "end_station_name"
            ]
        )
        .size()
        .reset_index(name="Trips")
        .sort_values(
            "Trips",
            ascending=False
        )
        .head(15)
    )

    routes["Route"] = (
        routes["start_station_name"]
        + " → " +
        routes["end_station_name"]
    )

    fig = px.bar(
        routes,
        x="Trips",
        y="Route",
        orientation="h",
        text="Trips",
        title="Top 15 Most Popular Routes",
    )

    fig.update_layout(
        template="plotly_dark",
        height=650,
        yaxis=dict(categoryorder="total ascending"),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

def route_distance_chart(df):

    routes = (
        df.groupby(
            [
                "start_station_name",
                "end_station_name"
            ]
        )["trip_minutes"]
        .mean()
        .reset_index()
        .sort_values(
            "trip_minutes",
            ascending=False
        )
        .head(15)
    )

    routes["Route"] = (
        routes["start_station_name"]
        + " → " +
        routes["end_station_name"]
    )

    fig = px.bar(
        routes,
        x="trip_minutes",
        y="Route",
        orientation="h",
        text_auto=".1f",
        title="Average Trip Duration by Route",
    )

    fig.update_layout(
        template="plotly_dark",
        height=650,
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Minutes",
        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

def top_bikes_chart(df):

    bikes = (
        df["bike_id"]
        .value_counts()
        .head(20)
        .reset_index()
    )

    bikes.columns = ["Bike ID", "Trips"]

    fig = px.bar(
        bikes,
        x="Bike ID",
        y="Trips",
        text="Trips",
        title="Top 20 Most Used Bikes"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        xaxis_title="Bike ID",
        yaxis_title="Trips"
    )

    st.plotly_chart(fig, use_container_width=True)

def bike_duration_chart(df):

    duration = (
        df.groupby("bike_id")["trip_minutes"]
        .mean()
        .reset_index()
        .sort_values(
            "trip_minutes",
            ascending=False
        )
        .head(20)
    )

    fig = px.bar(
        duration,
        x="bike_id",
        y="trip_minutes",
        text_auto=".1f",
        title="Average Trip Duration by Bike"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        xaxis_title="Bike ID",
        yaxis_title="Minutes"
    )

    st.plotly_chart(fig, use_container_width=True)

def bike_usage_distribution(df):

    usage = (
        df["bike_id"]
        .value_counts()
        .reset_index()
    )

    usage.columns = ["Bike ID", "Trips"]

    fig = px.histogram(
        usage,
        x="Trips",
        nbins=40,
        title="Bike Usage Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        xaxis_title="Trips per Bike",
        yaxis_title="Number of Bikes"
    )

    st.plotly_chart(fig, use_container_width=True)

