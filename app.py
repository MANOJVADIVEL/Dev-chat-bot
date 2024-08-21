import streamlit as st
import google.generativeai as genai


st.title("welcome to my AIchat")
genai.configure(api_key="AIzaSyAudpo8Onruje6JAUBCgHcRoOXUi-9ySP8")
    
text = st.text_input("enter your prompt")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
    