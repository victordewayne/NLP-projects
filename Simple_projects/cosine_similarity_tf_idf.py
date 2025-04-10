from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text1 = "I love natural language processing."
text2 = "I enjoy working on natural language processing projects."

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])

cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print(f"Text 1: {text1}")
print(f"Text 2: {text2}")
print(f"Cosine Similarity: {cos_sim[0][0]:.4f}")
