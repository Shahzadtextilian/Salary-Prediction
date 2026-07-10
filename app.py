import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("salary_model_sklearn.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Salary Prediction", page_icon="💰")

st.title("💰 Salary Prediction App")

experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)

if st.button("Predict Salary"):

    input_data = np.array([[experience]])

    prediction = model.predict(input_data)

    # Convert NumPy array to a Python float
    salary = prediction.item()

    st.success(f"Predicted Salary = ${salary:,.2f}K")
