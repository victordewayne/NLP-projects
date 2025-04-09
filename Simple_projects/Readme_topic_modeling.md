# Simple Topic Modeling with LDA

This is a basic NLP project that uses **Latent Dirichlet Allocation (LDA)** to uncover hidden topics in a set of documents. The goal is to demonstrate how topic modeling works using the Gensim library.


## Features

- Text preprocessing with spaCy
- Tokenization, lemmatization, and stopword removal
- Bag-of-Words vectorization
- LDA model to extract topics
- Prints top keywords from each topic



## Tech Stack

- Python
- spaCy
- Gensim
- NumPy


## Sample output

Topics found:
[(0,
  '0.098*"well" + 0.059*"new" + 0.059*"every" + 0.059*"market" + 0.059*"hit" + '
 '0.059*"day" + 0.059*"high" + 0.059*"respond" + 0.059*"patient" + '
  '0.059*"medicine"'),
 (1,
  '0.066*"work" + 0.063*"new" + 0.063*"issue" + 0.063*"treatment" + '
  '0.063*"press" + 0.063*"reform" + 0.063*"say" + 0.063*"healthcare" + '      
  '0.063*"doctor" + 0.063*"future"')]
