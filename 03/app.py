from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Backend Server",
    version="1.0",
    description="API server using Langserve"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()

llama_model = Ollama(model="llama2")

prompt_openai = ChatPromptTemplate.from_template("Write essay about {topic} with 20 words")

prompt_llama2 = ChatPromptTemplate.from_template("Write poem about {topic} with 20 words")

add_routes(
    app,
    prompt_openai|model,
    path="/essay"
)

add_routes(
    app,
    prompt_llama2|llama_model,
    path="/poem"
)

if __name__ =="__main__":
    uvicorn.run(app, host="localhost",port=8000)