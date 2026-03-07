from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

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

# 3. User Inputs
topic = input("Enter topic for shayri: ")
number_of_lines = input("Enter number of lines: ")
language = input("Enter language: ")
type_of_shayri = input("Enter type of shayri: ")

# 4. Construct the messages for a Chat Model
messages = [
    SystemMessage(content="You are a professional Shayar (Poet)."),
    HumanMessage(content=f"Write a {type_of_shayri} shayri in {language} on the topic of '{topic}' in exactly {number_of_lines} lines.")
]

# 5. Invoke the CHAT model, not the raw LLM
result = chat_model.invoke(messages)

# 6. Print the content
print("\n--- Your Shayri ---\n")
print(result.content)