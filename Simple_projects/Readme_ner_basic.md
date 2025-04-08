# Named Entity Recognition (NER) with spaCy

This project demonstrates basic and interactive usage of spaCy's Named Entity Recognition (NER) capabilities.

## What is NER?

NER is a natural language processing technique that locates and classifies named entities in text into predefined categories such as:

- `PERSON`: People, including fictional
- `ORG`: Companies, institutions, etc.
- `GPE`: Countries, cities, states
- `DATE`, `TIME`, `MONEY`, etc.

---

## Requirements

- Python 3.7+
- spaCy

Install dependencies:

```bash
pip install -U spacy
python -m spacy download en_core_web_sm
```

## Sample output

Enter your sentence: Victor is the CEO of Wayne Corp       

Named Entities:

Victor               -> PERSON     (People, including fictional)
Wayne Corp           -> ORG        (Companies, agencies, institutions, etc.)