"""
This script creates a Streamlit dashboard to visualize the popularity of ChatGPT over time using a line chart.

Modules:
    - streamlit: Used to create the web application.
    - pandas: Used to handle and manipulate the data.
    - plotly.express: Used to create the line chart.

Data:
    - A DataFrame with a date range from January 2024 to October 2024 and corresponding popularity values for ChatGPT.

Functions:
    - None

Usage:
    Run this script to start a Streamlit web application that displays a line chart of ChatGPT's popularity over time.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Example DataFrame
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=10, freq="M"),
        "ChatGPT": [100, 120, 130, 150, 170, 180, 190, 200, 210, 220],
    }
)

# Create a Plotly figure
fig = px.line(data, x="date", y="ChatGPT", title="ChatGPT Popularity Over Time")

# Streamlit App
st.title("ChatGPT Popularity Dashboard")
st.plotly_chart(fig)
