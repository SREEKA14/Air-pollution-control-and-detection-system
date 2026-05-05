#  Intelligent Air Pollution Monitoring & Control System 

##  Overview

This project presents an AI-powered system for **real-time air pollution monitoring and control** using a simulated drone-based approach. It combines machine learning, data visualization, and 3D simulation to detect pollution levels and respond intelligently using a micromist spraying mechanism.

The system classifies pollution levels and simulates an autonomous drone that sprays optimized mist to reduce pollution, along with real-time dashboards, alerts, and report generation.

---

## 🎯 Objectives

* Detect and classify air pollution levels using AI
* Simulate automated drone-based pollution control
* Provide real-time monitoring through dashboards
* Generate intelligent mist composition recommendations
* Enable report generation for analysis

---

## 🧠 Models Used

### 🔹 XGBoost

* Used for pollution classification (LOW, MODERATE, HIGH)
* High accuracy for structured environmental data

### 🔹 LSTM

* Used for time-series pollution trend prediction
* Captures temporal patterns in pollution data

### 🔹 K-Means Clustering

* Used for grouping monitoring stations based on pollution patterns
* Helps identify high-risk zones

---

## ⚙️ Techniques & Technologies

* **Hybrid Decision System** (AI + Threshold logic)
* **Three.js** – 3D drone simulation
* **Chart.js** – Real-time pollution trend graph
* **Gauge.js** – AQI meter visualization
* **Flask API** – Backend prediction service
* **jsPDF** – Downloadable report generation
* **JavaScript (Fetch API)** – Frontend-backend communication

---

## 🚁 System Workflow

1. User inputs pollution values
2. Data is sent to backend (Flask API)
3. AI model predicts pollution level
4. Alert is triggered if pollution is high
5. Drone moves to polluted area
6. Micromist is sprayed
7. Pollution reduces visually
8. Dashboard updates in real time
9. Report can be downloaded

---

## 📊 Features

* Real-time pollution detection
* 3D drone simulation
* Micromist spraying mechanism
* Live dashboard with AQI gauge
* Alert system (visual + audio)
* AI-based mist optimization
* Downloadable PDF report

---

## 🧪 Micromist Optimization

### Mist Calculation:

Mist quantity is calculated based on pollution levels:

Mist = (PM2.5 × 0.5) + (PM10 × 0.3) + (CO × 20) + (NO2 × 0.2) + (SO2 × 0.2)

### Composition:

* Water (H₂O) – 70%
* Neutralizer – 15%
* Oxidizer – 10%
* Additives – 5%

### Purpose:

* Water captures particulate matter
* Neutralizers reduce acidic gases
* Oxidizers break down harmful gases
* Additives improve efficiency

---

## 🖥️ Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: Python (Flask)
* ML Models: XGBoost, LSTM, K-Means
* Visualization: Three.js, Chart.js, Gauge.js

---

## 🚀 How to Run

### Backend

```bash
python backend.py
```

### Frontend

```bash
cd frontend
python -m http.server 8000
```

Open in browser:

```
http://localhost:8000
```

---

## 🌟 Future Scope

* Integration with real IoT sensors
* Real drone deployment
* Advanced chemical optimization models
* Multi-location pollution monitoring
* Mobile app integration

---

## 🏆 Conclusion

This project demonstrates how AI, simulation, and automation can be combined to build an intelligent system for environmental monitoring and pollution control. It provides a scalable solution for smart city applications and sustainable development.

---

