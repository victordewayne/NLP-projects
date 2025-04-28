
# 🧠 Simple Chatbot using Intent Recognition and Context Memory

This is a basic chatbot that uses **Natural Language Processing (NLP)** techniques to recognize user intent and maintain short-term memory (context).  
The chatbot can handle greetings, weather queries (with location memory), and goodbyes.

---

## 🚀 Features

- Intent recognition using **Spacy** + **Cosine Similarity**.
- Preprocessing: lowercasing, removing stopwords, token filtering.
- Context memory to **remember user's location** during conversation.
- Simple command-line interface.
- Easy to extend with new intents!

---

## 📚 Tech Stack

- Python 3.x
- spaCy (`en_core_web_sm` model)
- Scikit-learn (`CountVectorizer`, `cosine_similarity`)

---

## 🛠️ Installation

1. Install the dependencies:

```bash
pip install spacy scikit-learn
python -m spacy download en_core_web_sm
```

---

## 🎯 How to Run

```bash
python chatbot.py
```

Example interaction:

```
You: hi
 Bot: Hello! How can I assist you today?

You: what's the weather
 Bot: Please tell me your location: 
You: Bangalore
 Bot: The weather in Bangalore is sunny!

You: bye
 Bot: Goodbye! Take care.
```

