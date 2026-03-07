from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv 
load_dotenv()

cm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)
result = cm.invoke("Where is the Eiffel Tower?") 
print(result)
print (result.content)


#import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Ensure your Google API key is set in your environment variables
# os.environ["GOOGLE_API_KEY"] = "your_api_key_here"

# Initialize the model (e.g., using gemini-2.5-pro or gemini-2.5-flash)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0.7
)

# Example invocation
response = llm.invoke("Hello, how are you today?")
print(response.content)