from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import load_prompt
import streamlit as st

from dotenv import load_dotenv
import os
load_dotenv()

endpoint = HuggingFaceEndpoint( repo_id="Qwen/Qwen2.5-1.5B-Instruct", task="text-generation", ) 

cm = ChatHuggingFace(llm=endpoint)
st.header("AI instant shayri maker")

topic = st.text_input("Enter topic for shayri: ")
number_of_lines = st.text_input("Enter number of lines: ")
language = st.text_input("Enter language: ")
style = st.text_input("Enter style: ")

template = load_prompt("shayri.json")

system_prompt = template.invoke({
    "topic": topic,
    "number_of_lines": number_of_lines,
    "language": language,
    "style": style
})

if st.button ("urj kiya hai"):
    result = ("------pesh hai aapki shayri------")
    result = cm.invoke(system_prompt)
    st.write (result.content)