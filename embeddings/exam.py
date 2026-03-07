from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")




user_docs = [ "Climate change is mainly caused by greenhouse gases released from burning fossil fuels and industrial activities.", 
             "The effects of climate change include rising global temperatures, melting glaciers, and increasing sea levels.", 
             "Climate change leads to extreme weather events such as heatwaves, floods, droughts, and stronger storms.",
               "Climate change disrupts ecosystems, damages agriculture, and increases risks to human health worldwide.", 
               "Using renewable energy, planting trees, and reducing emissions are key solutions to slow climate change.", 
               "Climate change causes rising temperatures, melting ice caps, and sea level rise, impacting life globally.", 
               "Global warming results in extreme weather like droughts, floods, and heatwaves, which are major climate impacts.", 
             "Reducing carbon emissions through clean energy and sustainability can help control climate change effects." ]

user_query = "what is climate change ?"
user_doc_embeddings = em.embed_documents(user_docs)
user_query_embedding = em.embed_query(user_query)

#compute cosine similarities
from sklearn.metrics.pairwise import cosine_similarity

score = cosine_similarity([user_query_embedding], user_doc_embeddings)
top_results = sorted([(i, s) for i, s in enumerate(score[0]) if s > 0.9],key=lambda x: x[1],reverse=True)[:3]
print(f"\nTop {len(top_results)} Results (Score > 0.55):")
if not top_results:
    print("No relevant data found.")
else:
    print(f"\nTop {len(top_results)} Results (Score > 0.55):")
    for i, (index, score) in enumerate(top_results, 1):
        print(f"{i}. Score: {score:.4f}")
        print(f"   Document: \"{user_docs[index]}\"")
        print("-" * 60)
