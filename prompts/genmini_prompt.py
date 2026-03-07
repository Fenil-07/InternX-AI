from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
import streamlit as st

from dotenv import load_dotenv
import os

# This will automatically pick up the GOOGLE_API_KEY from your .env file
load_dotenv()

# Initialize the Gemini chat model directly
# "gemini-2.5-flash" is the recommended default for fast text and multimodal generation
cm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7 
)
st.header("Mushaira.ai")

topic = st.text_input ("Enter topic")
number_of_lines = st.text_input("Enter number of lines")
style = st.text_input ("Enter style")
language = st. text_input("Enter language")

template = load_prompt ("shayri.json")

if st.button("urj kiya hai"):
    button_background_colour = st.color_picker("Pick a background color for your shayari", "#d167f8ff")
    system_prompt = template.invoke({
        "style": style,
        "number_of_lines": number_of_lines,
        "topic": topic,
        "language": language
    })
response_content = "Here is your beautiful generated shayari..."
        
# 4. Display the generated text using the dynamically picked background color!
st.markdown(f'''
            <div style="background-color: {button_background_colour}; padding: 30px; border-radius: 10px; color: blue; text-align: center; font-size: 24px; font-style: italic; font-family: serif;">
            {response_content}</div>''', unsafe_allow_html=True)
chain = template | cm

result = chain. invoke({
"style": style,
"number_of_lines": number_of_lines,
"topic": topic,
"language": language
})
st.write(result.content)