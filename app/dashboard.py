import streamlit as st
import pandas as pd
import sqlite3

DB_NAME = "ecobridge.db"

st.set_page_config(
    page_title="EcoBridge Dashboard",
    layout="wide"
)

st.title("EcoBridge Sustainability Dashboard")

conn = sqlite3.connect(DB_NAME)

try:
    df = pd.read_sql_query("SELECT * FROM requests", conn)
except Exception:
    st.warning("Database not found or table has not been created yet.")
    st.stop()
finally:
    conn.close()

if df.empty:
    st.info("No request data available yet.")
    st.stop()

col1, col2, col3 = st.columns(3)

col1.metric("Total Requests", len(df))
col2.metric("Energy Used (kWh)", round(df["energy_kwh"].sum(), 6))
col3.metric("Carbon Emissions (g)", round(df["carbon_g"].sum(), 4))

col4, col5, col6 = st.columns(3)

col4.metric("Total Cost (USD)", round(df["cost_usd"].sum(), 6))
col5.metric("Energy Saved (kWh)", round(df["energy_saved_kwh"].sum(), 6))
col6.metric("Cost Saved (USD)", round(df["cost_saved_usd"].sum(), 6))

st.subheader("Simple vs Complex Requests")
st.bar_chart(df["classification"].value_counts())

st.subheader("Model Usage")
st.bar_chart(df["model"].value_counts())

st.subheader("Energy Consumption Over Time")
st.line_chart(df.set_index("timestamp")["energy_kwh"])

st.subheader("Carbon Emissions Over Time")
st.line_chart(df.set_index("timestamp")["carbon_g"])

st.subheader("Cost Savings Over Time")
st.line_chart(df.set_index("timestamp")["cost_saved_usd"])

st.subheader("Request Data")
st.dataframe(df)
