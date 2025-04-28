# Resume Matcher App with Streamlit

This is a **Resume Matcher** application built using **Streamlit**, which compares resumes and job descriptions to match skills and calculate a match score. The app extracts text from PDF files (Resume and Job Description), performs a skill extraction, and computes a similarity score between the two.

## Features

- **Upload PDFs**: Upload your resume and job description in PDF format.
- **Skill Extraction**: Extract and analyze the key skills mentioned in the resume and job description.
- **Match Score**: Calculate a **match score** based on the similarity between the resume and job description.
- **Common Skills**: Display the **common skills** between the two documents.

## Technologies Used

- **Python**
- **Streamlit**: For building the web application interface.
- **Spacy**: For natural language processing (NLP) to extract skills from text.
- **PyMuPDF (fitz)**: For reading PDF files.
- **Scikit-learn**: For text similarity calculation using cosine similarity.

## How to Run Locally

### Prerequisites

Make sure you have **Python 3.7+** installed. You will also need to install the following libraries:

- **Streamlit**
- **Spacy**
- **PyMuPDF (fitz)**
- **Scikit-learn**

You can install the necessary libraries using `pip`:

```bash
pip install streamlit spacy pymupdf scikit-learn
```

Additionally, you need to install the `en_core_web_sm` model for **Spacy**:

```bash
python -m spacy download en_core_web_sm
```

After installing run the app 

Open your browser and go to [http://localhost:8501](http://localhost:8501) to access the app.

## Usage

1. **Upload Resume PDF**: Click the button to upload your resume in PDF format.
2. **Upload Job Description PDF**: Click the button to upload the job description in PDF format.
3. Click the **Match Skills** button to initiate the analysis.
4. View the **match score** and the **list of common skills** between the two documents.

