import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

model = joblib.load("Logistic_Regression_hearDisease.pkl")
scaler = joblib.load("scaler_heart.pkl")
expected_columns = joblib.load("columns_hear.pkl")

st.title("🩺 Heart Disease Prediction")
st.write("Enter patient details below.")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 10, 100, 30)
        sex = st.selectbox("Sex", ["M", "F"])
        chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
        exercise_angina = st.selectbox("Exercise Angina", ["N", "Y"])
        st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    with col2:
        resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
        cholesterol = st.number_input("Cholesterol", 100, 600, 200)
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
        max_hr = st.slider("Maximum Heart Rate", 60, 220, 150)
        oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 1.0)

    submitted = st.form_submit_button("Predict")

if submitted:

    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_"+sex: 1,
        "ChestPainType_"+chest_pain_type: 1,
        "RestingECG_"+resting_ecg: 1,
        "ExerciseAngina_"+exercise_angina: 1,
        "ST_Slope_"+st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    st.divider()

    if prediction == 1: 
        st.error("⚠️ You are at high risk of heart disease") 
    else: 
        st.success("✅ You are not at risk of heart disease")
