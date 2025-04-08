from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Machine learning is amazing.",
    "Artificial intelligence is the future.",
    "I love watching movies.",
    "Learning algorithms is fun."
]

embeddings = model.encode(sentences, convert_to_tensor=True)

for i in range(1, len(sentences)):
    score = util.pytorch_cos_sim(embeddings[0], embeddings[i])
    print(f"Similarity between:\n '{sentences[0]}'\n '{sentences[i]}'\n => {score.item():.4f}\n")