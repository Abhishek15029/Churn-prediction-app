if st.button("Predict"):

    input_dict = {
        "Age": age,
        "Tenure": tenure,
        "Usage Frequency": usage,
        "Support Calls": support_calls,
        "Payment Delay": payment_delay,
        "Total Spend": total_spend,
        "Last Interaction": last_interaction,

        "Gender_Male": 1 if gender == "Male" else 0,
        "Gender_Female": 1 if gender == "Female" else 0,

        "Subscription Type_Basic": 1 if subscription == "Basic" else 0,
        "Subscription Type_Standard": 1 if subscription == "Standard" else 0,
        "Subscription Type_Premium": 1 if subscription == "Premium" else 0,

        "Contract Length_Monthly": 1 if contract == "Monthly" else 0,
        "Contract Length_Quarterly": 1 if contract == "Quarterly" else 0,
        "Contract Length_Annual": 1 if contract == "Annual" else 0,
    }

    input_df = pd.DataFrame([input_dict])

    # SAFE FIX
    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer Will Stay (Churn Probability: {prob:.2f})")
