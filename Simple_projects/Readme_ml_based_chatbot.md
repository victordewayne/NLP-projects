# ML-Based Chatbot using Scikit-learn

This project is a **Machine Learning-based chatbot** that understands user **intent** and responds intelligently. It uses `scikit-learn` and a simple dataset of intents.


## How It Works

- Uses a `.json` file (`intents.json`) with:
  - **Intents (tags)** like "greeting", "goodbye", etc.
  - **Patterns** (what the user might say)
  - **Responses** (what the bot should reply)
- Converts text input to features using **TF-IDF Vectorization**
- Classifies input intent using **Logistic Regression**
- Selects a random response from the matched intent


## Example Interaction

Chatbot is ready! Type 'exit' to quit.
You: hi
Chatbot:  Hello!
You: how are you?
Chatbot:  I'm an ML-powered chatbot.
You: What's your name?
Chatbot:  I'm an ML-powered chatbot.
You: bye
Chatbot:  Goodbye!
You: exit
Chatbot: Goodbye!