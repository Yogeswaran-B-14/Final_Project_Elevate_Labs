# ⚡ Electric Vehicle Demand Forecasting – India (2025)

This project focuses on **forecasting the demand for Electric Vehicles (EVs) in India** using machine learning and time series analysis. It combines real-time-like simulated data, Random Forest regression, and ARIMA-based time series forecasting to derive actionable insights.

---

## 📄 Table of Contents

- [📌 Abstract](#-abstract)
- [🛠️ Tools Used](#️-tools-used)
- [🔁 Steps Involved](#-steps-involved)
- [📈 Modeling Techniques](#-modeling-techniques)
- [🚀 Deployment](#-deployment)
- [🧾 Conclusion](#-conclusion)

---

## 📌 Abstract

Electric Vehicles are reshaping the transportation landscape in India. This project aims to predict the **daily EV usage count** in major cities by analyzing charging station availability, weather patterns, and traffic congestion.

By combining machine learning and ARIMA-based time series forecasting, this project helps understand trends and enables better infrastructure planning and investment.

---

## 🛠️ Tools Used

- **Python** (pandas, scikit-learn, statsmodels, matplotlib, seaborn)
- **Jupyter Notebook** for prototyping
- **Tableau** for visualization
- **Streamlit** for deploying the prediction model as a web app
- **Google Colab** for cloud-based development
- **GitHub** for version control

---

## 🔁 Steps Involved

1. **Data Collection**:  
   Simulated data includes:
   - Charging Station Availability (`charging_stations.csv`)
   - Weather Data (`weather_data.csv`)
   - Traffic Congestion Levels (`traffic_data.csv`)
   - Simulated Usage Count (`simulated_ev_usage_india.csv`)

2. **Data Preprocessing**:  
   - Handling missing values
   - Encoding categorical variables (e.g., city names)
   - Feature scaling and transformation
   - Merging datasets based on `city` and `date`

3. **Exploratory Data Analysis (EDA)**:  
   - Analyzing trends in EV usage across cities
   - Correlation between EV usage and temperature, traffic, charging stations
   - Visualizations via Tableau and Python

4. **Model Building**:
   - **Random Forest Regressor** for short-term EV usage prediction
   - **ARIMA Time Series Model** for long-term trend analysis

5. **Evaluation**:
   - RMSE, MAE, and R² metrics used for model validation

---

## 📈 Modeling Techniques

### 1. 🎯 Random Forest Regressor
- Input Features: `charging_station_count`, `average_temperature`, `traffic_index`, `city_encoded`
- Output: Predicted EV usage count
- Trained and serialized as `ev_random_forest_model.pkl`

### 2. ⏳ ARIMA (Time Series)
- Used on `simulated_ev_usage_india.csv`
- Automatically determined p, d, q parameters
- Plotted future usage forecasts for planning

---

## 🚀 Deployment

### 📦 Streamlit App (via Colab)
- Lightweight web interface to accept new input features
- Model predicts EV usage on-the-fly
- Optionally deployable using `ngrok` with Streamlit in Colab

---

## 🧾 Conclusion

This EV Demand Forecasting project provides a robust, data-driven framework for **predicting electric vehicle usage** in Indian cities. It bridges **machine learning and time series forecasting**, enabling smart infrastructure and energy planning for the future of e-mobility.

> 📌 Future enhancements: Incorporate live APIs, real-time traffic/weather integration, and city-specific seasonal adjustments.

---

