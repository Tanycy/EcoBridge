import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("ecobridge.db")
df = pd.read_sql_query("SELECT * FROM requests", conn)

st.title("EcoBridge Dashboard")

st.metric("Total Requests", len(df))
st.metric("Total Energy Used", round(df["energy"].sum(), 2))
st.metric("Total Carbon Emission", round(df["carbon"].sum(), 2))

st.subheader("Simple vs Complex Requests")
st.bar_chart(df["classification"].value_counts())

st.subheader("Model Usage")
st.bar_chart(df["model"].value_counts())

st.subheader("Energy Consumption")
st.line_chart(df["energy"])
