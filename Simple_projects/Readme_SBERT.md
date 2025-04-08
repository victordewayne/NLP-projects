# Sentence-BERT Similarity Checker 

This project demonstrates how to use **Sentence-BERT (SBERT)** to compute semantic similarity between text sentences using powerful pre-trained language models.

## Setup

Make sure to activate your virtual environment and install dependencies:

```bash
pip install sentence-transformers
```
## Sample output

Similarity between:
 'Machine learning is amazing.'
 'Artificial intelligence is the future.'
 => 0.5453

Similarity between:
 'Machine learning is amazing.'
 'I love watching movies.'
 => 0.2335

Similarity between:
 'Machine learning is amazing.'
 'Learning algorithms is fun.'
 => 0.6936
