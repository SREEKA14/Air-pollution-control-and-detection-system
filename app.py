import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
import time

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Pollution & Drone System",
    page_icon="🚁",
    layout="wide"
)

# --------------------------------------------------
# Load Models
# --------------------------------------------------

global_model = joblib.load("models/global_xgboost_model.pkl")
cpcb_model = joblib.load("models/cpcb_xgboost_model.pkl")
station_model = joblib.load("models/station_kmeans_model.pkl")
lstm_model = load_model("models/bulletin_lstm_model.h5")

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def decode_pollution(level):
    if level == 0:
        return "LOW"
    elif level == 1:
        return "MODERATE"
    else:
        return "HIGH"

def simulate_drone(level):
    if level == 2:
        return {
            "status": "Activated",
            "altitude": "50 meters",
            "spray": "Micromist ON",
            "coverage": "2 km radius"
        }
    elif level == 1:
        return {
            "status": "Standby",
            "altitude": "30 meters",
            "spray": "OFF",
            "coverage": "Monitoring Mode"
        }
    else:
        return {
            "status": "Inactive",
            "altitude": "Grounded",
            "spray": "OFF",
            "coverage": "None"
        }

# --------------------------------------------------
# UI Layout
# --------------------------------------------------

st.title("🚁 Intelligent Air Pollution & Virtual Drone System")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌫 Enter Pollution Parameters")
    pm25 = st.number_input("PM2.5", value=50.0)
    pm10 = st.number_input("PM10", value=80.0)
    co = st.number_input("CO", value=0.5)
    no2 = st.number_input("NO2", value=30.0)
    so2 = st.number_input("SO2", value=20.0)

with col2:
    st.subheader("📊 System Output")

# --------------------------------------------------
# Button Action
# --------------------------------------------------

if st.button("🚀 Run AI System"):

    # Run detection model
    data = np.array([[pm25, pm10, co, no2, so2]])
    pollution_level = global_model.predict(data)[0]
    pollution_label = decode_pollution(pollution_level)

    st.markdown("## 🔍 Detection Result")

    if pollution_label == "HIGH":
        st.error(f"Pollution Level: {pollution_label}")
    elif pollution_label == "MODERATE":
        st.warning(f"Pollution Level: {pollution_label}")
    else:
        st.success(f"Pollution Level: {pollution_label}")

    # Drone Simulation Panel
    drone_data = simulate_drone(pollution_level)

    st.markdown("## 🚁 Drone Control Panel")

    colA, colB, colC, colD = st.columns(4)
    colA.metric("Status", drone_data["status"])
    colB.metric("Altitude", drone_data["altitude"])
    colC.metric("Spray Mode", drone_data["spray"])
    colD.metric("Coverage", drone_data["coverage"])

    # --------------------------------------------------
    # Pollution Reduction Simulation (Only if HIGH)
    # --------------------------------------------------

    if pollution_label == "HIGH":

        st.subheader("🌫 Micromist Spray Simulation")

        # Show drone animation
        try:
            st.image("drone.gif", width=300)
        except:
            st.warning("Add drone.gif to project folder for animation.")

        with st.spinner("🚁 Spraying micromist..."):
            time.sleep(3)

        before_value = 150
        after_value = 60

        progress_bar = st.progress(0)
        pollution_text = st.empty()

        for i in range(before_value, after_value, -5):
            progress_bar.progress((before_value - i) / (before_value - after_value))
            pollution_text.write(f"Current AQI Level: {i}")
            time.sleep(0.1)

        st.success("✅ Spray Completed Successfully!")

        col1, col2 = st.columns(2)
        col1.metric("Before Spray AQI", before_value)
        col2.metric("After Spray AQI", after_value, delta="-90")

    else:
        st.info("🚁 Drone deployment not required.")


