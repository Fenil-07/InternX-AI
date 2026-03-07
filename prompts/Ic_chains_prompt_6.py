from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import load_prompt
import streamlit as st

from dotenv import load_dotenv
import os
load_dotenv()

endpoint = HuggingFaceEndpoint( repo_id="Qwen/Qwen3.5-397B-A17B", task="text-generation", ) 

cm = ChatHuggingFace(llm=endpoint)
st.header("AI instant shayri maker")

topic = st.text_input ("Enter topic")
number_of_lines = st.text_input("Enter number of lines")
style = st.text_input ("Enter style")
language = st. text_input("Enter language")

template = load_prompt ("shayri.json")

if st.button("urj kiya hai"):
    system_prompt = template.invoke({
        "style": style,
        "number_of_lines": number_of_lines,
        "topic": topic,
        "language": language
    })
chain = template | cm

result = chain. invoke({
"style": style,
"number_of_lines": number_of_lines,
"topic": topic,
"language": language
})
st.write(result.content)