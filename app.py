import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details below:")

# ---------- NUMERIC INPUTS ---------- #

age = st.slider("Age", 10, 100, 30)
tenure = st.slider("Tenure", 0, 72, 12)
usage = st.number_input("Usage Frequency", 0, 100)
support_calls = st.slider("Support Calls", 0, 10, 1)
payment_delay = st.slider("Payment Delay", 0, 30, 0)
total_spend = st.number_input("Total Spend", 0.0, 100000.0)
last_interaction = st.number_input("Last Interaction (days)", 0, 365)

# ---------- DROPDOWNS ---------- #

gender = st.selectbox("Gender", ["Male", "Female"])
subscription = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])

# ---------- PREDICT ---------- #

if st.button("Predict"):

    input_dict = {
        "Age": age,
        "Tenure": tenure,
        "Usage Frequency": usage,
        "Support Calls": support_calls,
        "Payment Delay": payment_delay,
        "Total Spend": total_spend,
        "Last Interaction": last_interaction,

        # Gender
        "Gender_Male": 1 if gender == "Male" else 0,
        "Gender_Female": 1 if gender == "Female" else 0,

        # Subscription
        "Subscription Type_Basic": 1 if subscription == "Basic" else 0,
        "Subscription Type_Standard": 1 if subscription == "Standard" else 0,
        "Subscription Type_Premium": 1 if subscription == "Premium" else 0,

        # Contract
        "Contract Length_Monthly": 1 if contract == "Monthly" else 0,
        "Contract Length_Quarterly": 1 if contract == "Quarterly" else 0,
        "Contract Length_Annual": 1 if contract == "Annual" else 0,
    }

    input_df = pd.DataFrame([input_dict])

    # Ensure correct order
    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("Result")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer Will Stay (Churn Probability: {prob:.2f})")
