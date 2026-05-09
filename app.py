import streamlit as st
import pandas as pd
import pickle

# Load model and files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Page title
st.set_page_config(page_title="Customer Churn Prediction")

st.title(" Customer Churn Prediction System")

st.write("Fill customer details below:")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

MonthlyCharges = st.number_input("Monthly Charges", value=50.0)
TotalCharges = st.number_input("Total Charges", value=500.0)

# Create input dataframe
input_data = pd.DataFrame({
    'gender':[gender],
    'SeniorCitizen':[SeniorCitizen],
    'Partner':[Partner],
    'Dependents':[Dependents],
    'tenure':[tenure],
    'PhoneService':[PhoneService],
    'MultipleLines':[MultipleLines],
    'InternetService':[InternetService],
    'OnlineSecurity':[OnlineSecurity],
    'OnlineBackup':[OnlineBackup],
    'DeviceProtection':[DeviceProtection],
    'TechSupport':[TechSupport],
    'StreamingTV':[StreamingTV],
    'StreamingMovies':[StreamingMovies],
    'Contract':[Contract],
    'PaperlessBilling':[PaperlessBilling],
    'PaymentMethod':[PaymentMethod],
    'MonthlyCharges':[MonthlyCharges],
    'TotalCharges':[TotalCharges]
})

# Convert categorical data
input_data = pd.get_dummies(input_data)

# Match training columns
input_data = input_data.reindex(columns=columns, fill_value=0)

# Scaling
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error(" Customer is likely to CHURN")
    else:
        st.success(" Customer is likely to STAY")