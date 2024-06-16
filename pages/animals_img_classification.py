import pickle
from PIL import Image
from io import BytesIO
from img2vec_pytorch import Img2Vec
import streamlit as st

with open('pages/model_animals_npk.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

st.set_page_config(layout="wide", page_title="Animal Image Classification")

st.write("## Animal Image Classification Demo")
st.write(
    ":grin: Upload an image of an animal, and we'll predict which animal it is based on our model :grin:"
)

st.write("""
This application classifies uploaded images of animals into different categories using a pre-trained model. 
You can upload an image and the model will predict which animal is in the image. 
The classification is limited to the following animals: antelope, badger, bat, bear, bee, beetle, bison, boar, butterfly, cat, caterpillar, chimpanzee, cockroach, cow, coyote, crab, crow, deer, dog, dolphin, donkey, dragonfly, duck, eagle, elephant.
""")

st.sidebar.write("## Upload your image :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

@st.cache_data
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="jpg")
    byte_im = buf.getvalue()
    return byte_im

def classify_image(upload):
    image = Image.open(upload)
    col1.write("Uploaded Image :camera:")
    col1.image(image)

    col2.write("Predicted Category :wrench:")
    img = Image.open(upload)
    features = img2vec.get_vec(img)
    pred = model.predict([features])

    col2.header(pred[0])

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        classify_image(upload=my_upload)
else:
    st.write("Upload an image to classify...")