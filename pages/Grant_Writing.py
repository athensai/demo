import streamlit as st
import openai

st.set_page_config(
    page_title="Grant Writing",
)

openai.api_key = st.secrets["openaiKey"]
st.write("# Welcome to Grant Writer!")

org = st.text_input("Organization name: ", disabled=False)
amount = st.text_input("Amount requested: ", disabled=False)
project = st.text_input("Project description: ", disabled=False)

prompt = "Write a grant proposal for " + org + ". They are requesting " + amount + "for " + project

if st.button('Write'):
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
    st.write(response['choices'][0]['text'])
