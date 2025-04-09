import nltk
import spacy
from nltk.corpus import stopwords
from gensim import corpora
from gensim.models import LdaModel
from pprint import pprint

# Download stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')

# Load spacy model
nlp = spacy.load("en_core_web_sm")

# Sample documents
documents = [
    "The economy is working better than ever.",
    "Healthcare reform is a pressing issue.",
    "Doctors say the new treatment works.",
    "Markets are hitting new highs every day.",
    "The patient responded well to the medicine.",
    "Investors are optimistic about the future."
]

# Preprocessing function
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and token.text not in stop_words
    ]
    return tokens

# Preprocess all docs
processed_docs = [preprocess(doc) for doc in documents]

# Create Dictionary and Corpus
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(text) for text in processed_docs]

# Train LDA model
lda_model = LdaModel(corpus=corpus, num_topics=2, id2word=dictionary, passes=10)

# Display topics
print("\nTopics found:")
pprint(lda_model.print_topics())
