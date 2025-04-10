# Text Similarity in NLP

This module demonstrates two main approaches to measure how similar two pieces of text are: **Lexical (surface-level)** and **Semantic (meaning-based)**.

---

## 1. Cosine Similarity with TF-IDF

### Description:
Measures similarity based on word overlap using TF-IDF vectors and cosine similarity.

### Technique:
- Convert sentences to vectors using `TfidfVectorizer`
- Compare them using `cosine_similarity` from `sklearn`

### Example Output:

Text 1: I love natural language processing.
Text 2: I enjoy working on natural language processing projects.
Cosine Similarity: 0.4074


### Limitation:
Does not understand synonyms or meaning. Only checks surface word matches.


## 2. Semantic Similarity with BERT

### Description:
Uses a pre-trained transformer model to generate embeddings that capture the **meaning** of each sentence.

### Technique:
- Uses `sentence-transformers` and `all-MiniLM-L6-v2`
- Computes cosine similarity on embeddings

### Example Output:

Text 1: I love Natural Language Processing.
Text 2: NLP is something I'm really passionate about.
Semantic Similarity Score: 0.6123