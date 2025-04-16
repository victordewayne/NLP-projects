# Dependency Parsing using spaCy

This project demonstrates how to use spaCy to perform **dependency parsing**, a fundamental task in Natural Language Processing (NLP) for understanding the **grammatical structure** of sentences.

## What is Dependency Parsing?

Dependency parsing analyzes the grammatical structure of a sentence by establishing relationships between "head" words and words that modify those heads. It is widely used in:
- Grammar analysis
- Information extraction
- Semantic understanding
- Chatbot development
- Question answering systems

## Library used
    spaCY

    
## Example output

The quick brown fox jumps over the lazy dog.

The        det             fox
quick      amod            fox
brown      amod            fox
fox        nsubj           jumps
jumps      ROOT            jumps
over       prep            jumps
the        det             dog
lazy       amod            dog
dog        pobj            over
.          punct           jumps
