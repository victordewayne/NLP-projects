# POS Tagging Project 

# Overview
This simple project demonstrates Part-of-Speech (POS) Tagging using NLTK in Python.  
POS tagging assigns grammatical categories (like noun, verb, adjective) to each word in a sentence.

# Features
- Tokenizes a sentence into words.
- Applies POS tagging using nltk.pos_tag().
- Identifies nouns, verbs, adjectives, determiners, and more.

# Example Output:
Original Text: The quick brown fox jumps over the lazy dog.
Tokenized Words: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.']
POS Tags: [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'), ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN'), ('.', '.')]
