
import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure", 0, 100)
monthly = st.number_input("Monthly Charges", 0.0, 1000.0)
total = st.number_input("Total Charges", 0.0, 100000.0)

if st.button("Predict"):
    input_df = pd.DataFrame([{
        'tenure': tenure,
        'MonthlyCharges': monthly,
        'TotalCharges': total
    }])

    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model.feature_names_in_]

    pred = model.predict(input_df)[0]

    if pred == 1:
        st.error("Will Churn")
    else:
        st.success("Will Stay")
