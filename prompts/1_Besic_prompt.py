from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load .env file (Ensure it contains GOOGLE_API_KEY=your_api_key)
load_dotenv()

# 1. Setup the Gemini Chat Model
# 'gemini-1.5-flash' is fast and free/cheap. Use 'gemini-1.5-pro' for complex logic.
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 2. Wrap it in ChatHuggingFace to handle the ChatML template
llm = ChatGoogleGenerativeAI(llm=llm)

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
print("----irshard----irshard----irshard")
print(result.content)