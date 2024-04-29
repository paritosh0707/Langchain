import requests
import streamlit as st
import json

def get_essay(topic):
    response = requests.post("http://localhost:8000/essay/invoke",
                            json={"input":{"topic": topic}})
    return response.json()['output']['content']

def get_poem(topic):
    response = requests.post("http://localhost:8000/poem/invoke",
                            json={"input":{"topic": topic}})
    return response.json()['output']['content']

## streamlit app
st.title("Langserve Demo")

essay_topic = st.text_input("Write essay topic...")
poem_topic = st.text_input("Write poem topic...")

if essay_topic:
    st.write(get_essay(essay_topic))
if poem_topic:
    st.write(get_poem(poem_topic))