from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
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

st.header("Mushaira.ai")

# 3. User Inputs
topic = st.text_input("Enter topic for shayri: ")
number_of_lines = st.text_input("Enter number of lines: ")
language = st.text_input("Enter language: ")
style = st.text_input("Enter type of shayri: ")

template = ChatPromptTemplate(
    template =
    """
  you are a poet, write a shayari on the following topic.

  TASK:
  - write a shayari on the topic given below: {topic}
  - the responce must be {number_of_lines} lines long.
  - the responce must be in {style} style as per input.
  - Every line must be rhyming with each other meaningful and related to the topic.
  - do not write any explanation or anything else, just write the shayari.

  STYLE RULES:(follow the rules for the style of shayri given in input)
    - write the shayari in {style} style as per input.
    1. Sher (Couplet)
    Definition: The fundamental building block of Shayari. A Sher consists of exactly two lines (called Misras).
    The Rule: Those two lines must contain a completely independent, profound, and finished thought. You don't need to read anything before or after it to understand its meaning.
    Length: 2-4 Lines.
    2. Rubai (Quatrain)
    Definition: A standalone, four-line poem. The word originates from the Arabic word for "four."
    The Rule: It follows a strict rhyming scheme of AABA. The first, second, and fourth lines rhyme, while the third line is a "wildcard" that sets up the punchline delivered in the fourth. It is typically used for philosophical, spiritual, or romantic themes.
    Length: 4 Lines.
    3. Ghazal (Ode)
    Definition: A collection of several independent Shers (couplets) strung together by a strict set of structural rules.
    The Rule: A Ghazal typically has between 5 and 15 couplets. The fascinating thing about a Ghazal is that every couplet can be about a completely different topic (one about love, the next about politics). They are bound together only by a strict meter (Behr) and a recurring rhyming pattern at the end of the second line of every couplet (Kaafiya and Radif).
    Length: Usually 10+ Lines (5+ couplets).
    4. Nazm (Poem)
    Definition: A structured poem dedicated to a single, continuous theme or narrative from the first line to the last.
    The Rule: Unlike a Ghazal where every couplet is independent, a Nazm tells a cohesive story or explores one specific idea (like a poem about a rainy evening, or a specific political event). It has a title, and while it often uses rhyme and meter, it is far more flexible than a Ghazal.
    Length: Variable (can be short or very long).
    5. Azad Nazm (Free Verse)
    Definition: The modern rebel of the Shayari world. It is poetry free from the rigid, classical rules of rhyming patterns and strict meter.
    The Rule: There are no strict rules. It relies on the natural rhythm of the words, the line breaks, and the power of the imagery to convey emotion, rather than a mathematical rhyming structure.
    Length: Variable.

 LANGUAGE RULES:
  - write the shayari in {language} language as per input.
  - do not write the shayari in any other language, only write in the language given in input.

 FORMAT:
  -do not write in continuous paragraph, write the shayari in separate lines as per the number of lines given in input.
  - do not write the shayari in any other format, only write in the format given in input.

  QUALITY RULES:
  - ensure the shayari is of high quality, creative, and engaging.
  - avoid clichés and overused phrases, strive for originality and depth in your shayari.
  - ensure the shayari evokes emotions and resonates with the reader, making it memorable and impactful.
  - ensure the shayari is well-structured, with a clear beginning, middle, and end, and that it flows smoothly from one line to the next.
  - ensure the shayari is grammatically correct and free of spelling errors, maintaining a high standard of language and expression.

  Before you start writing the shayari, reensure 
  1. you understand the topic, style, language.
  2. you understand the number of lines required.
  3. Take a moment to gather your thoughts.

  now generate the shayari based on the above instructions and rules.

  """,
input_variables=["topic", "number_of_lines", "language", "style"])

system_prompt = template.invoke({
    "topic": topic,
    "number_of_lines": number_of_lines,
    "language": language,
    "style": type_of_shayri
})


# 4. Construct the messages for a Chat Model
#messages = [
    #SystemMessage(content="You are a professional Shayar (Poet)."),
    #HumanMessage(content=f"Write a {type_of_shayri} shayri in {language} on the topic of '{topic}' in exactly {number_of_lines} lines.")
#]
if st.button ("urj kiya hai"):
    background_colour = st.color_picker("Pick a background color for your shayari", "#d167f8ff")
    result = chat_model.invoke(system_prompt)
    st.markdown(f"<div style='background-color: {background_colour}; padding: 10px; border-radius: 5px;'>{result.content}</div>", unsafe_allow_html=True)