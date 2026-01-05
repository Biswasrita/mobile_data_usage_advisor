import streamlit as st
import pandas as pd
import joblib
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "usage_model.pkl")
encoder_path = os.path.join(BASE_DIR, "model", "le_target.pkl")

model = joblib.load(model_path)
le_target = joblib.load(encoder_path)

st.set_page_config(page_title="Mobile Data Usage Advisor", layout="centered")

st.title("📶 Smart Mobile Data Usage Advisor")
st.write("Predict your mobile data usage risk using machine learning")

st.divider()


screen_time = st.slider(
    "📱 Screen-on time (hours per day)",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

app_time = st.slider(
    "⏱️ App usage time (minutes per day)",
    min_value=0,
    max_value=1000,
    value=300
)

data_usage = st.slider(
    "📊 Mobile data usage (MB per day)",
    min_value=0,
    max_value=5000,
    value=800
)

if st.button("Analyze Usage"):
    input_df = pd.DataFrame({
        "Screen On Time (hours/day)": [screen_time],
        "App Usage Time (min/day)": [app_time],
        "Data Usage (MB/day)": [data_usage]
    })

    prediction = model.predict(input_df)[0]
    risk = le_target.inverse_transform([prediction])[0]

    st.subheader(" Result")

    if risk == "Safe":
        st.success(" Safe usage – your data usage is under control")
    elif risk == "Warning":
        st.warning(" Warning – consider reducing heavy apps")
    else:
        st.error(" High Risk – data may finish quickly")

    st.info(f"Predicted Risk Level: **{risk}**")

