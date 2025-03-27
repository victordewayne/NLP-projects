import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The quick brown fox jumps over the lazy dog."

#Tokenization
tokens = word_tokenize(text)

#Pos tagging
pos_tags = pos_tag(tokens)

print("Original text: ", text)
print("Tokenized text: ", tokens)
print("POS Tags:", pos_tags)