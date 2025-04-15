# Character-Level Seq2Seq Chatbot (NLP Project)

This is a simple character-level chatbot built using the **Sequence-to-Sequence (Seq2Seq)** model with **LSTM layers** in TensorFlow/Keras. It takes in input strings one character at a time and generates character-level responses.  


## Project Highlights

- Built a **custom encoder-decoder model** using LSTMs.
- Used **teacher forcing** to train on character pairs (input → target).
- Created a chatbot interface that takes user input and generates a response.
- Trained on a **tiny dataset** to illustrate the basic concept.

## Example Interaction

Chatbot is ready! Type 'exit' to quit.
You: hi

Chatbot: helll
You: lol

Chatbot: hi
You: hi

Chatbot: helll
You: how are you?

Chatbot: i'm  oooo
You: who are you?

Chatbot: i'm  oooo
You:


Output may seem like gibberish — this is expected due to:
- Very limited training data
- Character-level granularity (no semantic understanding)
- No use of embeddings or pre-trained knowledge


## Libraries Used

- Python 3.8+
- TensorFlow / Keras
- NumPy


## What I Learned

- Basics of sequence-to-sequence modeling
- Character-level data preprocessing
- Training an encoder-decoder model with LSTM layers
- How to simulate a chatbot with generated responses

