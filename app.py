import streamlit as st
import pickle
import numpy as np

# Load model

with open("salary_model_gd.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Salary Prediction App")

st.write("Enter Employee Experiance")

experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0
)

if st.button("Predict Salary"):

    prediction = model.predict([[experience]])

    st.success(f"Predicted Salary = ${prediction[0]:,.2f}")
