import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/crop_recom_streamlitapp.py", "Crop Recommendation ML Model", "1️⃣", in_section=True),
        Page("pages/basic_sentiment_analyzer.py", "Basic Sentiment Analyzer", "2️⃣", in_section=True),
        Page("pages/img_classification.py", "Image Classification 1 (Sky Condition)", "3️⃣", in_section=True),
        Page("pages/img_classification_lettuce_diseases.py", "Image Classification 2 (Lettuce Diseaes)", "4️⃣", in_section=True),
  
        Section("Sample Source Code", "💾"),
        Page("pages/crop_src.py", "Crop Recommendation SRC", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "Basic Sentiment Analyzer SRC", "2️⃣", in_section=True),
        Page("pages/image_classification_src.py", "Image Classification SRC", "3️⃣", in_section=True),
        Page("pages/full_src_recom.py", "Full Crop Recommendation SRC", "4️⃣", in_section=True),
        Page("pages/crop_src_full.py", "Crop Recommendation Training Full SRC", "5️⃣", in_section=True),

    ]
)


hide_pages(["Thank you"])

st.markdown("### FINAL REQUIREMENTS PRESENTED BY:")
st.markdown("### BALIBAD, DANIELLE of BSIS 3-B")

st.image("./balibad.jpg")
st.markdown("""For more info, contact <a href="https://www.facebook.com/profile.php?id=100010493740908">Danielle Marie Balibad</a> on Facebook""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/nyctophiliaaili/mlportfolio_balibad)")
st.info("Issues are now fixed with Streamlit 1.35.0")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

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
### 👨‍🎓 Sample Header Title

##### 👨‍👦‍👦 Subheader Title

* Bullet 1
* Bullet 2
* Bullet 3


##### 👨‍🔧 More Content

   HISTORY, PURPOSE AND USAGE
        Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. 
        The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:
        “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
        The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. 
        A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.
        The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. 
        Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.

### 🔎 Overview""", unsafe_allow_html=True)


st.image("./back.jpg")


st.markdown("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Id neque aliquam vestibulum morbi blandit cursus risus. Sagittis nisl rhoncus mattis rhoncus. 
Purus viverra accumsan in nisl nisi scelerisque eu. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet. 
Eleifend quam adipiscing vitae proin. Neque convallis a cras semper auctor neque. Et tortor consequat id porta nibh. 
Vitae nunc sed velit dignissim sodales ut eu. Bibendum ut tristique et egestas quis ipsum suspendisse. 
Pharetra massa massa ultricies mi. In nulla posuere sollicitudin aliquam ultrices sagittis. Et pharetra pharetra massa massa. 
Pretium viverra suspendisse potenti nullam ac. Viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor. 
Nibh mauris cursus mattis molestie a iaculis at erat. Diam sit amet nisl suscipit. 
Urna molestie at elementum eu facilisis sed odio morbi quis. Arcu non sodales neque sodales.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
