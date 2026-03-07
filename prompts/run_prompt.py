import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from st_copy_to_clipboard import st_copy_to_clipboard
from langchain_core.prompts import load_prompt

# --- 1. Custom Styling (Sea Green Theme) ---
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #A3E4D7;
        color: #311432;
        border: black solid 1px;
        border-radius: 8px;
        padding: 8px 12px;
        button-alignment: center;
    }
    div.stButton > button:first-child:hover {
        background-color: #skyblue; 
    }
    .poetry-output {
        font-family: 'Italic', serif;
        font-size: 24px;
        line-height: 1.8;
        color: #311432;
        text-align: center;
        background-color: #FFE4E1; 
        padding: 30px;
        border-radius: 10px;
        border-left: 5px solid #FFB7C5;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. API Key Setup via Sidebar ---
st.sidebar.title("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter your Google API Key:", type="password")

# --- 3. Configuration & State ---
style_rules = {
    "Sher (Couplet)": 2,
    "Rubai (Quatrain)": 4,
    "Ghazal (Ode)": 10,
    "Nazm (Poem)": 8,
    "Azad Nazm (Free Verse)": 12,
}

# --- 4. Streamlit UI Elements ---
st.title("🪶 Mushaira.ai")
st.subheader("Your AI-Powered Shayari Companion")

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox("Language", ["Gujarati", "Marathi", "Hindi", "English", "Urdu"], index=0)
    selected_style = st.selectbox("Poetry Style", list(style_rules.keys()))

with col2:
    topic = st.text_input("Topic for Shayari")
    number_of_lines = st.number_input(
        "Number of Lines", 
        min_value=1, 
        max_value=100, 
        value=style_rules[selected_style], 
        step=1
    )

# --- 5. LangChain Execution ---
if st.button("Generate Shayari"):
    # Guardrail: Check if the API key is provided before running
    if not api_key:
        st.error("🚨 Please enter your Google API Key in the sidebar first!")
    else:
        # THE FIX: Pass the API key DIRECTLY to the model
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.8,
            api_key=api_key  # <--- This stops it from looking for st.secrets
        )
        
        with st.spinner("Writing verses..."):
            try:
                # Ensure shayri.json is in the same directory as this script
                prompt = load_prompt("shayri.json")
                
                chain = prompt | llm
                
                response = chain.invoke({
                    "style": selected_style.split(" ")[0], 
                    "language": language,
                    "topic": topic,
                    "number_of_lines": number_of_lines
                })
                
                st.markdown(f'<div class="poetry-output">{response.content.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

                # --- THE NEW COPY BUTTON ---
                st.write("") # Adds a tiny bit of breathing room below the text
                
                # Creates a button that silently copies the raw text to the user's clipboard
                st_copy_to_clipboard(
                    response.content, 
                    before_copy_label="📋 Copy ", 
                    after_copy_label="✅ Copied!"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {e}")