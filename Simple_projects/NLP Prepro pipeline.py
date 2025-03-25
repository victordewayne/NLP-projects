import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


nltk.download('punkt')
nltk.download('stopwords')

nlp =spacy.load("en_core_web_sm")

#Tokenization
def preprocess_text(text):
    tokens = word_tokenize(text)

    #Stopword removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    #Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    return stemmed_tokens

sample_text = "Natural Language Processing is an exciting field of Artificial Intelligence."
processed_tokens = preprocess_text(sample_text)

print("Original Text: ", sample_text)
print("Processed Tokens: ", processed_tokens)

#Lemmitization
def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop]
    return lemmatized_tokens

print("Lemmatized Text: ",lemmatize_text(sample_text))