# Customer Churn Prediction App 🚀

This project is an end-to-end Machine Learning application that predicts whether a customer is likely to churn based on telecom data.

---

## 📌 Overview
The goal of this project is to identify customers who are likely to leave a service using historical data.  
The trained model is deployed as a web app to allow real-time predictions.

---

## ⚙️ Features
- Data preprocessing and feature handling  
- Handling class imbalance using SMOTE  
- Model training using Random Forest  
- Evaluation using accuracy, confusion matrix, and F1-score  
- Deployment using Streamlit  

---

## 🧠 Model Details
- Model Used: Random Forest Classifier  
- Accuracy: ~93%  
- Evaluation Metrics:
  - Accuracy  
  - Confusion Matrix  
  - F1-score  

Note: Since churn datasets are often imbalanced, F1-score and class balance were also considered instead of relying only on accuracy.

---

## 🚀 Deployment
The model is deployed using Streamlit and can take user input to predict churn in real time.

Live App:  [
https://churn-prediction-app-otcwmxnfsee2jedjempsef.streamlit.app/](https://churn-prediction-app-otcwmxnfsee2jedjempsef.streamlit.app/)

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- Streamlit  

---

## 📂 Project Structure
app.py                # Streamlit app  
model.pkl            # Trained model  
churn.ipynb          # Training notebook  
requirements.txt     # Dependencies  
README.md  

---

## 📈 Learning Outcome
This project helped me understand:
- The complete ML pipeline (data → model → deployment)  
- Importance of consistent preprocessing  
- Handling imbalanced datasets  
- Converting models into usable applications  

---

## 🔮 Future Improvements
- Add feature importance / model interpretability  
- Improve model performance with tuning  
- Enhance UI of the app  

---

## 🤝 Feedback
Feel free to explore the project and share feedback!
