from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load("models/global_xgboost_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract values
        pm25 = float(data.get('pm25', 0))
        pm10 = float(data.get('pm10', 0))
        co = float(data.get('co', 0))
        no2 = float(data.get('no2', 0))
        so2 = float(data.get('so2', 0))

        # IMPORTANT: Feature order same as training
        features = np.array([[pm25, pm10, co, no2, so2]])

        # Model prediction
        prediction = model.predict(features)[0]

        print("Input:", features)
        print("Model raw prediction:", prediction)

        # 🔥 Hybrid Decision Logic (Best for demo + real world)
        if pm25 > 150 or pm10 > 200:
            pollution_label = "HIGH"
        elif pm25 > 80 or pm10 > 120:
            pollution_label = "MODERATE"
        else:
            pollution_label = "LOW"

        return jsonify({
            "pollution_level": pollution_label,
            "model_prediction_raw": int(prediction),
            "pm25": pm25,
            "pm10": pm10,
            "co": co,
            "no2": no2,
            "so2": so2
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
