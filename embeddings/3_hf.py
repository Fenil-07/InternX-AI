from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
result = em.embed_documents("where is the eiffel tower?")
print(result)
