import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

DB_NAME = "ecobridge.db"

st.set_page_config(
    page_title="EcoBridge Dashboard",
    page_icon="🌱",
    layout="wide"
)

# ===========================
# Custom CSS
# ===========================

st.markdown("""
<style>

.main {
    background-color: #F7F9FC;
}

h1{
    color:#2E7D32;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.title("🌱 EcoBridge Sustainability Dashboard")
st.caption("Energy-Efficient AI Routing Analytics")

# ===========================
# Load Database
# ===========================

conn = sqlite3.connect(DB_NAME)

try:
    df = pd.read_sql_query("SELECT * FROM requests", conn)
except:
    st.warning("Database not found.")
    st.stop()

conn.close()

if df.empty:
    st.info("No requests yet.")
    st.stop()

# ===========================
# KPI
# ===========================

avg_energy = df["energy_score"].mean()
avg_response = df["response_time_ms"].mean()

total_cost = df["estimated_cost_usd"].sum()
saved_cost = df["estimated_cost_saved_usd"].sum()

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric(
    "📦 Requests",
    len(df)
)

c2.metric(
    "⚡ Avg Energy",
    f"{avg_energy:.2f}"
)

c3.metric(
    "💵 Total Cost",
    f"${total_cost:.6f}"
)

c4.metric(
    "🌱 Cost Saved",
    f"${saved_cost:.6f}"
)

c5.metric(
    "⏱ Avg Response",
    f"{avg_response:.0f} ms"
)

st.divider()

# ===========================
# Charts Row 1
# ===========================

left,right = st.columns(2)

with left:

    fig = px.pie(
        df,
        names="classification",
        title="Prompt Classification",
        hole=0.55,
        color="classification",
        color_discrete_map={
            "simple":"#4CAF50",
            "complex":"#F57C00"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    model = df["selected_model"].value_counts().reset_index()
    model.columns=["Model","Count"]

    fig = px.bar(
        model,
        x="Model",
        y="Count",
        title="Model Usage",
        color="Model"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===========================
# Charts Row 2
# ===========================

left,right = st.columns(2)

with left:

    fig = px.line(
        df,
        y="estimated_cost_usd",
        title="Estimated API Cost"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.line(
        df,
        y="response_time_ms",
        title="Response Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===========================
# Charts Row 3
# ===========================

left,right = st.columns(2)

with left:

    fig = px.line(
        df,
        y="energy_score",
        title="Energy Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    routing = pd.DataFrame({
        "Metric":[
            "Energy Saved",
            "Cost Saved"
        ],
        "Value":[
            df["energy_saved_score"].sum(),
            df["estimated_cost_saved_usd"].sum()
        ]
    })

    fig = px.bar(
        routing,
        x="Metric",
        y="Value",
        title="EcoBridge Savings"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===========================
# Recent Requests
# ===========================

st.divider()

st.subheader("📋 Recent Requests")

st.dataframe(

    df[
        [
            "timestamp",
            "prompt",
            "classification",
            "selected_model",
            "energy_score",
            "estimated_cost_usd",
            "response_time_ms"
        ]
    ].head(10),

    use_container_width=True,
    hide_index=True

)