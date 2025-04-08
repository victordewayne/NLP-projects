import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text =  input("Enter your sentence: ")

doc = nlp(text)

print("\nNamed Entities:\n")
for ent in doc.ents:
    print(f"{ent.text:20} -> {ent.label_:10} ({spacy.explain(ent.label_)})")

