from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

em = OpenAIEmbeddings(model="text-embedding-3-large-002", dimensions=32)

vector_result = em.embed_query("where is eiffel tower?")

print(vector_result)
print(len(vector_result))  # Should print 32