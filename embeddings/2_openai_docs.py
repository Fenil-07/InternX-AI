from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

em = OpenAIEmbeddings(model="text_embedding_small", dimensions=32)
docs = ["Hello world", "Bonjour le monde", "Hola mundo"]

result = em.embed_documents(docs)

print(result)
print(len(result))  # Should print 32