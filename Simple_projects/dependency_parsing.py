import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "The quick brown fox jumps over the lazy dog."

doc = nlp(text)

for token in doc:
    print(f"{token.text:<10} {token.dep_:<15} {token.head.text}")

displacy.render(doc, style="dep")