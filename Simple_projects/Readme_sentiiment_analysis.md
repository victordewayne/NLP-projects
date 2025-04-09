# Sentiment Analysis (TextBlob)

This mini-project demonstrates basic sentiment analysis using the `TextBlob` library in Python.

## Description

Sentiment analysis is the process of identifying and categorizing opinions expressed in a piece of text.  
TextBlob provides a simple API for diving into common NLP tasks such as sentiment detection.

We extract:
**Polarity**: Float in range [-1.0, 1.0] where -1 indicates negative sentiment and +1 indicates positive.
**Subjectivity**: Float in range [0.0, 1.0] where 0 is very objective and 1 is very subjective.

## Sample output

Text: I love this product! It's amazing.
Polarity: 0.6125, Subjectivity: 0.75

Text: This is the worst thing I've ever bought.
Polarity: -1.0, Subjectivity: 1.0

Text: It's okay, not great but not terrible either.
Polarity: 0.19999999999999998, Subjectivity: 0.75
