from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

# 1. Setup the Endpoint with the correct task
# Featherless/HuggingFace prefer 'conversational' for Instruct models
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="conversational", 
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# 2. Wrap it in ChatHuggingFace to handle the ChatML template
chat_model = ChatHuggingFace(llm=llm)

st.header("AI instant shayri maker")

# 3. User Inputs
topic = st.text_input("Enter topic for shayri: ")
number_of_lines = st.text_input("Enter number of lines: ")
language = st.text_input("Enter language: ")
type_of_shayri = st.text_input("Enter type of shayri: ")


# 4. Construct the messages for a Chat Model
messages = [
    SystemMessage(content="You are a professional Shayar (Poet)."),
    HumanMessage(content=f"Write a {type_of_shayri} shayri in {language} on the topic of '{topic}' in exactly {number_of_lines} lines.")
]
if st.button ("urj"):
    result = chat_model.invoke(messages)
    st.write (result.content)