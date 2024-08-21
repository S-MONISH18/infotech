import streamlit as st
import google.generativeai as genai

st.title("welcome to INFOTECH AI")

# Configure the API key
genai.configure(api_key="AIzaSyD0AJ42-kPJkv_dueFv8wS2xoXpOvnOtmU")

# Get user input
text = st.text_input("Enter your message:")

   
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

 
if st.button("click me"):  
    response = chat.send_message(text)

    st.write(response.text)
