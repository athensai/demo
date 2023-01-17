import streamlit as st
import openai

st.set_page_config(
    page_title="Summarizer"
)

st.write("# Summarize Text")

text = st.text_area(label="Text", height=300, max_chars=4000)

if st.button('Summarize'):
    prompt = "Summarize the main points from the article in less than 120 characters: "
    response = openai.Completion.create(engine="text-davinci-002", prompt= prompt + text, max_tokens=150)
    st.write(response['choices'][0]['text'])

