import requests
import streamlit as st 
import base64
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/sdxl-turbo"
headers = {"Authorization": "Bearer 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"}

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("pen_tool.jpg")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input("enter a prompt"),
})
# You can access the image with PIL.Image for example

image = Image.open(io.BytesIO(image_bytes))

if st.button('generate'):
    st.image(image)

