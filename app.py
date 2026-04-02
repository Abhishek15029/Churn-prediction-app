import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("📊 Customer Churn Prediction")
st.write("Fill all details to predict churn")

# Get feature names from model
features = model.feature_names_in_

input_data = {}

st.subheader("Customer Inputs")

# Dynamically create inputs
for feature in features:
    
     # Skip unwanted columns
    if feature.lower() in ["churn", "customerid", "customer_id"]:
        continue
        
    # Numeric features
    if any(x in feature.lower() for x in ["tenure", "charges", "spend", "calls", "delay"]):
        input_data[feature] = st.number_input(feature, value=0.0)
    
    # One-hot encoded features
    else:
        input_data[feature] = st.selectbox(feature, [0, 1])

# Predict button
if st.button("Predict"):
    
    input_df = pd.DataFrame([input_data])

    # Ensure correct order
    input_df = input_df[features]

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("Result")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer Will Stay (Churn Probability: {prob:.2f})")
