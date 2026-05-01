import joblib
import numpy as np
from tensorflow.keras.models import load_model

# Load models
global_model = joblib.load("models/global_xgboost_model.pkl")
cpcb_model = joblib.load("models/cpcb_xgboost_model.pkl")
station_model = joblib.load("models/station_kmeans_model.pkl")
from tensorflow.keras.models import load_model
lstm_model = load_model("models/bulletin_lstm_model.h5")


print("All models loaded successfully ✅")

# --------------------------------------------------
# 1️⃣ Pollution Detection (Global Model)
# --------------------------------------------------

def detect_pollution(pm25, pm10, co, no2, so2):
    data = np.array([[pm25, pm10, co, no2, so2]])
    prediction = global_model.predict(data)
    return prediction[0]

# --------------------------------------------------
# 2️⃣ AQI Classification (CPCB Model)
# --------------------------------------------------

def classify_aqi(aqi):
    data = np.array([[aqi]])
    prediction = cpcb_model.predict(data)
    return prediction[0]

# --------------------------------------------------
# 3️⃣ Future Prediction (LSTM)
# --------------------------------------------------

def predict_future_aqi(sequence):
    sequence = np.array(sequence).reshape(1, len(sequence), 1)
    prediction = lstm_model.predict(sequence)
    return prediction[0][0]

# --------------------------------------------------
# 4️⃣ Station Risk Clustering
# --------------------------------------------------

def cluster_station(state_encoded, city_encoded, status_encoded):
    data = np.array([[state_encoded, city_encoded, status_encoded]])
    cluster = station_model.predict(data)
    return cluster[0]

# --------------------------------------------------
# 5️⃣ Decision Engine (Drone Logic)
# --------------------------------------------------

def drone_decision(pollution_level):
    if pollution_level == 2:  # HIGH
        return "🚨 Activate Virtual Drone Micromist Spraying"
    elif pollution_level == 1:  # MODERATE
        return "⚠ Monitor Area - Prepare Drone"
    else:
        return "✅ Air Quality Safe - No Action Needed"

def decode_pollution(level):
    if level == 0:
        return "LOW"
    elif level == 1:
        return "MODERATE"
    else:
        return "HIGH"


# --------------------------------------------------
# Example Run
# --------------------------------------------------

pollution_level = detect_pollution(120, 180, 0.8, 40, 20)
decision = drone_decision(pollution_level)

pollution_label = decode_pollution(pollution_level)

print("Pollution Level:", pollution_label)
print("Drone Action:", decision)

