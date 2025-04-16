import spacy

nlp = spacy.load("en_core_web_trf")

text = "Barack Obama was the 44th President of the United States. Apple is looking at buying U.K. startup for $1 billion."

doc = nlp(text)

for ent in doc.ents:
    print(f"Entity: {ent.text}")
    print(f"Label: {ent.label_}")
    if ent.kb_id_:
        print(f"Linked Entity ID: {ent.kb_id_}")
        print(f"Confidence Score: {ent._.kb_ents}")
    else:
        print("No linked entity.")
    print("----")
