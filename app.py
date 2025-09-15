import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from streamlit_option_menu import option_menu
from statsmodels.tsa.arima.model import ARIMA

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="🌦 Weather Forecasting App",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #83a4d4, #b6fbff);
    }
    .main {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #1e3c72;
        font-weight: 700;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1e3c72, #2a5298);
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2a5298, #1e3c72);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# Sidebar Menu
# -------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="📌 Navigation",
        options=["Forecast", "About"],
        icons=["bar-chart-line", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# -------------------------------
# Forecast Page
# -------------------------------
if selected == "Forecast":
    st.title("🌍 Weather Forecasting Dashboard")
    st.markdown("#### Powered by **ARIMA Model** & Historical Weather Data")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload your weather CSV file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df["last_updated"] = pd.to_datetime(df["last_updated"])
        
        # Sidebar settings for Forecast page
        country = st.sidebar.selectbox("🌐 Select Country", df["country"].unique())
        forecast_days = st.sidebar.slider("📅 Forecast horizon (days)", 7, 90, 30)

        # Filtered country data
        country_df = df[df["country"] == country].sort_values("last_updated")

        if len(country_df) < 30:
            st.warning("Not enough historical data for this country to forecast accurately.")
        else:
            # Train ARIMA Model dynamically per country
            @st.cache_resource
            def train_arima(data):
                ts = data["temperature_celsius"]
                model = ARIMA(ts, order=(5,1,0))
                model_fit = model.fit()
                return model_fit

            model = train_arima(country_df)

            # Forecast
            forecast = model.get_forecast(steps=forecast_days)
            forecast_df = forecast.summary_frame()[["mean"]].rename(columns={"mean": "Forecasted_Temperature"})
            forecast_df["Date"] = pd.date_range(
                start=country_df["last_updated"].max() + timedelta(days=1),
                periods=forecast_days
            )

            # Layout: historical vs forecast
            col1, col2 = st.columns(2)

            with col1:
                st.subheader(f"📈 Historical Trend: {country}")
                st.line_chart(country_df.set_index("last_updated")["temperature_celsius"])

            with col2:
                st.subheader(f"🔮 Forecast ({forecast_days} days)")
                st.dataframe(forecast_df, use_container_width=True)

            # Chart: Historical + Forecast
            st.subheader(f"🌡 Temperature Forecast - {country}")
            fig, ax = plt.subplots(figsize=(11, 5))
            ax.plot(country_df["last_updated"], country_df["temperature_celsius"], label="Historical", color="#1e3c72", linewidth=2)
            ax.plot(forecast_df["Date"], forecast_df["Forecasted_Temperature"], marker="o", color="#ff6b6b", label="Forecast", linewidth=2)
            ax.set_title(f"Forecast for {country}", fontsize=16, weight="bold")
            ax.set_xlabel("Date")
            ax.set_ylabel("Temperature (°C)")
            ax.legend()
            plt.xticks(rotation=45)
            st.pyplot(fig)

            # Download forecast
            csv = forecast_df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Forecast Data", csv, "forecast.csv", "text/csv")

    else:
        st.info("Please upload a CSV file to continue.")

# -------------------------------
# About Page
# -------------------------------
elif selected == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
    This **Weather Forecasting App** was built with:
    - 🧠 ARIMA Model (Time Series Forecasting)
    - 📊 Pandas & Matplotlib
    - 🎨 Streamlit for modern UI

    **How it works:**
    1. Upload historical weather data.  
    2. Train ARIMA model to predict future trends.  
    3. Display results with interactive charts.  

    🔮 Future Upgrades:
    - Humidity & Rainfall Forecasting  
    - Interactive Maps with Folium  
    - Deep Learning models (LSTMs, Transformers)  
    """)

    # Divider
    st.markdown("---")

    # Developer Card
    st.markdown("""
    <div style="background-color:#f8f9fa; padding:20px; border-radius:15px; text-align:center; box-shadow: 0px 4px 8px rgba(0,0,0,0.1);">
        <h2 style="color:#333;">👨‍💻 Developer</h2>
        <h3 style="margin-top:10px; color:#0078D7;">ASAD AZIZ</h3>
        <p style="color:gray;">Student of BS-Artificial Intelligence | AI Enthusiast | Developer</p>
        <a href="https://github.com/Asad-Aziz-001" target="_blank" style="margin:10px; text-decoration:none;">🐙 GitHub</a> |
        <a href="https://www.linkedin.com/in/asad-aziz-140p" target="_blank" style="margin:10px; text-decoration:none;">💼 LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)
