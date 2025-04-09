from textblob import TextBlob

texts = [
    "I love this product! It's amazing.",
    "This is the worst thing I've ever bought.",
    "It's okay, not great but not terrible either."
]

for text in texts:
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"\nText: {text}")
    print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")