import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Spacy model
nlp = spacy.load('en_core_web_sm')

# Define intents
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "weather": ["weather", "temperature", "rain", "forecast"],
    "goodbye": ["bye", "goodbye", "see you", "take care"]
}

# Preprocess user input
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Recognize intent using cosine similarity
def recognize_intent(user_input):
    processed_input = preprocess(user_input)

    vectorizer = CountVectorizer()
    all_examples = []
    intent_labels = []

    for intent, examples in intents.items():
        all_examples.extend(examples)
        intent_labels.extend([intent] * len(examples))

    vectors = vectorizer.fit_transform(all_examples + [processed_input])
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1])

    best_match_idx = cosine_sim.argmax()
    best_match_score = cosine_sim[0, best_match_idx]

    if best_match_score > 0.3:  # Threshold for recognizing
        return intent_labels[best_match_idx]
    else:
        return "unknown"

# Chat function
def chat():
    context = {}

    print(" Hello! I am your chatbot. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(" Bot: Goodbye! Take care.")
            break

        intent = recognize_intent(user_input)

        if intent == "greeting":
            print(" Bot: Hello! How can I assist you today?")
        elif intent == "weather":
            if 'location' not in context:
                location = input(" Bot: Please tell me your location: ")
                context['location'] = location
            print(f" Bot: The weather in {context['location']} is sunny!")
        elif intent == "goodbye":
            print(" Bot: Goodbye! Have a nice day!")
            break
        else:
            print(" Bot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chat()
