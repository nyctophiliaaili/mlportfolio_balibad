import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        
        Section("Main Page", "🏠"),
        Page("pages/about_me.py", "About Me", "👨‍💻", in_section=True),
        Page("pages/app_description.py", "Streamlit App Description", "📜", in_section=True),
        Page("pages/what_i_learned.py", "What I Have Learned", "📚", in_section=True),
        
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/sentiment_analysis_app.py", "Basic Sentiment Analyzer", "👍", in_section=True),
        Page("pages/california_housing.py", "California Housing Price Predictor", "💰", in_section=True),
        Page("pages/animals_img_classification.py", "Animals Image Classification", "🐾", in_section=True),

        Section("Sample Source Code", "💾"),
        Page("pages/sentiment_src.py", "Basic Sentiment Analyzer SRC", "👍", in_section=True),
        Page("pages/housing_src.py", "California Housing Price Predictor SRC", "💰", in_section=True),
        Page("pages/animals_img_classification_src.py", "Animals Image Classification SRC", "🐾", in_section=True),

    ]
)


hide_pages(["Thank you"])

st.markdown("### FINAL REQUIREMENTS PRESENTED BY:")
st.markdown("### BALIBAD, DANIELLE of BSIS 3-B")

st.image("./balibad.jpg")
st.markdown("""For more info, contact <a href="https://www.facebook.com/profile.php?id=100010493740908">Danielle Marie Balibad</a> on Facebook""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/nyctophiliaaili/mlportfolio_balibad)")
st.markdown("---")

st.markdown("### HISTORY, PURPOSE AND USAGE of MACHINE LEARNING")

with st.expander("History of Machine Learning"):
    st.markdown("""
    # History
    Machine learning has a rich history that dates back to the 1950s. The field evolved from early theories of artificial intelligence and the development of neural networks. Notable milestones include:
    - 1950: Alan Turing proposes the Turing Test to assess a machine's ability to exhibit intelligent behavior.
    - 1952: Arthur Samuel develops the first computer program that can learn and improve its performance at playing checkers.
    - 1980s: The rise of machine learning research and the development of backpropagation for training neural networks.
    - 2000s: The advent of big data and powerful GPUs fuels the growth of deep learning, leading to significant breakthroughs in image and speech recognition.
    """)

with st.expander("Purpose of Machine Learning"):
    st.markdown("""
    # Purpose
    The purpose of machine learning is to enable computers to learn from data and make decisions or predictions without being explicitly programmed. This can be broken down into several key objectives:
    - **Automation**: Automating repetitive and time-consuming tasks.
    - **Prediction**: Making predictions based on historical data, such as stock prices or weather forecasts.
    - **Pattern Recognition**: Identifying patterns and anomalies in large datasets, such as detecting fraudulent transactions or diagnosing medical conditions.
    - **Personalization**: Providing personalized recommendations and experiences, such as in e-commerce or content streaming services.
    """)

with st.expander("Usage of Machine Learning"):
    st.markdown("""
    # Usage
    Machine learning is widely used across various industries and applications:
    - **Healthcare**: For diagnosing diseases, predicting patient outcomes, and personalizing treatment plans.
    - **Finance**: For fraud detection, algorithmic trading, and credit scoring.
    - **Retail**: For customer segmentation, inventory management, and personalized marketing.
    - **Transportation**: For optimizing routes, predicting maintenance needs, and enabling autonomous driving.
    - **Entertainment**: For content recommendation, sentiment analysis, and creating realistic computer-generated imagery (CGI).
    - **Agriculture**: For crop prediction, soil analysis, and precision farming.
    """)

st.markdown("""
### 👨‍🎓 Introduction to Streamlit Application

##### 👨‍👦‍👦 Overview

* Easy to use
* Interactive web apps
* Python-based framework

##### 👨‍🔧 More Content

   Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

   The purpose of Streamlit is to simplify the process of creating web applications for data science and machine learning projects. It allows data scientists and machine learning engineers to turn their models and analyses into interactive web applications without needing extensive web development skills.

   Streamlit applications are simple to write and deploy. You can create a working app with just a few lines of Python code. The library provides a wide range of widgets, such as sliders, buttons, and graphs, to create interactive applications. The framework also supports real-time updates and is highly customizable.

   Since its release, Streamlit has gained a lot of popularity due to its simplicity and ease of use. It is widely used in the data science community and has a growing ecosystem of plugins and extensions.

   Whether you are building a quick prototype or a complex data visualization, Streamlit provides the tools you need to get your application up and running quickly and efficiently.


### 🔎 Overview""", unsafe_allow_html=True)


st.image("./streamlit.png")

st.markdown("""
Streamlit is an open-source Python library that enables the creation of interactive, web-based applications for data science and machine learning projects. It is designed to simplify the process of building and sharing web apps without requiring extensive web development experience.

Key features of Streamlit include:

- **Ease of Use**: Streamlit allows you to create web apps with just a few lines of Python code. The intuitive API makes it easy to add interactive widgets such as sliders, buttons, and input fields.
- **Real-Time Updates**: Streamlit apps automatically update in real-time as you make changes to your code. This makes it easy to iterate and improve your app quickly.
- **Wide Range of Widgets**: Streamlit provides a variety of built-in widgets for common tasks such as displaying tables, plotting graphs, and handling user input. You can also create custom widgets as needed.
- **Integration with Python Libraries**: Streamlit seamlessly integrates with popular Python libraries such as NumPy, pandas, Matplotlib, and Plotly, making it easy to incorporate data processing and visualization into your app.
- **Deployment Options**: Streamlit apps can be deployed on various platforms, including Streamlit Cloud, Heroku, and AWS. This makes it easy to share your apps with others.

The goal of Streamlit is to empower data scientists and machine learning engineers to create interactive applications quickly and easily, without having to worry about the complexities of web development. Whether you need to build a quick prototype or a fully-featured application, Streamlit provides the tools you need to bring your ideas to life.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=nyctophiliaaili&repo=mlportfolio_balibad&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
