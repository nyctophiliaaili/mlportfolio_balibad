
import streamlit as st
import pandas as pd
import pickle

# Load the trained model from the saved file
filename = 'pages/housing_model.sav'
model = pickle.load(open(filename, 'rb'))

st.title("California Housing Price Predictor")
st.subheader("Enter the housing features to predict the median house value:")

longitude = st.number_input("Longitude:", value=-120.0, format="%.6f")
latitude = st.number_input("Latitude:", value=35.0, format="%.6f")
housing_median_age = st.number_input("Housing Median Age:", value=20)
total_rooms = st.number_input("Total Rooms:", value=1000)
total_bedrooms = st.number_input("Total Bedrooms:", value=200)
population = st.number_input("Population:", value=500)
households = st.number_input("Households:", value=200)
median_income = st.number_input("Median Income:", value=3.0, format="%.4f")

# Create a DataFrame for the input features
input_data = pd.DataFrame({
    'longitude': [longitude],
    'latitude': [latitude],
    'housing_median_age': [housing_median_age],
    'total_rooms': [total_rooms],
    'total_bedrooms': [total_bedrooms],
    'population': [population],
    'households': [households],
    'median_income': [median_income]
})

# Make prediction
predicted_value = model.predict(input_data)

st.text("The predicted median house value is:")
st.text_area(label="", value=f"${predicted_value[0]:.2f}", height=100)