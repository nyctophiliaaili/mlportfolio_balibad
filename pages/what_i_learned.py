import streamlit as st

# Title
st.title("🎓 What I Learned")
st.image("back.jpg")
# Learnings from Quantitative Methods: Building Foundations for the Future
st.header("📊 Learnings from Quantitative Methods: Building Foundations for the Future")
st.write("""
Studying Quantitative Methods has been instrumental in building a strong foundation for my future endeavors in data science and machine learning. 
I gained a solid understanding of statistical concepts, data analysis techniques, and mathematical principles that are essential for working with data. 
This knowledge has helped me in various aspects of my projects, from data preprocessing to model evaluation.
""")

# Practical Applications
st.header("Practical Applications")

# Sentiment Analysis
with st.expander("📝 Sentiment Analysis"):
    st.write("""
    Sentiment analysis involves analyzing and classifying text data to determine the sentiment expressed, 
    such as positive, negative, or neutral. In my project on the basic sentiment analyzer, 
    I learned how to use NLTK and a Naive Bayes classifier to perform sentiment analysis on text messages. 
    This taught me the importance of text preprocessing and feature engineering in natural language processing tasks.
    """)

# Prediction
with st.expander("🔮 Prediction"):
    st.write("""
    Prediction involves using machine learning models to make predictions or forecasts based on input data. 
    In my project on the California housing price predictor, I learned how to train a machine learning model 
    to predict the median house value based on various housing features. This taught me how to 
    preprocess data, train a model, and evaluate its performance for prediction tasks.
    """)

# Image Classification
with st.expander("🖼️ Image Classification"):
    st.write("""
    Image classification is the task of categorizing images into predefined classes or labels. 
    In my project on animals image classification, I learned how to use pre-trained models and image embeddings 
    to classify images of animals into different categories. This helped me understand the concept of 
    feature extraction and how it can be applied in real-world scenarios.
    """)
