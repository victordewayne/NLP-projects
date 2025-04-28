import streamlit as st
import spacy
import time
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the English model for spaCy
nlp = spacy.load('en_core_web_sm')

def preprocess(text):
    """Preprocesses the text by tokenizing, removing stopwords and non-alphabetic tokens."""
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return ' '.join(tokens)

SKILL_DB = [
    "python", "java", "c++", "sql", "excel", "data analysis", "machine learning",
    "deep learning", "nlp", "communication", "problem solving", "teamwork",
    "project management", "aws", "docker", "linux", "tensorflow", "pytorch",
    "fastapi", "django", "flask", "javascript", "html", "css", "power bi", "tableau"
]


def extract_skills(text):
    """Extracts known skills from the input text."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())

    # Tokens that are alphabetic and not stop words
    tokens = [token.text for token in doc if token.is_alpha and not token.is_stop]

    # Match only skills that are in SKILL_DB
    extracted = set()
    for token in tokens:
        if token.lower() in SKILL_DB:
            extracted.add(token.lower())

    return list(extracted)


def calculate_match(resume_text, jobdesc_text):
    """Calculates the match score between resume and job description."""
    processed_resume = preprocess(resume_text)
    processed_jobdesc = preprocess(jobdesc_text)
    
    vectorizer = CountVectorizer().fit_transform([processed_resume, processed_jobdesc])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    
    return similarity * 100

def read_pdf(file):
    """Reads a PDF file and extracts the text."""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def main():
    st.title("🔍 Resume Matcher App with PDF Upload + Skill Gap Analysis")
    st.subheader("Upload your Resume and Job Description (as PDF files)")
    
    resume_file = st.file_uploader("Upload Resume PDF", type=['pdf'])
    jobdesc_file = st.file_uploader("Upload Job Description PDF", type=['pdf'])
    
    if st.button("Match Skills 🚀"):
        if resume_file and jobdesc_file:
            with st.spinner('Analyzing... please wait'):
                resume_text = read_pdf(resume_file)
                jobdesc_text = read_pdf(jobdesc_file)
                
                match_score = calculate_match(resume_text, jobdesc_text)
                resume_skills = extract_skills(resume_text)
                jobdesc_skills = extract_skills(jobdesc_text)
                
                matched_skills = set(resume_skills).intersection(set(jobdesc_skills))
                missing_skills = set(jobdesc_skills) - set(resume_skills)
                
                time.sleep(2)  # simulate loading

            st.success(f"🎯 Match Score: {match_score:.2f}%")

            st.subheader("✅ Matched Skills")
            st.info(f"{', '.join(matched_skills) if matched_skills else 'No matching skills found'}")

            st.subheader("❌ Missing Skills (Consider learning these)")
            st.warning(f"{', '.join(missing_skills) if missing_skills else 'No missing skills detected! 🚀'}")

        else:
            st.error("Please upload both resume and job description PDFs!")

if __name__ == '__main__':
    main()
