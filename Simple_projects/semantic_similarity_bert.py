from sentence_transformers import SentenceTransformer, util

# Load pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample texts
text1 = "I love Natural Language Processing."
text2 = "NLP is something I'm really passionate about."

# Encode sentences
emb1 = model.encode(text1, convert_to_tensor=True)
emb2 = model.encode(text2, convert_to_tensor=True)

# Compute cosine similarity
cos_sim = util.pytorch_cos_sim(emb1, emb2)

print(f"Text 1: {text1}")
print(f"Text 2: {text2}")
print(f"Semantic Similarity Score: {cos_sim.item():.4f}")
