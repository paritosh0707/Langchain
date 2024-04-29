from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("user","Question:{question}")
    ]
)


## Inference Llama2 LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

## Streamlit app
st.title('Langchain demo using Llama2 via Ollama')
input_text = st.text_input("Ask the query...")
if input_text:
    response = chain.invoke({'question':input_text})
    st.write(response)