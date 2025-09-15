# Weather-Trend-Forecasting
🌦 Weather Forecasting App built with Streamlit and ARIMA. Visualize historical temperature trends, forecast future weather per country, and download forecast data. Features interactive charts, dynamic ARIMA modeling, and a clean, modern UI for accurate and insightful weather predictions.

# Live App : https://weather-trend-forecasting-wsqguqrr5mcwain6kbhfdp.streamlit.app/

# *🌍 Weather & Climate Forecasting Project – Detailed Workflow*

# **1. Data Acquisition**

Dataset source: Kaggle – Global Weather Repository.

The dataset contained weather records from multiple countries and cities, including temperature (°C/°F), humidity, wind, pressure, visibility, air quality indicators, and astronomical data.

Records were time-stamped (last_updated) and included geographical details (latitude, longitude, country, location_name).

# **2. Data Cleaning & Preprocessing**

*Handling missing values:*

Missing entries in columns such as air quality and precipitation were filled using interpolation or dropped depending on sparsity.

*Outliers:*

Extreme anomalies were detected using Z-scores and Isolation Forest.

**Example:**

~3,352 anomalies were found in temperature, wind speed, and air quality measures.

These anomalies were later removed to improve model performance.

*Normalization:*

Numerical variables were standardized to align ranges for analysis.

# **3. Exploratory Data Analysis (EDA)**

*Temperature trends:*

Explored daily averages and seasonal variations across countries.

*Air quality patterns:*

Analyzed CO, Ozone, PM2.5, and PM10 levels in relation to weather conditions.

*Geographical spread:*

Identified countries with the highest number of weather records (e.g., Oman, Myanmar, Vietnam).

*Correlation analysis:*

Humidity and air quality indices showed meaningful relationships.

Wind speed was inversely related to pollution in some regions.

*Visualizations:*

*Heatmaps for correlations.*

Line plots for time-series temperature changes.

Bar charts for country-level data availability.

# **4. Advanced EDA – Anomaly Detection**

Used Z-score and Isolation Forest to detect abnormal values in weather metrics.

Identified anomalies such as extreme wind gusts, very high air pollution values, or unrealistic temperatures.

After anomaly removal:

Original dataset shape: 67,038 rows

Cleaned dataset shape: 63,686 rows

**Result: A more reliable dataset for forecasting.**

# **5. Forecasting Models**
   
Baseline Forecasting (ARIMA)

ARIMA (Auto-Regressive Integrated Moving Average) was applied on daily average temperature.

Results:

MAE = 0.073

RMSE = 0.085

Interpretation: The model achieved excellent accuracy, capturing temporal patterns effectively.

Other Forecasting Approaches (Planned/Compared)

Prophet: Handles strong seasonality (daily, monthly, yearly patterns).

LSTM (Neural Network): Can capture non-linear dependencies in long sequences.

Ensemble Models: Combine ARIMA, Prophet, and LSTM to balance strengths and reduce weaknesses.

# **6. Unique Analyses**

*a) Climate Analysis*

Monthly and yearly averages of temperature were analyzed.

Heatmaps showed seasonal temperature fluctuations across years.

Example: Some regions showed clear monsoon/winter patterns.

*b) Environmental Impact*

Correlation between weather (temperature, humidity, wind) and air quality (PM2.5, PM10, CO, NO₂, Ozone).

Findings:

Higher wind speed often coincided with lower PM2.5 concentrations (dispersion effect).

Humidity had a strong impact on particulate matter levels.

*c) Feature Importance*

Used Random Forest to estimate feature importance for predicting temperature.

Key influential features included:

Humidity

Air Quality PM2.5

Wind speed

Pressure levels

*d) Spatial Analysis*

Used geographical data (latitude, longitude, country) to map patterns.

Produced global maps showing:

Average temperature per country.

Air quality index distributions.

Clear geographical variations appeared (e.g., desert countries with higher average temperatures).

# **7. Model Saving & Reuse**

Forecasting models (ARIMA) were saved as .pkl files for later reuse.

Predictions were also exported into .csv for reporting and visualization.

This ensured reproducibility and efficiency in future experiments.

# **8. Key Insights & Outcomes**

Data Quality: Cleaning anomalies improved model stability.

Forecasting Performance: ARIMA gave a strong baseline with very low error.

Environmental Correlations: Weather conditions like wind and humidity showed measurable effects on air pollution.

Feature Importance: Air quality and humidity were strong predictors of temperature variations.

Geographical Patterns: Climate and pollution levels varied significantly across countries.

# **9. Future Extensions**

Train Prophet + LSTM + Ensemble models for improved forecasting.

Add seasonal decomposition to separate trend/seasonality/noise.

Perform country-level climate forecasting (per region instead of globally aggregated).

Explore climate change impact by analyzing multi-year data trends.

# **✅ In short:**

You built a full pipeline → from data cleaning → EDA → anomaly detection → forecasting → environmental & geographical analysis → model saving.

This project not only forecasts temperature but also studies the climate–environment–air quality nexus at a global level.
