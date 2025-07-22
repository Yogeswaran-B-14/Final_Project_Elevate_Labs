
import streamlit as st
import pickle
import numpy as np

st.title("EV Charging Demand Forecasting 🇮🇳")

# Load model
with open("ev_random_forest_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# User Inputs
st.sidebar.header("Input Parameters")
day_of_week = st.sidebar.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 3)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
temperature = st.sidebar.slider("Temperature (°C)", 10, 45, 30)
holiday = st.sidebar.selectbox("Is it a holiday?", ["No", "Yes"])
is_holiday = 1 if holiday == "Yes" else 0
prev_hour_usage = st.sidebar.slider("Previous Hour Usage", 0, 100, 30)

# Combine features (5 inputs)
features = np.array([[day_of_week, hour, temperature, is_holiday, prev_hour_usage]])
predicted_usage = model.predict(features)[0]

st.subheader("📈 Predicted Charging Usage Count:")
st.success(f"{int(predicted_usage)} vehicles")
