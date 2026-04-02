
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details below:")

# Inputs
tenure = st.number_input("Tenure (months)", 0, 100)
monthly = st.number_input("Monthly Charges", 0.0, 10000.0)
total = st.number_input("Total Charges", 0.0, 100000.0)

if st.button("Predict"):

    input_df = pd.DataFrame([{
        'tenure': tenure,
        'MonthlyCharges': monthly,
        'TotalCharges': total
    }])

    # Handle missing columns
    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Likely to churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Likely to stay (Probability: {prob:.2f})")
