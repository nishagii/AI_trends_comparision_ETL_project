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
