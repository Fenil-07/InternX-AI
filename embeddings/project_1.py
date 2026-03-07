from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

user_docs = ["Neymar da Silva Santos Júnior's ascent from the dusty streets of Mogi das Cruzes to the pinnacle of world football is a testament to raw talent honed by unwavering dedication.", 
             "Born into a modest family where his father, a former footballer, became his first mentor, Neymar’s relationship with the ball began almost as soon as he could walk. ",
             "He honed his skills on the futsal courts of São Vicente, where the heavier ball and tighter spaces forced him to develop the lightning-quick reflexes and close control that would later become his trademark.",
             "His prodigious talent was undeniable, drawing the attention of scouts from Santos FC when he was just a child, leading to a contract that would change his family's life forever.",
             "At Santos, he wasn't just another prospect; he was a phenomenon in the waiting, dazzling youth coaches with an improvisational style that echoed the 'Ginga' spirit of Brazilian legends like Pelé and Robinho.",
             "His professional debut at 17 was not a tentative step but an explosion onto the scene, as he humiliated defenders with audacious dribbles and scored goals that defied physics. The 'Meninos da Vila' generation, led by a mohawked Neymar, brought a swagger back to Brazilian domestic football that had been missing for years, culminating in a Copa Libertadores triumph that cemented his status as a national icon before he even left for Europe.", 
             "The pressure on his young shoulders was immense, dubbed 'The Next Pelé' by a media frenzy that followed his every move, yet he played with a joy that made the game look like a dance. His journey wasn't just about skill; it was about survival in a ruthless industry, navigating the physical brutality of defenders who sought to break him and the weight of expectation from a nation of 200 million.",
             "By the time he signed for Barcelona to play alongside Messi, he was no longer just a promising talent but a global superstar, having transformed the art of the winger with his unique blend of street-smart trickery and elite athleticism. ",
             "His path was paved with sacrifices, from leaving friends behind to enduring grueling training regimes, but his belief in his 'Ousadia e Alegria' (Audacity and Joy) philosophy never wavered.",
             " Every stepover, every nutmeg, and every goal was a tribute to the boy who just wanted to play, proving that magic still had a place in the modern, mechanized game of football."]

user_query = "who is messi  ?"

user_doc_embeddings = em.embed_documents(user_docs)

user_query_embedding = em.embed_query(user_query)
#compute cosine similarities
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity([user_query_embedding], user_doc_embeddings)
print(similarities) 
print("Most similar document:", user_docs[similarities.argmax()])
if similarities.max() < 0.5:
 print("No relevant documents found.")