# BERT Embedding with Hugging Face Transformers

This project demonstrates how to extract contextual word embeddings using the BERT model from Hugging Face Transformers.

## 🔍 About
Unlike traditional models (Word2Vec, GloVe), BERT generates different embeddings for a word depending on its context. This makes it powerful for modern NLP tasks.

## 📦 Requirements
- transformers
- torch

Install via pip:
```bash
pip install transformers torch
```
## Sample output

Token: natural
Vector: tensor([ 0.0178, -0.0639, -0.4339,  0.0949, -0.5138])...

Token: language
Vector: tensor([ 0.0222,  0.2747, -0.8755, -0.3436,  0.0721])...

Token: processing
Vector: tensor([-0.4649,  0.3409,  0.1145, -0.8861,  0.1100])...

Token: is
Vector: tensor([ 0.4387,  0.2838, -0.5876, -0.1623,  0.3174])...

Token: amazing
Vector: tensor([ 0.2189,  0.1686, -0.0038,  0.1943,  0.7987])...

Token: .
Vector: tensor([ 0.1497,  0.3796, -0.0273, -0.0371,  1.1861])...