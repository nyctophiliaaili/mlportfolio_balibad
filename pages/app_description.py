import streamlit as st

# Title
st.title("Streamlit App Descriptions")

# Basic Sentiment Analyzer
st.header("Basic Sentiment Analyzer")
st.image("sentiment_analyzer.png", caption="Basic Sentiment Analyzer")
st.write("""
This application analyzes the sentiment of a text message and classifies it as positive or negative. 
It uses a trained Naive Bayes classifier and NLTK for text processing. 
You can input a message and click the 'Say it' button to see the sentiment analysis result.
""")

# California Housing Price Predictor
st.header("California Housing Price Predictor")
st.image("housing_price_predictor.png", caption="California Housing Price Predictor")
st.write("""
This application predicts the median house value in California based on various housing features. 
You can input the longitude, latitude, housing median age, total rooms, total bedrooms, population, households, and median income 
to get the predicted median house value.
""")

# Animals Image Classification
st.header("Animals Image Classification")
st.image("animal_classification.png", caption="Animals Image Classification")
st.write("""
This application classifies uploaded images of animals into different categories using a pre-trained model. 
You can upload an image and the model will predict which animal is in the image.
""")