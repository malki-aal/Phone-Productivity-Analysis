import streamlit as st
import pandas as pd
import os

st.title("Student Productivity Dashboard")

# ---------------------------
# Load cleaned data
# ---------------------------
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "..", "data", "clean_data.csv")
df = pd.read_csv(file_path)

# ---------------------------
# Show dataset preview
# ---------------------------
st.subheader("Dataset Preview")
st.dataframe(df)

# ---------------------------
# Scatter: Phone Usage vs Productivity
# ---------------------------
st.subheader("Phone Usage vs Productivity")
st.scatter_chart(df, x="phone_usage_hours", y="productivity_score")

# ---------------------------
# Scatter: Sleep vs Productivity
# ---------------------------
st.subheader("Sleep vs Productivity")
st.scatter_chart(df, x="sleep_hours", y="productivity_score")

# ---------------------------
# Filter by sleep hours (interactive)
# ---------------------------
sleep_filter = st.slider("Minimum Sleep Hours", 0, 10, 5)
filtered_df = df[df["sleep_hours"] >= sleep_filter]

st.subheader("Filtered Data by Sleep")
st.dataframe(filtered_df)

st.subheader("Phone Usage vs Productivity (Filtered)")
st.scatter_chart(filtered_df, x="phone_usage_hours", y="productivity_score")