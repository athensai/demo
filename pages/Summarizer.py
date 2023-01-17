import streamlit as st
import openai

st.set_page_config(
    page_title="Summarizer"
)

st.write("# Summarize Text")

text = st.text_area(label="Text", height=300, max_chars=4000)

if st.button('Write'):
    prompt = "Summarize the main points from the article in less than 120 characters: "
    response = openai.complete(prompt = prompt + text)
    st.write(response['choices'][0]['text'])

