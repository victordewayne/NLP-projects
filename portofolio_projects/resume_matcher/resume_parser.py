import re   
import spacy    


nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = ["python", "java", "sql", "machine learning", "excel", "data", "nlp", "analysis"]

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not found"

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not found"

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in SKILL_KEYWORDS if skill in text]
    return list(set(found))

def parse_resume(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text)
    }