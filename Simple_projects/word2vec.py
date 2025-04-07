from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# Sample text corpus (You can use a larger dataset)
corpus = [
    "Natural Language Processing is exciting.",
    "Machine Learning and NLP are related fields.",
    "Word2Vec helps in understanding word relationships.",
]

# Tokenizing sentences into words
tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]

# Train Word2Vec model
model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)

# Get the vector for a word
word = "nlp"
if word in model.wv:
    print(f"Vector for '{word}':\n", model.wv[word])

# Find similar words
print("\nWords similar to 'nlp':", model.wv.most_similar("nlp"))
