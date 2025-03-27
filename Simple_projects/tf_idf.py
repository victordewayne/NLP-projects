from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Natural Language Processing is an exciting field of Artficial Inelligence.",
    "Machine Learning and NLP are revolutionizing text processing.",
    "TF-IDF helps identify important words in a document.",
]


#TF - IDF Vectorizer
vectorizer = TfidfVectorizer()

#Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

#Get feature names (unique words)
feature_names = vectorizer.get_feature_names_out()

#Convert TF - IDf matrix to array
tfidf_array = tfidf_matrix.toarray()


#printing the output
for i, doc in enumerate(documents):
    print(f"\nDocumment {i+1}: {doc}")
    for j, word in enumerate(feature_names):
        print(f"{word}: {tfidf_array[i][j]:.4f}")