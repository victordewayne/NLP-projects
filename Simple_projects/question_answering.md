# Question Answering (QA) with Transformers

This project demonstrates two key approaches to **Question Answering (QA)** in Natural Language Processing:

- **Extractive QA** — finds answers *within* the given context
- **Abstractive QA** — *generates* answers based on understanding of the context

Both approaches are implemented using **Hugging Face Transformers**.


## 1. Extractive QA
Extractive QA **extracts** the exact answer span from a context.

### Example

**Context**:  
"Albert Einstein was born in Ulm, Germany in 1879."

**Question**:  
"Where was Einstein born?"

**Answer**:  
"Ulm, Germany"

## 2. Abstractive QA
Abstractive QA uses a text-to-text model like T5 to generate answers. It doesn't just pick an existing span — it can rephrase or summarize the answer using context understanding.

## Example
Context:
"The Mona Lisa is a half-length portrait painting by Italian artist Leonardo da Vinci. It is considered a masterpiece of the Renaissance."

Question:
"Who painted the Mona Lisa?"

Answer (Generated):
"Leonardo da Vinci"